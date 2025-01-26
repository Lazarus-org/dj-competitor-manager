from django.urls import path
from .views import competitor_feature_table

urlpatterns = [
    path('competitor-feature-table/', competitor_feature_table, name='competitor_feature_table'),
]