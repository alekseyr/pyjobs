from django.db import models
from django.contrib.auth.models import AbstractUser

from django_extensions.db.models import TimeStampedModel


class User(AbstractUser):
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    phone = models.CharField('номер телефона', max_length=127, blank=True)

    @models.permalink
    def get_absolute_url(self):
        return 'user-detail', (self.pk,)

    def __str__(self):
        name = self.get_full_name()
        if not name:
            name = self.username
        return name


class Advert(TimeStampedModel):
    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'

    title = models.CharField(verbose_name='название вакансии', max_length=127, blank=False,
                             help_text='краткое описание отражающее суть вакансии')
    description = models.TextField(verbose_name='описание вакансии', blank=True)
    author = models.ForeignKey(User, verbose_name='автор вакансии', blank=True)

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'advert-detail', (self.pk,)