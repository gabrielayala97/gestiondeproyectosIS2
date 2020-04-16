from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
#from django.db.models.signals import post_save
#from django.dispatch import receiver
from apps.rol.models import Rol


class Usuario(AbstractUser):
    #usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.OneToOneField(Rol,null=True, blank=True, on_delete=models.CASCADE)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass
""""@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.usuario.save()"""
