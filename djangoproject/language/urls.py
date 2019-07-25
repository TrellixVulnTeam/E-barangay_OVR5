from django.urls import path, include
from . import views
from .views import LanguageView,language
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)

urlpatterns = [
    path('',include(router.urls)),
    path('language/',views.language,name='language-programming'),

]
