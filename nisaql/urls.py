from django.conf.urls import url

from . import views
from graphene_django.views import GraphQLView
from .schema import schema

urlpatterns = [
    url(r'^$', GraphQLView.as_view(graphiql=True, schema=schema)),
]