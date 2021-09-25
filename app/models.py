from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator ,MinValueValidator


# Create your models here.

STATE_CHOICES= (

      ('Arunachal Pradesh ','Arunachal Pradesh'),
      ('Andhra Pradesh','Andhra Pradesh'),
      ('Assam','Assam'),
      ('Bihar','Bihar'),
      ('Chhattisgarh','Chhattisgarh'),
      ('Goa','Goa'),
      ('Gujarat','Gujarat'),
      ('Haryana','Haryana	'),
      ('Himachal Pradesh','Himachal Pradesh'),
      ('Jharkhand','Jharkhand'),
      ('Karnataka','Karnataka'),
      ('Kerala','Kerala'),
      ('Madhya Pradesh','Madhya Pradesh'),
      ('Maharashtra','Maharashtra'),
      ('Manipur','Manipur'),
      ('Meghalaya','Meghalaya'),
      ('Mizoram','Mizoram'),
      ('Nagaland','Nagaland'),
      ('Odisha','Odisha'),
      ('Punjab','Punjab'),
      ('Rajasthan','Rajasthan'),
      ('Sikkim','Sikkim	'),
      ('Tamil Nadu','Tamil Nadu'),
      ('Telangana','Telangana'),
      ('Tripura',	'Tripura'),
      ('Uttar Pradesh',	'Uttar Pradesh'),
      ('Uttarakhand',	'Uttarakhand'),
      ('West Bengal',	'West Bengal'),
      ('Andaman and Nicobar Island',	'Andaman and Nicobar Island'),
      ('Chandigarh',	'Chandigarh'),
      ('Dadra and Nagar Haveli and Daman and Diu',	'Dadra and Nagar Haveli and Daman and Diu'),
      ('Delhi',	'Delhi'),
      ('Ladakh	','Ladakh	'),
      ('Lakshadweep','Lakshadweep'),
      ('Jammu and Kashmir','Jammu and Kashmir'),
      ('Puducherry','Puducherry'),

)

class Customer(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField( max_length=50)
    locality=models.CharField( max_length=50)
    city=models.CharField( max_length=50)
    zipcode=models.IntegerField()
    ph=models.IntegerField()
    state= models.CharField(choices=STATE_CHOICES, max_length=50)
    



    def _str_(self) :
      return str(self.id)

CATEGORY_CHOICES=(
    ('M','MOBILE'),
    ('L','LEPTOP'),
    ('TW','TOP WEAR'),
    ('BW','BOTTOM WEAR'),

)
class Product(models.Model):
    title=models.CharField(max_length=200)
    selling_price=models.FloatField()
    description=models.TextField()
    category=models.CharField(choices=CATEGORY_CHOICES , max_length=50,default='')
    brand=models.CharField(max_length=200)
    Product_image=models.ImageField(upload_to='Producti')

    def _str_(self) :
     return str(self.id)

class Cart(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   product=models.ForeignKey(Product,on_delete=models.CASCADE)
   quantity=models.PositiveIntegerField(default=1)

   def _str_(self) :
    return str(self.id)
    @property()
    def total_cost(self):
       return self.quantity * self.product.selling_price


STATUS_CHOICES=(

    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way', 'On the way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)
class OrderPlaced(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
   product=models.ForeignKey(Product,on_delete=models.CASCADE)
   quantity=models.PositiveIntegerField(default=1)
   ordered_date=models.DateTimeField( auto_now_add=True)
   status=models.CharField(choices=STATUS_CHOICES,max_length=50,default='Pending')
    
       
   