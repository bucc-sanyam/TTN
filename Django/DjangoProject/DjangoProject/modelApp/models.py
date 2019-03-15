from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    reporting_manager = models.ForeignKey('self', null=False, on_delete=models.CASCADE, default=4)

    designation_choices = [
        ('CEO', 'CEO'),
        ('Senior Software Engineer', 'Senior Software Engineer'),
        ('Project Manager', 'Project Manager'),
        ('Trainee', 'Trainee'),
    ]

    designation = models.CharField(max_length=50, choices=designation_choices)
