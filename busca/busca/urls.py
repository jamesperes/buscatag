"""busca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from buscatag.views import tags_ratings, tags_list, pessoa, dev_list, pro_list
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^$',RedirectView.as_view(url='/tags') ),
    url(r'^admin/', admin.site.urls),
    url(r'^tag/(?P<tag_id>[0-9]+)', tags_ratings),
    url(r'^tags/', tags_list),
    url(r'^devs/', dev_list),
    url(r'^pro/', pro_list),
    url(r'^pessoa/(?P<pessoa_id>[0-9]+)', pessoa),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
