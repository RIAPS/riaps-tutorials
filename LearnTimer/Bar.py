from riaps.run.comp import Component

class Bar(Component):
    def __init__(self):
        super(Bar, self).__init__()

    def handleActivate(self):
        self.clock.setDelay(3.0) # Delay for 1 s
        self.clock.launch() # Start the timer
        self.logger.info("I will say Hello world! in 3 seconds...")

    def on_clock(self):
        msg = self.clock.recv_pyobj() # Required to remove the timer message from the message queue
        self.logger.info(f"Hello world!")