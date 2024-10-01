from django.contrib import admin
from .models import cleaner,booking,subscriber,contact, orders
# Register your models here.
admin.site.register(cleaner)
admin.site.register(booking)
admin.site.register(subscriber)
admin.site.register(contact)
admin.site.register(orders)