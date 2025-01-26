from django.urls import path, include
from rest_framework.routers import DefaultRouter
from competitor_manager.api.views.competitor_manager import CompetitorFeatureTableViewSet

router = DefaultRouter()
router.register(r'competitor-feature-table', CompetitorFeatureTableViewSet, basename='competitor-feature-table')

urlpatterns = router.urls