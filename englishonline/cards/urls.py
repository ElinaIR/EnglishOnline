from django.urls import path, include
from rest_framework import routers

from cards.views import *


router = routers.DefaultRouter()

router.register(r'profiles', CardsUserProfileViewSet)
router.register(r'or_cards', OriginalCardViewSet)
router.register(r'cards', CardViewSet)
router.register(r'decks', DeckViewSet)
router.register(r'popularity', DeckPopularityViewSet)
router.register(r'attempts', AttemptViewSet)
router.register(r'marks', MarkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
