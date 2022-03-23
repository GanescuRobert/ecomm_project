from django.urls import path
from . import views
from store.controller import authview, cartview, checkoutview, wishlistview

urlpatterns = [
    path('', views.home, name="home"),
    path('collections', views.collections, name='collections'),
    path('collections/<str:slug>', views.collectionsview, name='collectionsview'),
    path('collections/<str:cate_slug>/<str:prod_slug>',
         views.productview, name='productview'),

    path('register/', authview.registerpage, name="registerpage"),
    path('login/', authview.loginpage, name="loginpage"),
    path('logout/', authview.logoutpage, name="logoutpage"),

    path('cart',cartview.viewcart, name="cart"),
    path('add-to-cart', cartview.addtocart, name="addtocart"),
    path('update-cart', cartview.updatecart, name="updatecart"),
    path('delete-cart-item',cartview.deletecartitem,name="deletecartitem"),
    
    path('wishlist',wishlistview.index, name="wishlist"),
    path('add-to-wishlist', wishlistview.addtowishlist, name="addtowishlist"),
    path('delete-wishlist-item',wishlistview.deletewishlistitem,name="deletewishlistitem"),
    
    path('checkout', checkoutview.viewcheckout, name="checkout"),
    path('placeorder', checkoutview.placeorder, name="placeorder"),
]
