from riaps.run.comp import Component

class Listener(Component):
    def __init__(self):
        super(Listener, self).__init__()
        
    def on_subPort(self):
        msg = self.subPort.recv_pyobj()
        self.logger.info(f"Listener received: {msg}")