from riaps.run.comp import Component
import spdlog


class Averager(Component):

    def __init__(self, name, Ts):
        super(Averager, self).__init__()
        self.name = name
        self.sensorUpdate = False
        self.dataValues = {}
        self.Ts = Ts
        self.ownValue = 0
        
    def on_sensorData(self):
        self.sensorValue = self.sensorData.recv_pyobj()
        self.dataValues = {}
        self.sensorUpdate = True
        
    def on_nodeDataSub(self):
        msg = self.nodeDataSub.recv_pyobj()
        name,value = msg
        if name != self.name:
            self.dataValues[name] = value
        
    def on_update(self):
        msg = self.update.recv_pyobj()
        if self.sensorUpdate:
            self.ownValue = self.sensorValue
            self.sensorUpdate = False
        if len(self.dataValues) != 0:
            sum = 0.0
            for value in self.dataValues.values():
                sum += (self.ownValue - value)
            der = sum / self.Ts
            self.ownValue -= der
        msg = (self.name,self.ownValue)
        self.nodeDataPub.send_pyobj(msg)
        
    def on_display(self):
        msg = self.display.recv_pyobj()
        self.logger.info(f'Local Estimate: {self.ownValue}')