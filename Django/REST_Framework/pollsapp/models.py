from django.db import models

# Create your models here.
class Questions(models.Model):
    text = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User', related_name='Questions', on_delete=models.CASCADE, editable = False, null = True)

    def __str__(self):
        return self.text

class Choices(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text