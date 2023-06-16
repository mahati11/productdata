# from django.contrib import admin
# from django.urls import path,include
# from hello import views
# urlpatterns = [
#     path('',views.get_products,name="index"),
# ]
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)
router.register(r'variant', views.VariantViewSet)
router.register(r'image', views.ImageViewSet)
router.register(r'option', views.OptionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]