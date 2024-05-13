from django.db import models

class Products(models.Model):  #Movie table definition
    model_name=models.CharField(max_length=30)
    company=models.CharField(max_length=30)
    desc=models.TextField()
    year=models.IntegerField()
    image=models.ImageField(upload_to='movies',null=True,blank=True)
    price=models.IntegerField()
    def __str__(self):
        return self.model_name
