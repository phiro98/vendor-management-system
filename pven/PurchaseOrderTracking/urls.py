from django.urls import path
from django.conf import settings
from django.urls import path, include
from PurchaseOrderTracking.views import POView, PODetailView, POacknowledge

urlpatterns = [
    path('', POView.as_view()),
    path('<po_number>/', PODetailView.as_view()),
    path('<po_number>/acknowledge', POacknowledge.as_view()),
]