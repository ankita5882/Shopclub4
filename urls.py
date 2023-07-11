from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.views import View


urlpatterns = [
    path('', views.home,name='home'),
    path('product-detail/<int:pk>', views.product_detailView, name='product-detail'),
    # path('product-detail/<int:pk>', views.product_detailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.PrifileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    # path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('mobile/', views.mobile, name='mobile'),
    path('topwear/', views.topwear, name='topwear'),
    path('bottomwear/', views.bottomwear, name='bottomwear'),
    path('laptop/', views.laptop, name='laptop'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('registration/', views.RegisterView.as_view(), name='registration'),
    path('checkout/', views.checkout, name='checkout'),
    path('pmode/', views.pmode, name='pmode'),

    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('logout/',views.user_logout,name='logout'),
    path('showcart/',views.showcart,name='showcart'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
