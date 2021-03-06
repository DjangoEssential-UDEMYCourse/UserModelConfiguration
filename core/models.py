from django.db import models

from django.contrib.auth import get_user_model
# from django.conf import settings


class Post(models.Model):
    # autor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Autor', on_delete=models.CASCADE)
    autor = models.ForeignKey(get_user_model(), verbose_name='Autor', on_delete=models.CASCADE)
    titulo = models.CharField('Titulo', max_length=100)
    texto = models.TextField('Texto', max_length=500)

    def __str__(self):
        return self.titulo
