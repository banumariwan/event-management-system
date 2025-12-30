from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from events.views import EventViewSet, TaskViewSet, AttendanceViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('events', EventViewSet)
router.register('tasks', TaskViewSet)
router.register('attendances', AttendanceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
