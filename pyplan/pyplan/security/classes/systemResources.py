from rest_framework import serializers

class SystemResources(object):

    def __init__(self):
        self.totalMemory = 0
        self.usedMemory = 0
        self.usedCPU = 0
        self.pid = ""
        self.engineURI = ""
        self.engineUID = ""
        self.engineParams = ""
        self.sessionStatus = ""


class SystemResourcesSerializer(serializers.Serializer):

    totalMemory = serializers.FloatField(default=0)
    usedMemory = serializers.FloatField(default=0)
    usedCPU = serializers.FloatField(default=0)

    sessionStatus = serializers.CharField(default="")
    engineURI = serializers.CharField(default="")
    engineUID = serializers.CharField(default="")
    engineParams = serializers.CharField(default="")
