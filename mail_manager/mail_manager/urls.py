from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('newsletter.urls', namespace='newsletter')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts'))
]
