# from rest_framework import routers
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from django.contrib.auth import views as auth_views

from .views import (
    CustomUserList, 
    CustomUserDetail,
    LaporanDetailUserView, 
    LaporanListView,
    LaporanUpdateView,
    LaporanDetailIdView,
    LaporanDetailUserView,
    LaporanUpdatePusatView,
    RiwayatPenyakitCreateView,
    RiwayatPenyakitDetailView,
    CustomTOPV, 
    PasswordResetEmail,
    PasswordReset
    # DahLogin
    # LaporanViewset,
)

# router = routers.SimpleRouter()
# router.register(r'laporan', LaporanListView)
# router.register(r'riwayat', RiwayatPenyakitViewset)

urlpatterns = [
    # path('', include(router.urls)),
    # path('me/', DahLogin.as_view()), 
    path('password_reset/', PasswordReset.as_view(), name='password_reset_confirm'),
    path('laporan/', LaporanListView.as_view()),
    path('laporan/detail', LaporanDetailUserView.as_view()),
    path('laporan/<int:pk>', LaporanDetailIdView.as_view()),
    path('laporan/update/<int:pk>', LaporanUpdateView.as_view()),
    path('laporan/lapor_pusat/<int:pk>', LaporanUpdatePusatView.as_view()),
    path('riwayat/<str:nomor_induk>', RiwayatPenyakitDetailView.as_view()),
    path('riwayat/create/<str:nomor_induk>', RiwayatPenyakitCreateView.as_view()),
    path('users/', CustomUserList.as_view()),
    path('users/<str:nomor_induk>', CustomUserDetail.as_view()),
    path('token/', CustomTOPV.as_view(), name='obtain_token'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
