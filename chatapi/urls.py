
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user_control.urls')),
    path('message/', include('message_control.urls')),
] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
