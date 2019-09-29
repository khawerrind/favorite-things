from rest_framework import serializers
import datetime
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError as JSONSchemaValidationError
from .models import Categories, FavoriteThings, AuditLog

from .jsonschema import (
    metadata_schema,
)


def is_valid_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False


class JSONSchemaField(serializers.JSONField):
    """
    Custom field that validates incoming data against JSONSchema,
    Then, if successful, will store it as a string.
    """

    def __init__(self, schema, *args, **kwargs):
        super(JSONSchemaField, self).__init__(*args, **kwargs)
        self.schema = schema

    def to_representation(self, obj):
        return json.loads(str(obj))

    def to_internal_value(self, data):
        try:
            validate(data, self.schema)
        except JSONSchemaValidationError as e:
            raise serializers.ValidationError(e.message)

        return super(JSONSchemaField, self).to_internal_value(json.dumps(data))


class CategoriesSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Categories
        fields = '__all__'
        read_only_fields = ('date_created', 'date_modified')


class FavoriteThingsSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source='category.name',
        required=False
    )
    metadata = JSONSchemaField(metadata_schema, required=False)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = FavoriteThings
        fields = '__all__'
        read_only_fields = ('date_created', 'date_modified')

    def increment_ranks(self, rank, category):
        if FavoriteThings.objects.filter(
            category_id=category.id,
            rank=rank
        ).exists():
            for obj in FavoriteThings.objects.filter(
                category_id=category.id,
                rank__gte=rank
            ).order_by('-rank'):
                obj.rank += 1
                obj.save()

    def create(self, validated_data):
        """Save the post data when creating a new FavoriteThings."""
        self.increment_ranks(
            validated_data['rank'],
            validated_data['category']
        )
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if instance.rank != validated_data['rank']:
            self.increment_ranks(
                validated_data['rank'],
                validated_data['category']
            )
        return super().update(instance, validated_data)


class AuditLogSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = AuditLog
        fields = '__all__'
        read_only_fields = ('date_created',)
