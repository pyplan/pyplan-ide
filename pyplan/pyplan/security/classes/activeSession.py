from rest_framework import serializers

class ActiveSession(object):

    def __init__(self):
        self.session_key = ""
        self.userName = ""
        self.currentModel = ""
        self.currentModelName = ""
        self.openAgo = 0
        self.activeAgo = 0
        self.timeoutIn = 0
        self.isPool = False
        self.currentModelFile = ""
        self.status = ""
        self.isGuest = False
        self.isCommonInstance = False
        self.readonly = False


class ActiveSessionSerializer(serializers.Serializer):
    session_key = serializers.CharField(default="")
    userName = serializers.CharField(default="")
    openAgo = serializers.IntegerField(default=0)
    activeAgo = serializers.IntegerField(default=0)
    currentModel = serializers.CharField(default="")
    currentModelName = serializers.CharField(default="")
    currentModelFile = serializers.CharField(default="")
    timeoutIn = serializers.IntegerField(default=0)
    isPool = serializers.BooleanField(default=False)
    status = serializers.CharField(default="")
    isGuest = serializers.BooleanField(default=False)
    isCommonInstance = serializers.BooleanField(default=False)
    readonly = serializers.BooleanField(default=False)
