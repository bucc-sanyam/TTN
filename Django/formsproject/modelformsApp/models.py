from django.db import models

class Manager(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    department = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.IntegerField()
    designation = models.CharField(max_length=50, null=False, default="Trainee")
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    reporting_manager = models.ForeignKey(Manager, null=False, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
