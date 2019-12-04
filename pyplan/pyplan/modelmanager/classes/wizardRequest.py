from pyplan.pyplan.modelmanager.classes.wizardParams import WizardParams

class WizardRequest(object):
    def __init__(self, **kargs):
        self.action = kargs["action"] if "action" in kargs else None
        self.wizard = kargs["wizard"] if "wizard" in kargs else None
        self.params = WizardParams(**kargs["params"]) if "params" in kargs else None
