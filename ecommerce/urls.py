from django.contrib import admin
from django.urls import path
from ecommerce import views

app_name = 'ecommerce'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>/', views.product_detail, name='product_detail'),
    path("comment/<int:pk>/", views.comment_view, name="comment_view"),
    path('customers/', views.customer_list, name='customer_list'),
    path('customer-detail/<int:pk>/', views.customer_details, name='customer_details'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('edit_customer/<int:pk>/', views.edit_customer, name='edit_customer'),
    path('delete_customer/<int:pk>/', views.delete_customer, name='delete_customer'),
    path("toggle-favourite/<int:product_id>/", views.toggle_favourite, name="toggle_favourite"),
    path('shopping-cart/', views.view_cart, name='shopping_cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-to-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('order/', views.order_list, name='order_list'),
    path('product-grid/', views.product_grid, name='product_grid'),
    path('default/', views.default, name='default'),
    path('followers/', views.followers, name='followers'),
    path('profile/', views.profile, name='profile'),
    path('analytics/', views.analytics, name='analytics'),
    path('crm/', views.crm, name='crm'),
    path('e-commerce/', views.e_commerce, name='e-commerce'),
    path('project-management/', views.project_management, name='project-management'),
    path('saas/', views.saas, name='saas'),
    path('calendar/', views.calendar, name='calendar'),
    path('chat/', views.chat, name='chat'),
    path('inbox/', views.inbox, name='inbox'),
    path('email-detail/', views.email_detail, name='email-detail'),
    path('compose/', views.compose, name='compose'),
]
