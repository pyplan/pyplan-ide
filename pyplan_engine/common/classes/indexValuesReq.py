class IndexValuesReq(object):
    def __init__(self, **kargs):
        self.node_id = kargs['node_id'] if 'node_id' in kargs else None
        self.index_id = kargs['index_id'] if 'index_id' in kargs else None
        self.filter = kargs['filter'] if 'filter' in kargs else None
        self.text1 = kargs['text1'] if 'text1' in kargs else None
        self.text2 = kargs['text2'] if 'text2' in kargs else None
