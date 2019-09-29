from rest_framework import generics
from .serializers import (
    CategoriesSerializer,
    FavoriteThingsSerializer,
    AuditLogSerializer
)
from .models import (
    Categories,
    FavoriteThings,
    AuditLog
)


class CategoriesListCreateAPIView(generics.ListCreateAPIView):
    """This class defines the create and list behavior of our rest api."""
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class FavoriteThingsListCreateAPIView(generics.ListCreateAPIView):
    """This class defines the create and list behavior of our rest api."""
    queryset = FavoriteThings.objects.all()
    serializer_class = FavoriteThingsSerializer


class FavoriteThingsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView): # noqa
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = FavoriteThings.objects.all()
    serializer_class = FavoriteThingsSerializer


class AuditLogListAPIView(generics.ListAPIView):
    """This class handles the http GET requests."""

    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
