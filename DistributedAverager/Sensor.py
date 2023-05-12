from riaps.run.comp import Component
import spdlog
import random


class Sensor(Component):

    def __init__(self):
        super(Sensor, self).__init__()

    def on_randomGenSub(self):
        msg = self.randomGenSub.recv_pyobj()
        localValue = msg+4*(random.random()-0.5) #Add noise randomly from uniform dist. [-2,2]
        self.logger.info(f"Sensor reading: {localValue}")
        self.sensorDataPub.send_pyobj(localValue)