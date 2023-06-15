from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from cards.models import *
from cards.serializers import *


class CardsUserProfileViewSet(viewsets.ModelViewSet):
    queryset = CardsUserProfile.objects.all()
    serializer_class = CardsUserProfileSerializer

    @action(methods=['get'], detail=True)
    def cards(self, request, pk):
        cards = Card.objects.filter(user=pk)
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)


class OriginalCardViewSet(viewsets.ModelViewSet):
    queryset = OriginalCard.objects.all()
    serializer_class = OriginalCardSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    lookup_field = 'slug'

    @action(methods=['get'], detail=True)
    def cards(self, request, slug):
        cards = OriginalCard.objects.filter(deck__slug=slug)
        serializer = OriginalCardSerializer(cards, many=True)
        return Response(serializer.data)


class DeckPopularityViewSet(viewsets.ModelViewSet):
    queryset = DeckPopularity.objects.all()
    serializer_class = DeckPopularitySerializer


class AttemptViewSet(viewsets.ModelViewSet):
    queryset = Attempt.objects.all()
    serializer_class = AttemptSerializer

    @action(methods=['get'], detail=True)
    def marks(self, request, pk):
        marks = Mark.objects.filter(attempt=pk)
        serializer = MarkSerializer(marks, many=True)
        return Response(serializer.data)


class MarkViewSet(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
