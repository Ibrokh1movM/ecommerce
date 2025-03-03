from django.db.models import Count, Avg, Sum, Max, Min, F, ExpressionWrapper, DecimalField
from ecommerce.models import Product, Category
import os
import django
from colorama import Fore, Style, init

init(autoreset=True)

# Django muhitini sozlash
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

# --------- Kategoriyalar bo‘yicha mahsulotlar soni ---------
categories = Category.objects.annotate(product_count=Count('products'))
print(f"\n{Fore.CYAN}{Style.BRIGHT}📦 Mahsulotlar kategoriyalar bo‘yicha:{Style.RESET_ALL}")
for category in categories:
    print(f"{Fore.YELLOW}- {category.title}: {category.product_count} ta mahsulot")

# --------- Mahsulotlar reytingi ---------
products = Product.objects.annotate(avg_rating=Avg('comments__rating'))
print(f"\n{Fore.GREEN}{Style.BRIGHT}⭐ Mahsulotlar reytingi:{Style.RESET_ALL}")
for product in products:
    print(f"{Fore.BLUE}{product.name}: {product.avg_rating or 0:.1f}⭐")

# --------- Eng qimmat va eng arzon mahsulotlar ---------
prices = Product.objects.aggregate(max_price=Max('price'), min_price=Min('price'))
print(f"\n{Fore.MAGENTA}{Style.BRIGHT}💰 Eng qimmat mahsulot narxi: {prices['max_price']:,.2f} so'm{Style.RESET_ALL}")
print(f"{Fore.MAGENTA}🛒 Eng arzon mahsulot narxi: {prices['min_price']:,.2f} so'm{Style.RESET_ALL}")

# --------- Umumiy chegirma miqdori ---------
total_discount = Product.objects.aggregate(average_discount=Avg('discount'))['average_discount']
print(f"\n{Fore.RED}{Style.BRIGHT}📉 Umumiy chegirma: {total_discount:.1f}%{Style.RESET_ALL}")

# --------- Ombordagi mahsulotlarning umumiy qiymati ---------
products_with_total_value = Product.objects.annotate(
    total_value=ExpressionWrapper(F('price') * F('quantity'), output_field=DecimalField())
)
print(f"\n{Fore.BLUE}{Style.BRIGHT}📊 Omborda mavjud mahsulotlar qiymati:{Style.RESET_ALL}")
for product in products_with_total_value:
    print(f"{Fore.CYAN}- {product.name}: {product.total_value:,.2f} so'm qiymatda mavjud")

# --------- Kategoriyalar bo‘yicha mahsulotlarning o‘rtacha narxi ---------
categories_with_avg_price = Category.objects.annotate(avg_price=Avg('products__price'))
print(f"\n{Fore.YELLOW}{Style.BRIGHT}💵 Kategoriyalar bo‘yicha o‘rtacha narxlar:{Style.RESET_ALL}")
for category in categories_with_avg_price:
    print(f"{Fore.LIGHTMAGENTA_EX}- {category.title}: {category.avg_price:,.2f} so‘m")

# --------- Har bir mahsulot uchun sharhlar soni ---------
products_with_comment_count = Product.objects.annotate(comment_count=Count('comments'))
print(f"\n{Fore.LIGHTCYAN_EX}{Style.BRIGHT}💬 Mahsulotlar sharhlari soni:{Style.RESET_ALL}")
for product in products_with_comment_count:
    print(f"{Fore.LIGHTGREEN_EX}- {product.name}: {product.comment_count} ta sharh")

print(f"\n{Fore.YELLOW}{Style.BRIGHT}✅ Hisob-kitoblar yakunlandi!{Style.RESET_ALL}")


# Ishtatish uchun
# python manage.py shell
# exec(open("ann_and_agr.py", encoding="utf-8").read())
