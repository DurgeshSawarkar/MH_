from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from masters.models import District
from masters.serializers import DistrictSerializer


@method_decorator(csrf_exempt, name='dispatch')
class DistrictAPIView(APIView):
    
    # LIST + FILTER
    def get(self, request):
        region_id = request.GET.get("region_id")

        queryset = District.objects.filter(is_deleted=False)

        if region_id:
            queryset = queryset.filter(region_id=region_id)

        queryset = queryset.order_by('-id')

        serializer = DistrictSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # CREATE
    def post(self, request):
        serializer = DistrictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@method_decorator(csrf_exempt, name='dispatch')
class DistrictDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return District.objects.get(pk=pk, is_deleted=False)
        except District.DoesNotExist:
            return None

    # GET SINGLE DISTRICT
    def get(self, request, pk):
        district = self.get_object(pk)
        if not district:
            return Response({"error": "District not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DistrictSerializer(district)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # UPDATE DISTRICT
    def put(self, request, pk):
        district = self.get_object(pk)
        if not district:
            return Response({"error": "District not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DistrictSerializer(district, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # SOFT DELETE
    def delete(self, request, pk):
        district = self.get_object(pk)
        if not district:
            return Response({"error": "District not found"}, status=status.HTTP_404_NOT_FOUND)

        district.is_deleted = True
        district.save()
        return Response({"message": "District deleted"}, status=status.HTTP_200_OK)
