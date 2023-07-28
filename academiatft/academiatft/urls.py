from django.contrib import admin
from django.urls import path, re_path, include
from .views import inicio
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('admin', admin.site.urls),
    re_path(r'^$', inicio),
    re_path(r'^unidades/', include('unidades.urls')),
    re_path(r'^items/', include('items.urls')),
]

