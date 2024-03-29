from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from main.serializers import DocumentSerializer

# Create your views here.
class DocumentUploadView(APIView):
# MultiPartParser AND FormParser
# "You will typically want to use both FormParser and MultiPartParser
# together in order to fully support HTML form data."
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        file_serializer = DocumentSerializer(data=request.data, context={"request": request})
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)