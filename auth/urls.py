from django.conf.urls import url
# from rest_framework.authtoken import views as authTokenView
from rest_framework_jwt.views import obtain_jwt_token

from . import views
app_name = 'auth'
urlpatterns = [
    # get authentication token for the user
    url(r'^api-token-auth/', obtain_jwt_token),
    # ex: /auth/check
    url(r'check/$', views.authCheck, name='index'),
]