from django.shortcuts import render
from rest_framework import generics, mixins, viewsets, status
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializers import StudentSerializer



class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    

    
class GenericAPIView(
    generics.GenericAPIView, 
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin):

    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)
    
    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)



class StudentAPIView(APIView):
    
    def get(self, request):
        all_student = Student.objects.all()
        serializer = StudentSerializer(all_student, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class StudentDetail(APIView):

    def get_object(self, id):

        try:
            return Student.objects.get(id=id)
        except Article.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        student = self.get_object(id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, id):
        student = self.get_object(id)
        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = self.get_object(id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)