class ModelPreference(object):

    def __init__(self, **kargs):
        self.modelId = kargs['modelId'] if 'modelId' in kargs else ''
        self.identifier = kargs['identifier'] if 'identifier' in kargs else ''
        self.title = kargs['title'] if 'title' in kargs else ''
        self.changeIdentifier = kargs['changeIdentifier'] if 'changeIdentifier' in kargs else '1'
        self.askBeforeRename = kargs['askBeforeRename'] if 'askBeforeRename' in kargs else '0'
        self.onOpenModel = kargs['onOpenModel'] if 'onOpenModel' in kargs else 'openDiagram'
        self.onOpenDashId = kargs['onOpenDashId'] if 'onOpenDashId' in kargs else ''
