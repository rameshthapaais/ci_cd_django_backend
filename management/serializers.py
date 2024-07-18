from rest_framework import serializers
from .models import Program, Course, Lecturer, Student, StudentMark

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['id', 'name', 'duration_months', 'level']

class CourseSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Course
        fields = ['id', 'name', 'program']

# class LecturerSerializer(serializers.ModelSerializer):
#     courses = CourseSerializer(many=True)

#     class Meta:
#         model = Lecturer
#         fields = ['id', 'name', 'email', 'courses']

class LecturerSerializer(serializers.ModelSerializer):
    # courses = CourseSerializer(many=True)

    class Meta:
        model = Lecturer
        fields = ['id', 'name', 'email', 'courses']

    # def create(self, validated_data):
    #     courses_data = validated_data.pop('courses')
    #     lecturer = Lecturer.objects.create(**validated_data)
    #     for course_data in courses_data:
    #         Course.objects.create(lecturer=lecturer, **course_data)
    #     return lecturer

    # def update(self, instance, validated_data):
    #     courses_data = validated_data.pop('courses')
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()

    #     # Assuming that all courses need to be replaced
    #     instance.courses.clear()
    #     for course_data in courses_data:
    #         Course.objects.create(lecturer=instance, **course_data)

    #     return instance
    
   

class StudentSerializer(serializers.ModelSerializer):
    # program = ProgramSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'student_id', 'program']

class StudentMarkSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = StudentMark
        fields = ['id', 'student', 'course', 'mark']
