from django.conf.urls import url
from .views import login_view, logout_view, register

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', login_view, name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^logout/$', logout_view, name='logout')
]