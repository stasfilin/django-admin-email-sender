from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

