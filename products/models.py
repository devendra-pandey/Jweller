from django.db import models
from django.db.models import Max

TYPE_MARRIED = (
        ('0', 'Married'),
        ('1', 'Single'),
    )


class Products(models.Model):
    image = models.FileField(upload_to='static/Uploads/product/', null= True , blank=True)
    gold_weight = models.CharField(max_length=30)
    diamond_carat = models.CharField(max_length=30)
    design_number = models.CharField(max_length=30,default=0, unique=True)
    status = models.BooleanField(default="1")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.design_number

    def calculate_design_number(self):
        res = Products.objects.filter().aggregate(max_id=Max('pk'))
        abc  = res.get('max_id')
        if abc is None :
            abc = 0
            number = abc + 1
            self.design_number = number
            return self.design_number
        else:    
            number = abc + 1

            self.design_number = number
            return self.design_number
        

    def save(self,*args,**kwargs):
        self.design_number = str(self.calculate_design_number())
        super().save(*args, **kwargs)     
    
    class Meta:
      get_latest_by = 'created'
