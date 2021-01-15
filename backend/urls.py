from rest_framework import routers
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    CustomUserList, 
    CustomUserDetail,
    LaporanDetail,
    LaporanList
)

urlpatterns = [
    path('laporan/', LaporanList.as_view()),
    path('laporan/<int:pk>/', LaporanDetail.as_view()),
    path('users/', CustomUserList.as_view()),
    path('users/<str:nomor_induk>/', CustomUserDetail.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='obtain_token'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
