from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    id = models.IntegerField(primary_key=True,default=0) 
    body_html=models.CharField(max_length=100,default='',null=True)
    vendor=models.CharField( max_length=100,default='',null=True)
    created_at=models.CharField(max_length=100,default='',null=True)
    handle=models.CharField( max_length=100,default='',null=True)
    updated_at=models.CharField(max_length=100,default='',null=True)
    published_at=models.CharField( max_length=100,default='',null=True)
    template_suffix=models.CharField( max_length=100,default='',null=True)
    status=models.CharField( max_length=100,default='',null=True)
    published_scope=models.CharField( max_length=100,default='',null=True)
    tags=models.CharField( max_length=100,default='',null=True)
    admin_graphql_api_id=models.CharField( max_length=255,default='',null=True)
    
    def __str__(self):
        return self.title


class Variants(models.Model):
#  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants',default=True,null=True)
    id = models.IntegerField(primary_key=True,default=0)
    title = models.CharField(max_length=255,default='',null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    compare_at_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    inventory_management = models.CharField(max_length=255,default='',null=True)
    option1 = models.CharField(max_length=255,blank=True, null=True)
    option2 = models.CharField(max_length=255, blank=True, null=True)
    option3 = models.CharField(max_length=255, blank=True, null=True)
    
    inventory_item_id = models.PositiveIntegerField(default=0,null=True)
    inventory_quantity = models.PositiveIntegerField(default=0,null=True)
    old_inventory_quantity = models.PositiveIntegerField(default=0,null=True)
    
    admin_graphql_api_id = models.CharField(max_length=255,default='',null=True)

    def __str__(self):
        return self.title

    

class Image(models.Model):
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images',default='',null=True)
    
    id = models.IntegerField(primary_key=True,default=0)
    position =models.CharField( max_length=50,default='',null=True)
    created_at = models.CharField( max_length=50,default='',null=True)
    updated_at = models.CharField( max_length=50,default='',null=True)
    width = models.CharField( max_length=50,default='',null=True)
    height = models.CharField( max_length=50,default='',null=True)
   
    def __str__(self):
        return str(self.id)

class Options(models.Model):
    
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='options',default='',null=True)
    id = models.IntegerField(primary_key=True,default=0)
    name = models.CharField(max_length=255,default='',null=True)
    position = models.CharField(max_length=50,default='',null=True)
    
    def __str__(self):
        return str(self.id)

