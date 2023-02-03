from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.general.models.model_seo_abstract import Seo
from utils.general.models.model_date_abstract import DateBasic
from utils.general.models.model_basic_post_abstract import BasicPost
from utils.general.models.model_basic_gallery_abstract import BasicGallery

from portfolio.models.model_portfolio import Portfolio


# from utils.general.models.model_status_abstraction import Status   TODO: uncomment

class PortfolioGallery(BasicGallery, DateBasic):
    class Meta:
        verbose_name = _('Portfolio')
        verbose_name_plural = _('Portfolios')

    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='portfolio_gallery')

    def __str__(self):
        return self.portfolio.title
