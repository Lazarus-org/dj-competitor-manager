from rest_framework import serializers
from competitor_manager.models import Competitor, Feature, FeatureValue

class FeatureValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureValue
        fields = ['competitor_id', 'value']

class FeatureSerializer(serializers.ModelSerializer):
    feature_values = FeatureValueSerializer(many=True, read_only=True, source='featurevalue_set')

    class Meta:
        model = Feature
        fields = ['id', 'name', 'feature_values']

class CompetitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competitor
        fields = ['id', 'name', 'competitor_type']