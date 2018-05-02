from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('favicon.ico', RedirectView.as_view(
            url=staticfiles_storage.url('icons/favicon.ico'), permanent=False), name="favicon"),

    # path('/', include('dmlgeo.urls', namespace='dmlgeo')),
    path('geo/', include('dmlgeo.urls', namespace='dmlgeo')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



