from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include,path

from SNet.views import homeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView.as_view(), name=''),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) +\
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
