from django.db import models

# Create your models here.

class Faculty(models.Model):
    name = models.CharField(max_length=300)
    hod = models.CharField(max_length=300)
    description = models.TextField()
    
    def __unicode__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=300)
    dean = models.CharField(max_length=300)
    description = models.TextField()
    
    def __unicode__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=300)
    matric_no = models.TextField()
    faculty_id = models.ForeignKey(Faculty)
    department_id = models.ForeignKey(Department)
    
    def __unicode__(self):
        return self.name
