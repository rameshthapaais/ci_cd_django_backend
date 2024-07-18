from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ProgramViewSet, CourseViewSet, LecturerViewSet, StudentViewSet, StudentMarkViewSet

router = DefaultRouter()
router.register(r'programs', ProgramViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'lecturers', LecturerViewSet)
router.register(r'students', StudentViewSet)
router.register(r'studentmarks', StudentMarkViewSet)

urlpatterns = [
    path('sis/', include(router.urls)),
]
