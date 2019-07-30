from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class User(AbstractUser):

    def __str__(self):
        return self.username


def upload_to(instance, filename):
    return 'profile_images/{0}/{1}'.format(instance.user.pk, filename)


class Profile(models.Model):
    CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    default_profile_image = 'profile.jpg'
    gender = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    age = models.PositiveSmallIntegerField(default=15)
    avatar = models.ImageField(
        default=default_profile_image,
        upload_to=upload_to,
        null=True,
        blank=True,
    )
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    phone_number = models.CharField(max_length=50, verbose_name="Номер телефона")
    email = models.EmailField()
    address = models.TextField(max_length=500, verbose_name="Ваш адрес")

    def get_absolute_url(self):
        return reverse('cabinet', kwargs={'pk': self.pk})

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


