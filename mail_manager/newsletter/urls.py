from django.conf.urls import url

from .views import (
    add_subscriber,
    is_newsletter_exists,
    create_newsletter,
    edit_newsletter,
    get_newsletters,
    index
)

app_name = 'newsletter'

urlpatterns = [
    url(
        r'^$',
        index,
        name='index'
    ),
    url(
        r'^get_newsletters/$',
        get_newsletters,
        name='get'
    ),
    url(
        r'^create/$',
        create_newsletter,
        name='create'
    ),
    url(
        r'^edit/$',
        edit_newsletter,
        name='edit'
    ),
    url(
        r'^check_newsletter/(?P<newsletter_id>\d+)/$',
        is_newsletter_exists,
        name='check'
    ),
    url(
        r'^add_subscriber/$',
        add_subscriber,
        name='add_subscriber'
    )
]
