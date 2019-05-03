from __future__ import unicode_literals
from __future__ import absolute_import

from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _




class PermaLink(models.Model):
    """
    Provide a PermaLink as default to provide a slug to model self and a get_absolute_url.
    e.g:
        @class SomeModel(PermaLink):
            @fields
    """
    slug = models.SlugField(_("slug"), blank=True, null=True)

    class Meta:
        abstract = True

    def get_url_kwargs(self, **kwargs):
        kwargs.update(getattr(self, 'url_kwargs', {}))
        return kwargs

    def get_absolute_url(self):
        _url = self.get_url_kwargs(slug=self.slug)
        return (self.url_name, (), _url)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self._slug)
        super(PermaLink, self).save(*args, **kwargs)


class TimeStamp(models.Model):
    """
    Provide a TimeStamp as default set a created and updated date/time to model self.
    e.g:
        @class SomeModel(TimeStamp):
            @fields
    """
    created = models.DateTimeField(_("criado em"), auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(_("modificado em"), auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True
