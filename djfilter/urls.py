from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from core import views
# from socialcustom.views import SomeTableView


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^show$', views.show),
    url(r'^Alert$', views.Alert),
    url(r'^logout_view$', views.logout_view),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
