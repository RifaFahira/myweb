from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^about/', views.about),
    url(r'^contact/', views.contact),
    url(r'^blog/', views.blog),
]
