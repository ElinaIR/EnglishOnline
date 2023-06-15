from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class OriginalCard(models.Model):
    word = models.CharField(max_length=50)
    front_word = models.CharField(max_length=255, blank=True)
    front_pic = models.FileField(upload_to='cards/pictures/', blank=True)
    back = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    deck = models.ForeignKey('Deck', related_name='cards', on_delete=models.CASCADE)

    def __str__(self):
        return self.word


class Card(models.Model):
    last_wrong = models.DateField(default=date.today())
    next_review = models.DateField(default=date.today())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_card = models.ForeignKey('OriginalCard', on_delete=models.CASCADE)


class Deck(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    desc = models.TextField(null=True)
    creation_date = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class DeckPopularity(models.Model):
    deck = models.ForeignKey('Deck', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Attempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deck = models.ForeignKey('Deck', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)


class Mark(models.Model):
    card = models.ForeignKey('OriginalCard', on_delete=models.CASCADE)
    mark = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    attempt = models.ForeignKey('Attempt', on_delete=models.CASCADE)


class CardsUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    ROLE = (
        (0, 'Student'),
        (1, 'Teacher'),
    )
    role = models.IntegerField(choices=ROLE, default=0)
    decks = models.ManyToManyField('Deck')

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_userprofile(sender, instance, created, **kwargs):
        if created:
            CardsUserProfile.objects.create(user=instance)
