from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^studentmanagement/', include('studentmanagement.urls')),
    url(r'^admin/', admin.site.urls),
]
