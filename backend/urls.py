from rest_framework import routers

from .views import CustomUserViewset, LaporanViewset

router = routers.SimpleRouter()

router.register(r'users',CustomUserViewset)
router.register(r'laporan', LaporanViewset)

urlpatterns = router.urls