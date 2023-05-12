from riaps.run.comp import Component
import spdlog
import random


class RandomGen(Component):

    def __init__(self):
        super(RandomGen, self).__init__()

    def on_clock(self):
        msg = self.clock.recv_pyobj()
        theValue = random.random()*20
        self.logger.info(f"New target average: {theValue}")
        self.randomGenPub.send_pyobj(theValue)
        
        