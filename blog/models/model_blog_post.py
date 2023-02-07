from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.translation import gettext_lazy as _

from utils.general.models.model_date_abstract import DateBasic
from utils.general.models.model_seo_abstract import Seo
from utils.general.models.model_basic_post_abstract import BasicPost
from utils.general.models.model_status_abstract import Status
from utils.general.models.model_language_status_abstract import LanguageStatus

from blog.models.model_blog_post_category import PostCategory
from utils.unique_slug_generator import unique_slug_generator


class Post(Seo, BasicPost, DateBasic, Status, LanguageStatus):
    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
    short_description = models.CharField(_("Short Discription"), max_length=50, null=True)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, related_name='posts',
                                 verbose_name=_('category'))

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Post)
def pre_post_category_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    if not instance.thumbnail_alt:
        instance.thumbnail_alt = unique_slug_generator(instance)
