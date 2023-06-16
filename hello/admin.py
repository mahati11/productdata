from django.contrib import admin
from hello.models import Product
from hello.models import Variants
from hello.models import Image
from hello.models import Options

# Register your models here.
admin.site.register(Product)
admin.site.register(Variants)
admin.site.register(Image)
admin.site.register(Options)

