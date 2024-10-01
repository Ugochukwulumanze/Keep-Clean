from django.db import models

# Create your models here.
class cleaner(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    phone = models.IntegerField(null = True)
    email_address = models.EmailField()
    permanent_address = models.CharField(max_length = 2000)
    sex = models.CharField(max_length = 6)
    age = models.IntegerField()
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
class subscriber(models.Model):
    first_name =  models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    phone = models.IntegerField(null = True)
    email_address = models.EmailField()
    current_address = models.CharField(max_length = 2000)
    service = models.CharField(max_length = 20)
    sex = models.CharField(max_length = 6)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
class booking(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    phone = models.IntegerField(null = True)
    email_address = models.EmailField()
    date = models.DateField()
    location = models.CharField(max_length = 500)
    service = models.CharField(max_length = 20)
    comments = models.CharField(max_length = 2000)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
class contact(models.Model):
    fill_name = models.CharField(max_length = 200)
    phone = models.IntegerField(null = True)
    email_address = models.CharField(max_length = 200)
    comments = models.TextField(max_length = 2000)
    
    def __str__(self):
        return self.fill_name 
    
    
class orders(models.Model):
    cleaner_id = models.ForeignKey(cleaner, on_delete = models.CASCADE)
    booking_id = models.ForeignKey(booking, on_delete = models.CASCADE)
    subscriber_id = models.ForeignKey(subscriber, on_delete = models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField()
    
    def __str__(self):
        return str(self.cleaner_id) + " "+ str(self.booking_id)
    
          
