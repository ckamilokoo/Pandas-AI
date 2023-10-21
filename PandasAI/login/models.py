from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    NIVEL_CHOICES = (
        (1, 'Usuario Normal'),
        (2, 'Usuario con Subscripción A y B'),
        (3, 'Administrador'),
    )

    nivel = models.PositiveSmallIntegerField(choices=NIVEL_CHOICES, default=1)
    
    
    # Cambia los valores de related_name para evitar conflictos
    groups = models.ManyToManyField(Group, blank=True, related_name='customuser_group_set')
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='customuser_permission_set',
        verbose_name=('user permissions'),
        help_text=('Specific permissions for this user.'),
    )

    def __str__(self):
        return self.username
