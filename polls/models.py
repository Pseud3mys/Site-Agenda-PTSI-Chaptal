from django.db import models
from django.utils import timezone

# Create your models here.

def upload_location(instance, filename):
    filebase, extension = filename.split('.')
    return 'sujets/%s.%s' % (instance.titre, extension)


class Sujet(models.Model):
    titre = models.CharField(max_length=255, default=0)
    photo = models.ImageField(upload_to=upload_location, null=True)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.titre