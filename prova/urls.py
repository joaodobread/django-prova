from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('locations/', include('locations.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('dashboard/clients/', include('clients.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
