import os

from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver

from Main.models import DataSetFile, Dataset  # isort: skip


@receiver(post_save, sender=Dataset)
def create_dataset(sender, created, instance, **kwargs):
    if created:
        Dataset.objects.filter(id=instance.id).update(PassengerId=instance.id)


@receiver(post_delete, sender=DataSetFile)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.File:
        if os.path.isfile(instance.File.path):
            os.remove(instance.File.path)


@receiver(pre_save, sender=DataSetFile)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = DataSetFile.objects.get(pk=instance.pk).File
    except DataSetFile.DoesNotExist:
        return False

    new_file = instance.File
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
