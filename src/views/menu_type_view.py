from rest_framework.views import APIView

from src.models import MenuType
from src.serializers import MenuTypeSerializer
from rest_framework.response import Response


class MenuTypeView(APIView):
    def get(self, request):
        menutypes = MenuType.objects.all()
        serializer = MenuTypeSerializer(menutypes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MenuTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class RetrieveMenuTypeView(APIView):
    def get(self, request, id):
        menutypes = MenuType.objects.get(id=id)
        serializer = MenuTypeSerializer(menutypes)
        return Response(serializer.data)

    def put(self, request, id):
        menutype = MenuType.objects.get(id=id)
        serializer = MenuTypeSerializer(menutype, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id):
        menutype = MenuType.objects.get(id=id)
        menutype.delete()
        return Response("OK")
