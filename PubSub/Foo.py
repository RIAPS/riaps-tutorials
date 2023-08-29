from riaps.run.comp import Component

class Foo(Component):

    def __init__(self):
        super(Foo, self).__init__()
        self.counter = 0

    def on_ticker(self):
        msg = self.ticker.recv_pyobj()
        self.logger.info(f"Foo sends: {self.counter}")
        self.pubPort.send_pyobj(self.counter)
        self.counter += 1