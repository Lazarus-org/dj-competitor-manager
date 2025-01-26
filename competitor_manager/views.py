from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Competitor, Feature, FeatureValue

def competitor_feature_table(request):
    """
    Optimized view to display a table of competitors and their feature values with pagination.
    """
    # Fetch all competitors and features with related feature values in a single query
    competitors = Competitor.objects.all()
    features = Feature.objects.prefetch_related('featurevalue_set').all()

    # Create a list of dictionaries to store feature values for each competitor
    feature_data = []
    for feature in features:
        feature_row = {'feature': feature}
        for competitor in competitors:
            # Get the feature value for the current competitor and feature
            feature_value = next(
                (fv for fv in feature.featurevalue_set.all() if fv.competitor_id == competitor.id),
                None
            )
            feature_row[competitor.id] = feature_value.value if feature_value else '-'
        feature_data.append(feature_row)

    # Paginate the feature_data (40 rows per page)
    paginator = Paginator(feature_data, 40)
    page_number = request.GET.get('page', 1)  # Get the current page number from the request
    page_obj = paginator.get_page(page_number)

    context = {
        'competitors': competitors,
        'features': features,
        'feature_data': page_obj,  # Pass the paginated data to the template
        'page_obj': page_obj,  # Pass the paginator object for navigation
    }
    return render(request, 'competitor_feature_table.html', context)