from django.urls import path

from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.store, name="store"),
	path('about/',views.about,name='about'),
	path('contact/',views.contact,name='contact'),

	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	#path('dsh/',views.dsh,name='dsh'),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('profile/',views.profile,name='profile'),
	path('signup/',views.signup,name='signup'),  
	path('signin/',auth_views.LoginView.as_view(template_name="store/signin.html"),name='signin'),
	path('signout/',auth_views.LogoutView.as_view(template_name = 'store/signout.html'),name = 'signout'),
	path('accounts/profile/',views.store,name = "store"),
	path('dsh/',views.dashboard,name='dsh'),
	path('log/',auth_views.LoginView.as_view(template_name='store/login1.html'),name='log'),
	path('lgo/',auth_views.LogoutView.as_view(template_name='store/logout.html'),name='lgot'),


	path('addpro/',views.addproduct,name="addpro"),
	



]