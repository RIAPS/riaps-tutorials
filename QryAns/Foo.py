from riaps.run.comp import Component
import spdlog

class Foo(Component):

    def __init__(self):
        super(Foo, self).__init__()
        self.counter = 0

    def on_clock(self):
        _ = self.clock.recv_pyobj()
        self.logger.info(f"Asking for 2 * {self.counter}")
        self.queryPort.send_pyobj(self.counter)
        self.counter += 1

    def on_queryPort(self):
        qry, ans = self.queryPort.recv_pyobj()
        self.logger.info(f"2 * {qry} is {ans}")