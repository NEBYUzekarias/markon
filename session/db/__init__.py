from sqlalchemy import Column, Integer, String, ForeignKey ,Float ,DateTime
from sqlalchemy.orm import relationship
import datetime
from .interface import Base


class Credential(Base):
    __tablename__ = "credential"
    email = Column(String(256),
                      primary_key=True,
                      unique=True,
                      nullable=False)
    username = Column(String(256))
    password = Column(String(256))
    picture = Column(String())
    token = Column(Float, default=50.00)
    tasks =relationship("Tasks",backref="credential", single_parent=True)
    active_device = Column(String(256), default="")
    devices = relationship("Device",
                           backref="credential",
                           lazy=True,
                           cascade="all, delete, delete-orphan",
                           single_parent=True)

    def __repr__(self):
        return "EMAIL     : {}\n" \
               "TOKEN        : {}\n" \
               "ACTIVE_DEVICE: {}\n" \
               "DEVICES      : {}\n".format(self.email,
                                            self.token,
                                            self.active_device,
                                            self.devices)


class Device(Base):
    __tablename__ = "devices"
    dev_id = Column(Integer, primary_key=True)
    device_name = Column(String(256), nullable=False)
    access_token = Column(String(256), default="")
    email = Column(String(256),
                      ForeignKey("credential.email"),
                      nullable=False)

    def __repr__(self):
        return "EMAIL    : {}\n" \
               "DEVICE_NAME : {}\n" \
               "ACCESS_TOKEN: {}\n".format(self.email,
                                           self.device_name,
                                           self.access_token)


class Tasks(Base):
    __tablename__="tasks"
    task_id = Column(Integer, primary_key= True)
    index = Column(Integer)
    date = Column(DateTime, default=datetime.datetime.now())
    tasks_executions =relationship("TaskExecutions",backref="tasks", single_parent=True)
    reward = Column (Float())
    email= Column(String(256),
                      ForeignKey("credential.email"),
                      nullable=False)


