from django.urls import path, include
from .views import StudentAPIView, StudentDetail, GenericAPIView, StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('student', StudentViewSet, basename='student')


urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('student/', StudentAPIView.as_view()),
    path('student/detail/<int:id>/', StudentDetail.as_view()),
    path('generic/student/<int:id>/', GenericAPIView.as_view()),
]
