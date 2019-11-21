import json
import grpc
import sys
import os
import logging
import argparse
import random
import string
import time
import json
import urllib3
from concurrent import futures
import datetime
from db import ConsumerCredential, TaskExecutions, ConsumerDevice , Tasks, Execution ,Subprocess , RewardTable , ProviderDevice
from db.interface import Database
from fractions import Fraction
from sqlalchemy.ext.declarative import DeclarativeMeta
import base64
import data_manager as dm
import pickle
import session_pb2_grpc as sm_pb2_grpc
import session_pb2 as sm_pb2

import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from organizer import Orchestrator


logging.basicConfig(format="%(asctime)s - [%(levelname)8s] "
                           "- %(name)s - %(message)s", level=logging.INFO)
log = logging.getLogger("session_manager")

ONE_DAY_IN_SECONDS = 60 * 60 * 24

try:
    nunet_port = os.environ['NUNET_PORT']
except:
    nunet_port = None
    print("no env variable NUNET_PORT")

if not nunet_port:
    nunet_port = 50000

class Status:
    OK = 0
    UNAUTHENTICATED = 1
    CANCELLED = 2
    UNKNOWN = 3
    NO_Sufficient_TOKEN =4

class Tag:
    ERROR = "error"
    LOG = "log"
   

def generate_access_token(length=15):
    key = ''.join(random.choice(string.ascii_letters + string.digits)
                  for _ in range(length))
    return key.upper()

class SessionServicer(sm_pb2_grpc.SessionServicer):

    def __init__(self, db_session,  timeout=20):
        self.db = db_session
        self.timeout = timeout
        self.min_token = 20
        self.token_spent_per_process = 15
        self.top_5=''

    def signup(self , request, context):
        cred = self.db.query(ConsumerCredential, email=request.email)
        if not cred: 
            if self.db.add(ConsumerCredential, email= request.email, password=self.db.hash_password(request.password)):
                log.info("Credential with email addres '{}' added.".format(request.email))
                return sm_pb2.SignupOutput(status= Status.OK )
            else:
                log.error("Error adding '{}'!".format(request.email))
                return self.set_grpc_context(context,
                                                sm_pb2.SignupOutput(),
                                                "Email addres already in use!",
                                                grpc.StatusCode.ALREADY_EXISTS)
        else:
            return self.set_grpc_context(context,
                                                sm_pb2.SignupOutput(),
                                                "Email addres already in use!",
                                                grpc.StatusCode.ALREADY_EXISTS)
        

        

    def login(self, request, context):
        cred = self.db.query(ConsumerCredential, email=request.email, password=request.password)
        if not cred:
            return self.set_grpc_context(context, sm_pb2.LoginOutput(), "User not registered!", grpc.StatusCode.NOT_FOUND)
        
        if self.db.query_all(Tasks , email = cred.email ): 
            first_task_flag = False 
        else: 
            first_task_flag = True 
        # Check if the Device is already registered
        device = self.db.query(ConsumerDevice, device_name=request.device_name, email=request.email)

        # Check if the Device is the active one
        if device and cred.active_device == device.device_name:
            log.warning("Device is already active and logged in.")
            return sm_pb2.LoginOutput(access_token=device.access_token,
                                  bool = first_task_flag)

        access_token = generate_access_token()
        if not device:
            log.info("Registering new Device: '{}'".format(request.device_name))
            self.db.add(ConsumerDevice,device_name=request.device_name,access_token=access_token,email=cred.email)
        elif device.access_token == "":
            log.info("Setting new access_token for: '{}'".format(request.device_name))
            self.db.update(ConsumerDevice, where={"email": cred.email,"device_name": device.device_name},
                                           update={"access_token": access_token})
        else:
            access_token = device.access_token
            log.warning("Device '{}' is already logged in.".format(request.device_name))

           
        return sm_pb2.LoginOutput(access_token=access_token ,
                                  bool = first_task_flag)

    def logout(self, request, context):
        cred, device, access_token  = self.validate_access(context)
        if not access_token:
            return self.set_grpc_context(context, sm_pb2.LogoutOutput(), "You have already logged out!", grpc.StatusCode.UNAUTHENTICATED)
        if cred.active_device == request.device_name:
            log.info("The active Device is logging out...")
            self.set_active_device(device.email, "")
        log.info("Updating the ConsumerDevice info...")
        self.db.update(ConsumerDevice,where={"dev_id": device.dev_id},
                                      update={"access_token": ""})
        return sm_pb2.LogoutOutput(status=Status.OK)

    def socialMediaLogin(self, request, context):
        http = urllib3.PoolManager()
        if request.media == 'facebook':
            content = http.request('GET', 'https://graph.facebook.com/me?fields=email,name,picture&access_token='+request.access_token)
        elif request.media == 'google':
            content = http.request('GET', 'https://www.googleapis.com/oauth2/v1/userinfo?access_token='+request.access_token)
        
        access_token = generate_access_token()
        if content.status == 200:
            data = json.loads(content.data.decode('utf-8'))
            #first_name = data['given_name']
            if request.media=='facebook':
                picture = data['picture']['data']['url']
            elif request.media == 'google':
                picture = data['picture']

            cred = self.db.query(ConsumerCredential,  email =data['email'])
            if self.db.query_all(Tasks , email = data['email']): 
                first_task_flag = False 
            else: 
                first_task_flag = True 
            if not cred:
                log.info("Registering new user: '{}'".format(data['email']))
                self.db.add(ConsumerCredential,
                            picture= picture,
                            email = data['email'])
                self.db.add(ConsumerDevice,
                            device_name=request.device_name,
                            access_token=access_token,
                            email = data['email']) 
                return sm_pb2.LoginOutput(access_token=access_token,
                                  bool = first_task_flag)

            # check if the device is already registered
            device = self.db.query(ConsumerDevice, 
                                    device_name=request.device_name,
                                    email = data['email'])
            if device and cred.active_device == device.device_name:
                log.warning("Device is already active and logged in.")
                return sm_pb2.LoginOutput(access_token=device.access_token , bool = first_task_flag)
            if not device:
                log.info("Registering new Device: '{}'".format(request.device_name))
                self.db.add(ConsumerDevice,
                            device_name=request.device_name,
                            access_token=access_token,
                            email = data['email'])
            elif device.access_token == "":
                log.info("Setting new access_token for: '{}'".format(request.device_name))
                self.db.update(ConsumerDevice, where={"email": cred.email,"device_name": device.device_name},
                                            update={"access_token": access_token})
                
            else:
                access_token = device.access_token
                log.warning("Device '{}' is already logged in.".format(request.device_name))

            return sm_pb2.LoginOutput(access_token=access_token , bool = first_task_flag)
        else:
            return self.set_grpc_context(context, sm_pb2.LoginOutput(), "User not registered!", grpc.StatusCode.UNAUTHENTICATED)


        
    def userInfo(self, request, context):
        cred, _, access_token = self.validate_access(context)
        if not access_token:
            return self.set_grpc_context(context, sm_pb2.UserInfoOutput(), "Invalid access!", grpc.StatusCode.UNAUTHENTICATED)
        tasks = self.db.query_all(Tasks , email = cred.email )
        task_run = len(tasks)
        total_token_spent = task_run * self.token_spent_per_process
        total_reward = 0.0
        completed_task = 0
        for task in tasks:
            if self.db.query(TaskExecutions, task_id = task.task_id, order = 1):
                completed_task +=1

        for rewards in tasks:
            if rewards.reward:
                total_reward += rewards.reward

        
        return sm_pb2.UserInfoOutput(email=cred.email,
                                      picture = cred.picture,
                                      balance = cred.token,
                                      total_token_spent = total_token_spent,
                                      total_reward = total_reward,
                                      task_run = task_run,
                                      completed_task =completed_task

                                      )



    def validate_access(self, context):
        access_token = self.get_access_token(context.invocation_metadata())
        if not access_token:
            log.error("No access token!")
            return None, None, None
        device = self.db.query(ConsumerDevice, access_token=access_token)

        if not device:
            log.error("Device not registered!")
            return None, None, None 
        cred = self.db.query(ConsumerCredential, email=device.email)
        if not cred:
            log.error("User not registered!")
            return None, None, None

        return cred, device, access_token

    # Set the active_device column of ConsumerCredential with the device_name
    def set_active_device(self, email, device_name):
        log.info("Setting {}.active_device to '{}'".format(email,
                                                           device_name))
        return self.db.update(ConsumerCredential,
                              where={"email": email},
                              update={"active_device": device_name})


    @staticmethod
    def set_grpc_context(context, message_type, msg, code=None):
        log.warning(msg)
        context.set_details(msg)
        if code:
            context.set_code(code)
        return message_type
    # Checks if the incoming request is valid

    @staticmethod
    def get_access_token(metadata):
        for key, value in metadata:
            if key == "access_token" and value:
                return value
        return None
    @staticmethod
    def object_as_dict(obj):
        return {c.key: getattr(obj, c.key)
                for c in inspect(obj).mapper.column_attrs}



