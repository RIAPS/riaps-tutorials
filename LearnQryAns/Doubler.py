from riaps.run.comp import Component
import spdlog

class Doubler(Component):

    def __init__(self):
        super(Doubler, self).__init__()