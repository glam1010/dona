from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views  # Import the views file to reference the `login_view` and `register_view` functions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),  # Route for login
    path('register/', views.register_view, name='register'),  # Route for register
    path('', TemplateView.as_view(template_name='index.html'), name='home'),  # Route for homepage
    path('donate/', views.donate_view, name='donate'),

]

# Serve static files during development (only if DEBUG is True)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
