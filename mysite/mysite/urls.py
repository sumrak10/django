from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include,path

from django.contrib.auth.views import LoginView

from mysite.views import homeView, LogoutView, RegisterView, ProfileView, EditProfileView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView.as_view(), name=""),
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('accounts/logout/', LogoutView.as_view(), name="logout"),
    path('accounts/register/', RegisterView.as_view(), name="register"),
    path('accounts/profile/', ProfileView.as_view(), name="profile"),
    path('accounts/profile/edit/', EditProfileView.as_view(), name="edit_profile"),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) +\
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
