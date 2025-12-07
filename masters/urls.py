from django.urls import path
from masters.views import RegionAPIView, RegionDetailAPIView

urlpatterns = [
    path('regions/', RegionAPIView.as_view()),              # List + POST
    path('regions/<int:pk>/', RegionDetailAPIView.as_view()),  # GET single + PUT + DELETE
]
