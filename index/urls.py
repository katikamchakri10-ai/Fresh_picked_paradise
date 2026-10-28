
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('slider/',views.home2,name='home2'),
    path('about/',views.about,name='about'),
    path('news/',views.news,name='news'),
    path('contact/',views.contact,name='contact'),
    path('shop/',views.shop,name='shop'),
    path('page404/',views.page404,name='page404'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('singlenews/',views.singlenews,name='singlenews'),
    path('singleproduct/',views.singleproduct,name='singleproduct'),
    path('chatbot-api/', views.chatbot_api, name='chatbot_api'),


]
