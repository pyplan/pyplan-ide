class GeoQuery(object):
    def __init__(self, **kargs):
        self.node = kargs["node"] if "node" in kargs else None
        self.zoom = kargs["zoom"] if "zoom" in kargs else None
        self.lat1 = kargs["lat1"] if "lat1" in kargs else None
        self.lat2 = kargs["lat2"] if "lat2" in kargs else None
        self.lng1 = kargs["lng1"] if "latlng1Field" in kargs else None
        self.lng2 = kargs["lng2"] if "lng2" in kargs else None
        self.isCluster = kargs["isCluster"] if "isCluster" in kargs else False
        self.latField = kargs["latField"] if "latField" in kargs else None
        self.lngField = kargs["lngField"] if "lngField" in kargs else None
        self.geoField = kargs["geoField"] if "geoField" in kargs else None
        self.geoLimitLat1 = kargs["geoLimitLat1"] if "geoLimitLat1" in kargs else None
        self.geoLimitLat2 = kargs["geoLimitLat2"] if "geoLimitLat2" in kargs else None
        self.geoLimitLng1 = kargs["geoLimitLng1"] if "geoLimitLng1" in kargs else None
        self.geoLimitLng2 = kargs["geoLimitLng2"] if "geoLimitLng2" in kargs else None
        self.rowIndex = kargs["rowIndex"] if "rowIndex" in kargs else None
        self.attIndex = kargs["attIndex"] if "attIndex" in kargs else None
        self.sizeField = kargs["sizeField"] if "sizeField" in kargs else None
        self.sizeAggregator = kargs["sizeAggregator"] if "sizeAggregator" in kargs else None
        self.colorField = kargs["colorField"] if "colorField" in kargs else None
        self.colorAggregator = kargs["colorAggregator"] if "colorAggregator" in kargs else None
        self.labelField = kargs["labelField"] if "labelField" in kargs else None
        self.labelAggregator = kargs["labelAggregator"] if "labelAggregator" in kargs else None
        self.iconField = kargs["iconField"] if "iconField" in kargs else None
        self.iconAggregator = kargs["iconAggregator"] if "iconAggregator" in kargs else None
        self.extraData = kargs["extraData"] if "extraData" in kargs else None
        self.id = kargs["id"] if "id" in kargs else None
