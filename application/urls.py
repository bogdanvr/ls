"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ls.views import Main, servicedetail
from contact.views import ThanksView
from about.views import AboutView
from blog.views import BlogView
from blog.views import BlogDetailView
from about import views
from contact.views import contactView

from django.conf.urls.static import static
from django.conf import settings
from application import settings





urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Main.as_view(), name="main"),
    url(r'^contacts/$', contactView, name="contact"),
    url(r'^about/$', AboutView.as_view(), name="about"),
    url(r'^thanks/$', ThanksView.as_view(), name = 'thanks'),
    url(r'^blog/$', BlogView.as_view(), name="blog"),
    url(r'^servicedetail/(?P<service_id>\d+)/$', servicedetail, name = 'servicedetail'),
    url(r'^(?P<pk>\d+)/$', BlogDetailView.as_view(), name = 'blog_detail'),
     
    
]
