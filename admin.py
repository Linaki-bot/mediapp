from django.contrib import admin
from medilabbapp.models import Product
from medilabbapp.models import Student
from medilabbapp.models import Model
from medilabbapp.models import Cars
from medilabbapp.models import Contact
# Register your models here.
admin.site.register(Product)
admin.site.register(Student)
admin.site.register(Model)
admin.site.register(Cars)
admin.site.register(Contact)
