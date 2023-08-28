from riaps.run.comp import Component

class Foo(Component):
    def __init__(self):
        super(Foo, self).__init__()

    def on_clock(self):
        msg = self.clock.recv_pyobj() # Required to remove the timer message from the message queue
        self.logger.info(f"Hello world!")