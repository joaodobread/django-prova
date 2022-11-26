from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.static import serve


print(settings.STATIC_URL, settings.STATIC_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('locations/', include('locations.urls')),
]


print(urlpatterns)
