from riaps.run.comp import Component
import spdlog

class Ticker(Component):

    def __init__(self):
        super(Ticker, self).__init__()
        self.counter = 1

    def on_ticker(self):
        msg = self.ticker.recv_pyobj()
        self.logger.info(f"Sending {self.counter}")
        self.counter += 1
        self.pubPort.send_pyobj(self.counter)