from django.urls import path
from . import views
from store.controller import authview, cartview, checkoutview

urlpatterns = [
    path('', views.home, name="home"),
    path('collections', views.collections, name='collections'),
    path('collections/<str:slug>', views.collectionsview, name='collectionsview'),
    path('collections/<str:cate_slug>/<str:prod_slug>',
         views.productview, name='productview'),

    path('register/', authview.registerpage, name="registerpage"),
    path('login/', authview.loginpage, name="loginpage"),
    path('logout/', authview.logoutpage, name="logoutpage"),

    path('add-to-cart', cartview.addtocart, name="addtocart"),
    path('cart',cartview.viewcart, name="cart"),
    path('update-cart', cartview.updatecart, name="updatecart"),
    path('delete-cart-item',cartview.deletecartitem,name="deletecartitem"),
    
    path('checkout', checkoutview.viewcheckout, name="checkout")
]
