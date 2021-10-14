from django.db import models
from django.utils import timezone

from PIL import Image
from io import BytesIO
from django.core.files import File
from PIL import ImageOps


# Create your models here.

def upload_location(instance, filename):
    filebase, extension = filename.split('.')
    return 'sujets/%s.%s' % (instance.pub_date, extension)


class Sujet(models.Model):
    DICT = (
        ('Mat', 'Maths'),
        ('Phy', 'Physique Chimie'),
        ('SI', "Science de l'ingénieur"),
        ('Ang', 'Anglais'),
        ('Fr', 'Francais'),
    )
    matiere = models.CharField(max_length=3, choices=DICT, default="Mat")
    image = models.ImageField(upload_to=upload_location, null=True)
    pub_date = models.DateTimeField('date', default=timezone.now)

    def __str__(self):
        return str(self.matiere)+" "+str(self.pub_date)

    def save(self, *args, **kwargs):
        im = Image.open(self.image)
        # Convert Image to RGB color mode
        im = im.convert('RGB')
        # auto_rotate image according to EXIF data
        im = ImageOps.exif_transpose(im)
        # save image to BytesIO object
        im_io = BytesIO()
        # save image to BytesIO object
        im.save(im_io, 'JPEG', quality=40)
        # create a django-friendly Files object
        new_image = File(im_io, name=self.image.name)
        # Change to new image
        self.image = new_image
        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        #self.matiere.storage.delete(self.matiere.name)
        self.image.storage.delete(self.image.name)
        super().delete()
