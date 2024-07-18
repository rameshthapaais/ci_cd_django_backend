from rest_framework import viewsets
from .models import Program, Course, Lecturer, Student, StudentMark
from .serializers import ProgramSerializer, CourseSerializer, LecturerSerializer, StudentSerializer, StudentMarkSerializer

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LecturerViewSet(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentMarkViewSet(viewsets.ModelViewSet):
    queryset = StudentMark.objects.all()
    serializer_class = StudentMarkSerializer
