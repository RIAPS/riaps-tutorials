from riaps.run.comp import Component
import spdlog

class QueryGenerator(Component):

    def __init__(self):
        super(QueryGenerator, self).__init__()
        self.counter = 1

    def on_clock(self):
        msg = self.clock.recv_pyobj()
        self.logger.info(f"Requesting double of {self.counter}")
        self.queryPort.send_pyobj(self.counter)
        self.counter += 1

    def on_queryPort(self):
        msg = self.queryPort.recv_pyobj()
        self.logger.info(f"Answer was {msg}")