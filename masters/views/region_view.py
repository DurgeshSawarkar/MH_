from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from masters.models import Region
from masters.serializers import RegionSerializer


@method_decorator(csrf_exempt, name='dispatch')
class RegionAPIView(APIView):

    def get(self, request):
        print(">>> GET METHOD CALLED")
        regions =  Region.objects.filter(is_deleted=False).order_by('-id')
        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        print(">>> POST METHOD CALLED")
        serializer = RegionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    


@method_decorator(csrf_exempt, name='dispatch')
class RegionDetailAPIView(APIView):

    def get(self, request, pk):
        print(">>> GET Detail METHOD CALLED")
        try:
            region = Region.objects.get(pk=pk, is_deleted=False)
        except Region.DoesNotExist:
            return Response({"error": "Region not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = RegionSerializer(region)
        return Response(serializer.data)

    def put(self, request, pk):
        print(">>> PUT METHOD CALLED")
        try:
            region = Region.objects.get(pk=pk, is_deleted=False)
        except Region.DoesNotExist:
            return Response({"error": "Region not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = RegionSerializer(region, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        print(">>> DELETE METHOD CALLED")
        try:
            region = Region.objects.get(pk=pk, is_deleted=False)
        except Region.DoesNotExist:
            return Response({"error": "Region not found"}, status=status.HTTP_404_NOT_FOUND)

        region.is_deleted = True
        region.save()
        return Response({"message": "Region deleted"}, status=200)
