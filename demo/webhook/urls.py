from django.conf.urls import url
from webhook.views import webhook_view
from . import views

urlpatterns = [
    url(r'', webhook_view),
]