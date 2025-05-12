from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, ApiKeyViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'apikeys', ApiKeyViewSet, basename='apikey')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Correct path
]
