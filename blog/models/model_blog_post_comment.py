from django.db import models
from django.utils.translation import gettext_lazy as _

from blog.models.model_blog_post import Post
from forms.models.model_base_comment_abstract import BaseComment
from utils.general.models.model_status_abstract import Status
from utils.general.models.model_language_status_abstract import LanguageStatus


class PostComment(BaseComment, Status, LanguageStatus):
    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='post_comments', verbose_name=_('reply'),
                              blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments',
                             verbose_name=_('comment'))

    def __str__(self):
        return self.name
