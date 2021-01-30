# from rest_framework import routers
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    CustomUserList, 
    CustomUserDetail,
    LaporanDetailView, 
    LaporanListView,
    LaporanUpdateView,
    RiwayatPenyakitCreateView,
    RiwayatPenyakitDetailView
    # DahLogin
    # LaporanViewset,
)

# router = routers.SimpleRouter()
# router.register(r'laporan', LaporanListView)
# router.register(r'riwayat', RiwayatPenyakitViewset)

urlpatterns = [
    # path('', include(router.urls)),
    # path('me/', DahLogin.as_view()),
    path('laporan/', LaporanListView.as_view()),
    path('laporan/<str:nomor_induk>', LaporanDetailView.as_view()),
    path('laporan/update/<int:pk>', LaporanUpdateView.as_view()),
    path('riwayat/<str:nomor_induk>', RiwayatPenyakitDetailView.as_view()),
    path('riwayat/create/', RiwayatPenyakitCreateView.as_view()),
    path('users/', CustomUserList.as_view()),
    path('users/<str:nomor_induk>/', CustomUserDetail.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='obtain_token'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
