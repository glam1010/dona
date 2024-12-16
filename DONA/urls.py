from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.auth import views as auth_views
from users import views

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('donate/', views.donate, name='donate'),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('users/', include('users.urls')),
    path('accounts/', include('accounts.urls')),

]

# Serve static files during development (only if DEBUG is True)
if settings.DEBUG:
    # This will serve the static files from the STATICFILES_DIRS during development
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
