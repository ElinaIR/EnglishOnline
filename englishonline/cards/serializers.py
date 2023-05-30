from django.utils.text import slugify
from rest_framework import serializers

from cards.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'last_name', 'first_name', 'username',)


class CardsUserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = CardsUserProfile
        fields = ('id', 'user', 'role', 'decks',)
        read_only_fields = ('role',)

    def update(self, instance, validated_data):
        if 'decks' in validated_data:
            decks = validated_data.pop('decks')
            deck = decks[0]
            if deck not in instance.decks.all():
                DeckPopularity.objects.create(user=instance.user, deck=deck)
                cards = OriginalCard.objects.filter(deck=deck)
                for card in cards:
                    Card.objects.create(user=instance.user, original_card=card)
            instance.decks.add(deck)
            instance.save()
        return instance


class DeckSerializer(serializers.ModelSerializer):
    creator = UserSerializer(default=serializers.CurrentUserDefault())

    class Meta:
        model = Deck
        fields = '__all__'
        read_only_fields = ('slug',)
        lookup_field = 'slug'

    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs['slug'] = slugify(attrs['title'], allow_unicode=True)
        return attrs

    def create(self, validated_data):
        return Deck.objects.create(**validated_data)


class OriginalCardSerializer(serializers.ModelSerializer):
    deck = DeckSerializer(read_only=True)
    deck_id = serializers.PrimaryKeyRelatedField(queryset=Deck.objects.all(), source='deck',
                                                 write_only=True)

    class Meta:
        model = OriginalCard
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    original_card = OriginalCardSerializer(read_only=True)
    or_card_id = serializers.PrimaryKeyRelatedField(queryset=OriginalCard.objects.all(), source='original_card',
                                                    write_only=True)

    class Meta:
        model = Card
        fields = '__all__'


class DeckPopularitySerializer(serializers.ModelSerializer):
    user = UserSerializer(default=serializers.CurrentUserDefault())
    deck = DeckSerializer(read_only=True)

    class Meta:
        model = DeckPopularity
        fields = '__all__'


class MarkSerializer(serializers.ModelSerializer):
    card = OriginalCardSerializer(read_only=True)
    card_id = serializers.PrimaryKeyRelatedField(queryset=OriginalCard.objects.all(), source='card',
                                                    write_only=True)

    class Meta:
        model = Mark
        fields = '__all__'


class AttemptSerializer(serializers.ModelSerializer):
    user = UserSerializer(default=serializers.CurrentUserDefault())

    class Meta:
        model = Attempt
        fields = '__all__'
