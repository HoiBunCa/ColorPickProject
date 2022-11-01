from django.db import models

# Create your models here.


class ImageModel(models.Model):
    name = models.TextField(max_length=100)
    image = models.FileField(upload_to='images/')
    user = models.TextField(max_length=100)

    @classmethod
    def create(self, name, image, user):
        return ImageModel.objects.create(name=name, image=image, user=user )

    def __str__(self):
        return self.name