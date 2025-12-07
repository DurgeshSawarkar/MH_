from django.urls import path
from masters.views.district_view import DistrictAPIView, DistrictDetailAPIView
from masters.views import RegionAPIView, RegionDetailAPIView

urlpatterns = [
    path('regions/', RegionAPIView.as_view()),              # List + POST
    path('regions/<int:pk>/', RegionDetailAPIView.as_view()),  # GET single + PUT + DELETE
    # District
    path('districts/', DistrictAPIView.as_view()),
    path('districts/<int:pk>/', DistrictDetailAPIView.as_view()),


]
