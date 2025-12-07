from rest_framework import serializers
from masters.models import District

class DistrictSerializer(serializers.ModelSerializer):
    # extra field (read-only)
    region_name = serializers.CharField(source='region.name', read_only=True)

    class Meta:
        model = District
        fields = "__all__"
