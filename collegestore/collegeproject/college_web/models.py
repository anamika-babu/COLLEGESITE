from django.db import models

# Create your models here.
class Detail(models.Model):
    name=models.CharField(max_length=250)
    DOB=models.DateField()
    Age=models.IntegerField()
    Gender=models.ForeignKey("Gender",on_delete=models.CASCADE)
    PhoneNo=models.CharField(max_length=200)
    Email=models.EmailField(unique=True)
    Address=models.TextField()
    Department=models.ForeignKey("Department",on_delete=models.CASCADE)
    Course=models.ForeignKey("Course",on_delete=models.CASCADE)
    Purpose=models.ForeignKey("Purpose",on_delete=models.CASCADE)
    DebitNoteBook = models.BooleanField("DebitNoteBook",default=False)
    Pen = models.BooleanField("Pen",default=False)
    ExamPaper = models.BooleanField("Exampaper",default=False)

    def __str__(self):
        return self.name
class Gender(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Department(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    name=models.CharField(max_length=300)
    department=models.ForeignKey("Department",on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Purpose(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
