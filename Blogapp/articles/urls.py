from .views import ArticleViewSet
from django.urls import path,include
#routing
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("articles", ArticleViewSet) #articles is the name of the url
 
urlpatterns = [ 
    path('', include(router.urls)),
]  