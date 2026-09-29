from django.contrib import admin
from . models import Customer 
from . admin_models import Admin,Product_order


admin.site.register(Customer)
admin.site.register(Admin)
admin.site.register(Product_order)