class Server:
    def __init__(self,
                 db_file="sessions.db",
                 db_create=False,
                 port=nunet_port,
                ):

        self.db_file = db_file
        self.db_create = db_create
        self.db = Database(db_file=db_file, db_create=db_create)
        self.port = port
        self.server = None
        self.timeout = 30
    def start_server(self):
        hundred_MB = (1024 ** 2) * 100   # max grpc message size

        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=20),
            options=[
            ('grpc.max_receive_message_length', hundred_MB)
        ])

        sm_pb2_grpc.add_SessionServicer_to_server(
            SessionManagerServicer(db_session=self.db,
                                   timeout=self.timeout), self.server )
        self.server.add_insecure_port("[::]:{}".format(self.port))
        log.info("Starting Server at localhost:{}".format(
            self.port))
        self.server.start()

    def stop_server(self):
        self.server.stop(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--db-file",
                        "-db",
                        dest="db_file",
                        default="sessions.db",
                        help="DB file name")
    parser.add_argument("--db-create",
                        action="store_true",
                        dest="db_create",
                        default=False,
                        help="Force DB creating")
    parser.add_argument("--port",
                        "-p",
                        type=int,
                        default=nunet_port,
                        help="Server port")

    args = parser.parse_args()

    server = Server(db_file=args.db_file,
                                  db_create=args.db_create,
                                  port=args.port,

                                  )
    server.start_server()

    try:
        while True:
            time.sleep(ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop_server()
