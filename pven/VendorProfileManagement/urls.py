from django.urls import path
from django.conf import settings
from django.urls import path, include
from VendorProfileManagement.views import VendorView, DetailView
from VendorPerformanceEvaluation.views import performanceView

urlpatterns = [
    path('', VendorView.as_view()),
    path('<vendor_code>/', DetailView.as_view()),
    path('<vendor_code>/performance', performanceView.as_view()),
]