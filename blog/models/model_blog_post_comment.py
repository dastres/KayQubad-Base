from django.db import models
from django.contrib.auth import get_user_model
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
    likes = models.ManyToManyField(get_user_model(), verbose_name=_('Likes'), related_name='like_comments')
    dislike = models.ManyToManyField(get_user_model(), verbose_name=_('Dislikes'), related_name='dislike_comments')

    def __str__(self):
        return self.name

    def get_like(self):
        return self.likes.count()

    def get_dislike(self):
        return self.dislike.count()
