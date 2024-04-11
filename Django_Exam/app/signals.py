from django.dispatch import receiver
from django.db.models.signals import pre_delete
from .models import Todo

@receiver(pre_delete, sender=Todo)
def delete_todo(sender, instance, **kwargs):
    instance.image.delete(False)
    
    
pre_delete.connect(delete_todo, sender=Todo)
    
    
    