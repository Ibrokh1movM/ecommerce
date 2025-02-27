from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from ecommerce.models import *
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin

# Admin panelni sozlash
admin.site.site_header = "Ecommerce Admin"
admin.site.site_title = "Ecommerce Admin Portal"
admin.site.index_title = "Welcome to Ecommerce Researcher Portal"


@admin.register(Product)
class ProductModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name','slug', 'category', 'price')  # 'my_order' olib tashlandi
    search_fields = ('name', 'price')
    list_filter = ('category', 'quantity')
    autocomplete_fields = ['category']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'created_at', 'product_count')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

    def product_count(self, category):
        return category.products.count()

admin.site.register(Image)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(ProductAttribute)
admin.site.register(Comment)
admin.site.register(ShoppingCart)
admin.site.register(Customer)