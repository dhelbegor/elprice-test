from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.services.behaviours import PermaLink, TimeStamp




class Departament(TimeStamp):
    name = models.CharField(_("nome"), max_length=255)

    class Meta:
        verbose_name = _('Departamento')
        verbose_name_plural = _('Departamentos')

    def __str__(self):
        return self.name


class Category(TimeStamp):
    name = models.CharField(_("nome"), max_length=255)

    class Meta:
        verbose_name = _('Categoria')
        verbose_name_plural = _('Categorias')

    def __str__(self):
        return self.name


class Product(PermaLink, TimeStamp):

    description = models.CharField(_("descrição"), max_length=255)
    departament = models.ForeignKey(Departament, verbose_name=_('departamento'), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=_('categoria'), on_delete=models.CASCADE)
    price = models.IntegerField(_('preço'))
    is_active = models.BooleanField(default=True, verbose_name=_('ativo?'))
    

    class Meta:
        ordering = ['-created']
        verbose_name = _('Produto')
        verbose_name_plural = _('Produtos')

    def __str__(self):
        return "{} {}".format(self.description, self.departament)

    @property
    def _slug(self):
        """
        This method is used to provide an
        auto gen slug field by PermaLink save method.
        """
        return "{}".format(self.description)