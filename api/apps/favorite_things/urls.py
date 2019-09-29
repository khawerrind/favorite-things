from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView
from .views import (
    CategoriesListCreateAPIView,
    FavoriteThingsListCreateAPIView,
    FavoriteThingsRetrieveUpdateDestroyAPIView,
    AuditLogListAPIView,
)

urlpatterns = {
    # index endpoint

    url(
        '^$',
        TemplateView.as_view(template_name="application.html"),
        name="app",
    ),

    # Categories endpoints

    url(
        r'^api/categories/$',
        CategoriesListCreateAPIView.as_view(),
        name="list-create-category"
    ),

    # Favorite endpoints

    url(
        r'^api/favorites/$',
        FavoriteThingsListCreateAPIView.as_view(),
        name="list-create-favorite"
    ),
    url(
        r'^api/favorites/(?P<pk>[0-9]+)/$',
        FavoriteThingsRetrieveUpdateDestroyAPIView.as_view(),
        name="details-favorite"
    ),

    # AuditLog endpoints

    url(
        r'^api/audit/$',
        AuditLogListAPIView.as_view(),
        name="list-audits"
    ),
}

urlpatterns = format_suffix_patterns(urlpatterns)
