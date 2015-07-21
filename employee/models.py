from django.db import models


class Employee(models.Model):
    emp_name = models.CharField(max_length=80)
    emp_code = models.CharField(max_length=30)
    salary = models.IntegerField(default=0)

    def __self__(self):
        return self.emp_name

