from django.db import models

# Create your models here.
class Program(models.Model):
  """
  Model representing a program offered by SIS.
  """
  program_categories = [
    ('certificate', 'Certificate'),
    ('Level 5',f'Level 5'),
    ('Level 6', f'Level 6 ')
    ]
  name = models.CharField(max_length=255)
  duration_months = models.IntegerField()
  level = models.CharField(max_length=100, choices=program_categories)

  def __str__(self):
    return f"{self.name}-{self.level}"

class Course(models.Model):
  """
  Model representing a course offered by SIS.
  """
  name = models.CharField(max_length=255)
  program = models.ForeignKey(Program, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.name}, {self.program.level}"

class Lecturer(models.Model):
  """
  Model representing a lecturer at SIS.
  """
  name = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  courses = models.ManyToManyField(Course)

  def __str__(self):
    return self.name

class Student(models.Model):
  """
  Model representing a student at SIS.
  """
  name = models.CharField(max_length=255)
  student_id = models.CharField(max_length=10, unique=True)
  program = models.ForeignKey(Program, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class StudentMark(models.Model):
  """
  Model representing a student's mark for a course.
  """
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  mark = models.IntegerField()

  def __str__(self):
    return f"{self.student.name} - {self.course.name} ({self.mark})"