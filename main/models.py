from django.db import models
from django.utils.translation import gettext_lazy as _
from work.minixs import TranslateMixin
import os
from datetime import datetime
import random
from django.contrib.auth.models import User


def upload_to(name):
    def handle(instance, filename):
        ext = os.path.splitext(filename)[1]

        return "{}/{:%Y}/{:%m}/{:%Y-%m-%d-%H-%M-%S}-{}{}".format(
            name,
            datetime.now(),
            datetime.now(),
            datetime.now(),
            random.randint(10000, 99999),
            ext
        )

    return handle


def posts_upload_to(instance, filename):
    return upload_to("posts")(instance, filename)


def carousel_upload_to(instamce, filename):
    return upload_to("carousel")(instamce, filename)


class Carousel(models.Model):
    STATUS_ACTIVE = 1
    STATUS_INACTIVE = 0

    image = models.ImageField(upload_to=carousel_upload_to)
    header = models.CharField(max_length=50, null=True, default=None, blank=True)
    comment = models.CharField(max_length=200, null=True, default=None, blank=True)
    status = models.SmallIntegerField(default=STATUS_ACTIVE, choices=(
        (STATUS_ACTIVE, "Faol"),
        (STATUS_INACTIVE, "Nofaol")
    ))
    order = models.SmallIntegerField(default=0)

    class Meta:
        verbose_name = 'Slideshow'
        verbose_name_plural = 'Slideshows'


class Category(TranslateMixin, models.Model):
    translate_attributes = ['name']

    name_uz = models.CharField(max_length=50, verbose_name="Nomi (uz)")
    name_ru = models.CharField(max_length=50, verbose_name="Nomi (ru)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'

class Post(TranslateMixin, models.Model):
    translate_attributes = ['subject', 'content']

    user = models.ForeignKey(User, on_delete=models.RESTRICT, default=None, null=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, default=None, null=True)
    subject_uz = models.CharField(max_length=100, verbose_name=_("Sarlavha (uz)"))
    subject_ru = models.CharField(max_length=100, verbose_name=_("Sarlavha (ru)"))
    content_uz = models.TextField(verbose_name=_("Izoh (uz)"))
    content_ru = models.TextField(verbose_name=_("Izoh (ru)"))
    image = models.ImageField(verbose_name=_("Rasm"), upload_to=posts_upload_to)
    read = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        # django model delete old file for on update
        ret = super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

        return ret

    @property
    def is_tag_new(self):
        return (datetime.now() - self.added_at).total_seconds() < 600


class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    post = models.ForeignKey(Post, on_delete=models.RESTRICT)
    liked_at = models.DateTimeField(auto_now_add=True)