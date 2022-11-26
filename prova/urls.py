from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('locations/', include('locations.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('dashboard/clients/', include('clients.urls'))
]
