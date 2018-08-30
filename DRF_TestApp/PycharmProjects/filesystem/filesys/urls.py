from django.conf.urls import include, url
from filesys.views import PathViewSet

urlpatterns = [
    # Categories API
    url(r'^$', PathViewSet.as_view({'get': 'list'})),
    #url(r'^filesys/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^api-auth/', include('rest_framework.urls'))
]