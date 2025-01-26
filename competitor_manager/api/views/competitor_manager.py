from rest_framework import mixins, viewsets
from rest_framework.response import Response
from competitor_manager.models import Competitor, Feature
from competitor_manager.api.serializers.competitor_manager import CompetitorSerializer, FeatureSerializer

class CompetitorFeatureTableViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that returns a list of competitors and their feature values.
    """
    def list(self, request, *args, **kwargs):
        # Fetch all competitors and features with related feature values
        competitors = Competitor.objects.all()
        features = Feature.objects.prefetch_related('featurevalue_set').all()

        # Serialize the data
        competitor_serializer = CompetitorSerializer(competitors, many=True)
        feature_serializer = FeatureSerializer(features, many=True)

        # Construct the response data
        response_data = {
            'competitors': competitor_serializer.data,
            'features': feature_serializer.data,
        }

        return Response(response_data)