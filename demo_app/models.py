from django.db import models

# Create your models here.
class category(models.Model):
    category_name=models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    product_name=models.CharField(max_length=100)
    product_price=models.FloatField()
    stock=models.IntegerField()
    product_image=models.FileField(upload_to="static/uploads",null=False)
    product_description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(category, on_delete=models.CASCADE,null=True)
    
    def _str_(self):
        return self.product_name
    
    