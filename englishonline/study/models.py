from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class BaseAudio(models.Model):
    start = models.FileField(upload_to='audio/', default='audio/default_start.mp3')
    start_speaking = models.FileField(upload_to='audio/', default='audio/default_speak.mp3')
    end = models.FileField(upload_to='audio/', default='audio/default_end.mp3')


class Task1(models.Model):
    task = models.TextField()
    audio = models.FileField(upload_to='%Y/%m/%d/audio/text/')
    text = models.TextField()
    prepare_time = models.IntegerField(default=90)
    record_time = models.IntegerField(default=90)


class Task2(models.Model):
    task = models.TextField()
    audio = models.FileField(upload_to='%Y/%m/%d/audio/ad/')
    pic_caption = models.CharField(max_length=50)
    pic = models.ImageField(upload_to='%Y/%m/%d/photos/ad/')
    question1 = models.FileField(upload_to='%Y/%m/%d/audio/ad/')
    question2 = models.FileField(upload_to='%Y/%m/%d/audio/ad/')
    question3 = models.FileField(upload_to='%Y/%m/%d/audio/ad/')
    question4 = models.FileField(upload_to='%Y/%m/%d/audio/ad/')
    prepare_time = models.IntegerField(default=90)
    record_time = models.IntegerField(default=20)


class Task3(models.Model):
    task = models.TextField()
    audio = models.FileField(upload_to='%Y/%m/%d/audio/interview/')
    start_audio = models.FileField(upload_to='%Y/%m/%d/audio/interview/')
    question1 = models.FileField(upload_to='%Y/%m/%d/audio/interview/')
    question2 = models.FileField(upload_to='%Y/%m/%d/audio/interview/')
    question3 = models.FileField(upload_to='%Y/%m/%d/audio/interview/')
    question4 = models.FileField(upload_to='%Y/%m/%d/audio/interview/')
    question5 = models.FileField(upload_to='%Y/%m/%d/audio/interview/')
    question6 = models.FileField(upload_to='%Y/%m/%d/audio/interview/', blank=True)
    end_audio = models.FileField(upload_to='%Y/%m/%d/audio/interview/')
    prepare_time = models.IntegerField(default=20)
    timer = models.IntegerField(default=5)
    record_time = models.IntegerField(default=40)


class Task4(models.Model):
    task = models.TextField()
    audio = models.FileField(upload_to='%Y/%m/%d/audio/pic_desc/')
    pic1 = models.ImageField(upload_to='%Y/%m/%d/photos/pic_desc/')
    pic2 = models.ImageField(upload_to='%Y/%m/%d/photos/pic_desc/')
    pic3 = models.ImageField(upload_to='%Y/%m/%d/photos/pic_desc/', blank=True)
    prepare_time = models.IntegerField(default=150)
    record_time = models.IntegerField(default=180)


class EGEVariant(models.Model):
    name = models.CharField(max_length=50)
    task1 = models.OneToOneField('Task1', on_delete=models.CASCADE, verbose_name='Text Task')
    task2 = models.OneToOneField('Task2', on_delete=models.CASCADE, verbose_name='Ad Task')
    task3 = models.OneToOneField('Task3', on_delete=models.CASCADE, verbose_name='Interview Task')
    task4 = models.OneToOneField('Task4', on_delete=models.CASCADE, verbose_name='Pic Desc Task')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='%Y/%m/%d/pdf/', blank=True)


class EGEPopularity(models.Model):
    variant = models.ForeignKey('EGEVariant', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class OGEVariant(models.Model):
    name = models.CharField(max_length=50)
    task1 = models.OneToOneField('Task1', on_delete=models.CASCADE, verbose_name='Text Task')
    task2 = models.OneToOneField('Task3', on_delete=models.CASCADE, verbose_name='Interview Task')
    task3 = models.OneToOneField('Task4', on_delete=models.CASCADE, verbose_name='Talk Task')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='%Y/%m/%d/pdf/', blank=True)


class OGEPopularity(models.Model):
    variant = models.ForeignKey('OGEVariant', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class VPRVariant(models.Model):
    name = models.CharField(max_length=50)
    task1 = models.OneToOneField('Task1', on_delete=models.CASCADE, verbose_name='Text Task')
    task2 = models.OneToOneField('Task4', on_delete=models.CASCADE, verbose_name='Pic Desc Task')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='%Y/%m/%d/pdf/', blank=True)


class VPRPopularity(models.Model):
    variant = models.ForeignKey('VPRVariant', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    ROLE = (
        (0, 'Student'),
        (1, 'Teacher'),
    )
    role = models.IntegerField(choices=ROLE, default=0)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_userprofile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
