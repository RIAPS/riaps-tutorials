from riaps.run.comp import Component
import spdlog

class Bar(Component):

    def __init__(self):
        super(Bar, self).__init__()

    def on_answerPort(self):
        qry = self.answerPort.recv_pyobj()
        self.logger.info(f"Performing 2 * {qry}...")
        ans = 2 * qry
        # Remember to send a message back with the same port!
        self.answerPort.send_pyobj((qry,ans))