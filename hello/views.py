from django.shortcuts import render,redirect
import shopify
from django.conf import settings
from django.http import HttpResponse
from .models import Product
from .models import Variants
from decimal import Decimal
from .models import Options
from .models import Image
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import ProductSerializer,VariantSerializer,ImageSerializer,OptionSerializer
# Create your views here.

def get_products(request):
    
    shop_url = 'https://{0}'.format(settings.SHOPIFY_STORE_DOMAIN)
    session = shopify.Session(shop_url, settings.SHOPIFY_API_VERSION)
    session.token = settings.SHOPIFY_API_ACCESS_TOKEN
    shopify.ShopifyResource.activate_session(session)
   
    products = shopify.Product.find()
    products_data = []
    for product in products:
        # Print product data
        print("Product Fields:")
        for attribute, value in product.to_dict().items():
            print(f"{attribute}: {value}")
        
        print("--------------------")
        product_data = product.to_dict()
        products_data.append(product_data)
    for product in products:
        # Create a new Product instance and save it to the database
        new_product = Product(title=product.title, id=product.id,body_html=product.body_html,price=product.variants[0].price,
        vendor=product.vendor,created_at=product.created_at,handle=product.handle,
        updated_at=product.updated_at,published_at=product.published_at,template_suffix=product.template_suffix,
        status=product.status, published_scope=product.published_scope,tags=product.tags,admin_graphql_api_id=product.admin_graphql_api_id)
        new_product.save()
        for var in product.variants:
            new_var=Variants(price=var.price,title=var.title,id=var.id)
            new_var.save()
        for img in product.images:
            new_img=Image(created_at=img.created_at,id=img.id,
            updated_at=img.updated_at,position=img.position)
            new_img.save()
        for op in product.options:
            new=Options(name=op.name,id=op.id,
            position=op.position)
            new.save()
     
    return JsonResponse(products_data, safe=False)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
class VariantViewSet(viewsets.ModelViewSet):
    queryset = Variants.objects.all().order_by('id')
    serializer_class = VariantSerializer
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all().order_by('id')
    serializer_class = ImageSerializer
class OptionViewSet(viewsets.ModelViewSet):
    queryset = Options.objects.all().order_by('id')
    serializer_class = OptionSerializer
