from django.db import models

# Create your models here.
from django.utils.text import slugify

class category(models.Model):
    cname=models.CharField(max_length=100)

    @property
    def get_categories(self):
        return subcategory.objects.filter(cname__cname=self.cname)


    def __str__(self):
        return self.cname


class subcategory(models.Model):
    cname=models.ForeignKey(category,on_delete=models.CASCADE)
    subcname=models.CharField(max_length=100)
    data=models.CharField(max_length=100,null=True)
    slug=models.SlugField(max_length=40,null=True)

    def save(self, *args, **kwargs): 
        self.slug = slugify(self.subcname) 
        super(subcategory, self).save(*args, **kwargs) 


    def __str__(self):
        return self.subcname


