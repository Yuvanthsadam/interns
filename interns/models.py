from django.db import models
from django.core.validators import FileExtensionValidator

def upload_directory_path(instance, filename):
    return 'UPLOADS/{0}/{1}'.format(instance.name, filename)

class employee(models.Model):
    name = models.CharField(max_length=50)
    mobile =models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    profile_image = models.FileField(
        upload_to=upload_directory_path, blank=True, null=True, max_length=255, validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg'])])

    def __str__(self):
        return self.name