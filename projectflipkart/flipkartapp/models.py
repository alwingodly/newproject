from django.db import models


from django.urls import reverse


class cat(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    descr=models.TextField(blank=True)
    image=models.ImageField(upload_to='catgal',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name=('categoty')
        verbose_name_plural=('category')
    def get_url(self):
       return reverse('flipkartapp:prodbycat',args=[self.slug])
    def __str__(self):
        return '{}'.format(self.name)

class prod(models.Model):
    name=models.CharField(max_length=250,unique=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    availability=models.BooleanField(default=True)
    image=models.ImageField(upload_to='progal',blank=True)
    slug=models.SlugField(max_length=250,unique=True)
    descr=models.TextField(blank=True)
    category=models.ForeignKey(cat,on_delete=models.CASCADE)
    stock=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name',)
        verbose_name=('products')
        verbose_name_plural=('products')
    def get_url(self):
       return reverse('flipkartapp:pdetails',args=[self.category.slug,self.slug])
    def __str__(self):
        return '{}'.format(self.name)