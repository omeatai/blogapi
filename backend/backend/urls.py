from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet

app_name = 'backend'

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
# router.register('articles', ArticleDetailsViewSet, basename='articles')
urlpatterns = router.urls

# urlpatterns = [
#     path('', include(router.urls))
# ]