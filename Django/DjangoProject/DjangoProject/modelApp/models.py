from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    reporting_manager = models.ForeignKey('self', null=False, on_delete=models.CASCADE)

    designation_choices = [
        ('CEO', 'CEO'),
        ('Senior Software Engineer', 'Senior Software Engineer'),
        ('Project Manager', 'Project Manager'),
        ('Trainee', 'Trainee'),
    ]

    designation = models.CharField(max_length=50, choices=designation_choices)


@receiver(post_save, sender=Employee)
def create_user_profile(sender, instance, **kwargs):
        instance.reporting_manager = instance
        instance.save()

