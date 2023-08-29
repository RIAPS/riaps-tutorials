from riaps.run.comp import Component

class Bar(Component):
    def __init__(self):
        super(Bar, self).__init__()
        
    def on_subPort(self):
        msg = self.subPort.recv_pyobj()
        self.logger.info(f"Bar received: {msg}")