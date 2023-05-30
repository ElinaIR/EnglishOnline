from django.contrib import admin

from cards.models import *


@admin.register(Deck)
class Deck(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(OriginalCard)
admin.site.register(Card)
admin.site.register(DeckPopularity)
admin.site.register(Attempt)
admin.site.register(Mark)
admin.site.register(CardsUserProfile)
