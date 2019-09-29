from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import FavoriteThings, AuditLog


@receiver(post_save, sender=FavoriteThings)
def audit_log_favorite_created(sender, instance, created, **kwargs):
    action = 'created' if created else 'updated'
    AuditLog.objects.create(title=instance.title, action=action)


@receiver(post_delete, sender=FavoriteThings)
def audit_log_favorite_deleted(sender, instance, **kwargs):
    AuditLog.objects.create(title=instance.title, action="deleted")
