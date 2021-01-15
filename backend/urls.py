from rest_framework import routers
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import CustomUserViewset, LaporanViewset, MyTokenObtainPairView

router = routers.SimpleRouter()

router.register(r'users', CustomUserViewset)
router.register(r'laporan', LaporanViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
