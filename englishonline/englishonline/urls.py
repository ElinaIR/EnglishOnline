"""
URL configuration for englishonline project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from study.views import *
from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# _________ EGE _________
router.register(r'ege/variants', EGEVariantViewSet)
router.register(r'ege/task1', Task1ViewSet)
router.register(r'ege/task2', EGETask2ViewSet)
router.register(r'ege/task3', EGETask3ViewSet)
router.register(r'ege/task4', EGETask4ViewSet)
router.register(r'ege/popularity', EGEPopularityViewSet)

# _________ OGE _________
router.register(r'oge/variants', OGEVariantViewSet)
router.register(r'oge/task1', Task1ViewSet)
router.register(r'oge/task2', OGETask2ViewSet)
router.register(r'oge/task3', OGETask3ViewSet)
router.register(r'oge/popularity', OGEPopularityViewSet)

# _________ VPR _________
router.register(r'vpr/variants', VPRVariantViewSet)
router.register(r'vpr/task1', Task1ViewSet)
router.register(r'vpr/task2', VPRTask2ViewSet)
router.register(r'vpr/popularity', VPRPopularityViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/base-audio/', BaseAudioView.as_view(), name='base-audio'),
    path('api/v1/cards/', include('cards.urls')),
    path('api/v1/get-csrf/', get_csrf_token),
    path('api/v1/register/', RegisterView.as_view(), name='register'),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
