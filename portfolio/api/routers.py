from rest_framework import routers
from portfolio.api.viewset.viewset_portfolio import PortfolioViewSet
from portfolio.api.viewset.viewset_portfolio_category import PortfolioCategoryViewSet

router = routers.DefaultRouter()
router.register('portfolio/category', PortfolioCategoryViewSet, basename='portfolio_category')
router.register('portfolio', PortfolioViewSet, basename='portfolio')

urlpatterns = router.urls
