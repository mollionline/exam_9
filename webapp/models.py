from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Photo(models.Model):
    photo = models.ImageField(upload_to='photo', verbose_name='Фотография', null=False, blank=False)
    sign = models.CharField(max_length=20, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    author = models.ForeignKey(get_user_model(), verbose_name='Автор', related_name='photos', on_delete=models.CASCADE)

    def __str__(self):
        return '{}. {}'.format(self.pk, self.photo)

    class Meta:
        ordering = ['-created_at', ]


class ChoosePhoto(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                               related_name='photo', verbose_name='Автор')
    photo = models.ForeignKey(Photo,
                              on_delete=models.CASCADE,
                              related_name='authors')
