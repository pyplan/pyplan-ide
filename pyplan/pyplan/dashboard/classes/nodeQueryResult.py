from .nodeDimension import NodeDimension


class NodeQueryResult(object):
    def __init__(self, **kargs):
        self.node = kargs['node'] if 'node' in kargs else None
        self.dims = list(map(lambda item: NodeDimension(**item), kargs['dims'])) if 'dims' in kargs else []
        self.rows = list(map(lambda item: NodeDimension(**item), kargs['rows'])) if 'rows' in kargs else []
        self.columns = list(map(lambda item: NodeDimension(**item),
                                kargs['columns'])) if 'columns' in kargs else []
        self.summaryBy = kargs['summaryBy'] if 'summaryBy' in kargs else 'sum'
        self.fromRow = kargs['fromRow'] if 'fromRow' in kargs else None
        self.toRow = kargs['toRow'] if 'toRow' in kargs else None
        self.bottomTotal = kargs['bottomTotal'] if 'bottomTotal' in kargs else False
        self.rightTotal = kargs['rightTotal'] if 'rightTotal' in kargs else False
        self.timeFormat = kargs['timeFormat'] if 'timeFormat' in kargs else 'A'
        self.timeFormatType = kargs['timeFormatType'] if 'timeFormatType' in kargs else 'FLO'
        self.calendarType = kargs['calendarType'] if 'calendarType' in kargs else 'CAL'
        self.resultType = kargs['resultType'] if 'resultType' in kargs else ''
