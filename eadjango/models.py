from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Post(models.Model):

    # Fields
    title = CharField(max_length=200)
    text = TextField()
    created_date = DateTimeField(default=timezone.now)

    # Relationship Fields
    author = ForeignKey(
        on_delete=models.CASCADE, on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('app_name_post_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('app_name_post_update', args=(self.pk,))