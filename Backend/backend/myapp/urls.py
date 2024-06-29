from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApplicantViewSet, VacancyViewSet

router = DefaultRouter()
router.register(r'applicants', ApplicantViewSet)
router.register(r'vacancies', VacancyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


