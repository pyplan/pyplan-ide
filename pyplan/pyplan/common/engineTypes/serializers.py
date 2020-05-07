from rest_framework import serializers


from pyplan_core.classes.common.filterChoices import filterChoices
from pyplan_core.classes.common.indexValuesReq import IndexValuesReq


class IndexValuesReqSerializer(serializers.Serializer):
    node_id = serializers.CharField(required=False, allow_blank=True)
    index_id = serializers.CharField()
    filter = serializers.ChoiceField(required=False, choices=[
                                     (e.value, e.name) for e in filterChoices])
    text1 = serializers.CharField(required=False)
    text2 = serializers.CharField(required=False)

    def create(self, validated_data):
        return IndexValuesReq(**validated_data)
