
from django.contrib import admin

# Register your models here.


from .models import Product, Variation, ProductImage, Category,ProductFeatured,PartnerImage

admin.site.register(Product)

admin.site.register(Variation)

admin.site.register(ProductImage)

admin.site.register(Category)

admin.site.register(ProductFeatured)

admin.site.register(PartnerImage)