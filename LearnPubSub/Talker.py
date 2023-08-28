from riaps.run.comp import Component

class Talker(Component):

    def __init__(self):
        super(Talker, self).__init__()
        self.counter = 0

    def on_ticker(self):
        msg = self.ticker.recv_pyobj()
        self.logger.info(f"Talker sends: {self.counter}")
        self.pubPort.send_pyobj(self.counter)
        self.counter += 1