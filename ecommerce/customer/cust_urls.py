

from django.urls import path
from . import views
urlpatterns = [ 
        path('',views.home_page,name='home'),
        path('about',views.about_page,name='about'),
        path('contact',views.contact_page,name='contact'),
        path('cust_login',views.customer_login_page,name='customer_login'),
        path('cust_signup',views.customer_signup_page,name='customer_signup'),
        path('customer_home',views.customer_home,name='customer_home'),
        path('customer_profile',views.customer_profile,name='customer_profile'),
        path('customer_order',views.customer_order,name='customer_order'),
        path('customer_tickets',views.customer_tickets,name='customer_tickets'),
        path('customer_signout',views.customer_signout,name='customer_signout'),
        
        
        path('admin_login',views.admin_login,name='admin_login'),
        path('admin_home',views.admin_home,name='admin_home'),
        path('add_product',views.add_product,name='add_product'),
        path('manage_product',views.manage_product,name='manage_product'),
        path('admin_tickets',views.admin_tickets,name='admin_tickets'),
        path('admin_signout',views.admin_signout,name='admin_signout'),
        path('delete_product/<int:id>/',views.delete_product,name='delete_product'),
        path('update_product',views.update_product,name='update_product'),
        path('viewproduct/<int:pid>/',views.viewproduct,name='viewproduct'),
        path('buy_product',views.buy_product,name='buy_product'),
        path('close_ticket/<int:rid>/',views.close_ticket,name='close_ticket'),
        path('customer_reply',views.customer_reply,name='customer_reply'),
        path('admin_reply',views.admin_reply,name='admin_reply'),
]