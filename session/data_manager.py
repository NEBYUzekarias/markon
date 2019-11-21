from db import ConsumerCredential, TaskExecutions, ConsumerDevice , Tasks, Execution ,Subprocess , RewardTable , ProviderDevice
import logging 
import datetime 
log = logging.getLogger("session_manager")


def updateToken(db, cred, token):
    log.info("Token update to User '{}'.".format(cred.email))
    db.update(ConsumerCredential,
                where={"email": cred.email},
                update={"token": cred.token + token })

                    
def addTask(db,  cred , lg,order):
    time = datetime.datetime.now()
    try:
        task = db.query_all(Tasks, email = cred.email).pop() 
    except:
        task = None
    if not task:
        index = 1
    else:
        index = task.index + 1
    if db.add(Tasks, email= cred.email, date = time ,index = index):
            log.info("new task is recorded for user  '{}' ...".format(cred.email))
    else:
        log.error("Error adding new record of user '{}' ".format(cred.email))
        return None
    task = db.query(Tasks, email=cred.email, date=time)
    yolo_execution_id = addExecution(db, lg, order , task.task_id)
    return yolo_execution_id  , task.task_id 

def addExecution( db,  result , order, task_id ):
    time = datetime.datetime.now()
    if db.add(Execution, subprocess_id = order, result= result, date = time):
        log.info("add new execution of user ")
    else:
        log.error("Error adding new execution ")
    execution = db.query(Execution, subprocess_id=order, date=time)
    addTaskExecution(db , order , task_id, execution.execution_id)
    return execution.execution_id
def addTaskExecution(db, order, task_id, execution_id):
        if db.add(TaskExecutions,
                        order = order,
                        task_id = task_id,
                        execution_id = execution_id):
                        log.info("success on adding new task execution")

        else:
            log.error("error adding new task execution")

def updateExecution( db, execution_id, lg,  input_image = ""):
    db.update(Execution,
                            where = { "execution_id" : execution_id},
                            update ={ "network_rx": lg.get("net_rx"),
                                        "network_tx": lg.get("net_tx"),
                                        "memory_usage": lg.get("memory_usage"),
                                        "time_taken": lg.get("time_taken"),
                                        "cpu_usage" : lg.get("cpu_usage"),
                                        "input_image" : input_image
                                    })  

def updateProviderDeviceData(db,device_name, token_earned):
    provider_device = db.query(ProviderDevice, device_name=device_name)
    token_earned = provider_device.token_earned + token_earned 
    process_completed = provider_device.process_completed + 1
    db.update(ProviderDevice , where ={"device_name": device_name},
                                update ={"token_earned": token_earned,
                                         "process_completed": process_completed})
