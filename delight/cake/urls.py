from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.index,name='index'),
    path("register/", views.sign_up, name="sign_up"), 
    path("login/", views.sign_in, name="sign_in"), 
    path("logout/", views.sign_out, name="sign_out"),
    
     
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('menu/',views.menu,name='menu'),
    path('order/',views.order,name='order'),
    path('live-search/', views.live_search, name='live_search'),
  

  
    path('<str:category>/',views.product_list,name='product_list'),

] 
