
from django.urls import path
from .import views


urlpatterns = [
    path('',views.home, name='about'),
    path('signup/',views.signup,name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('<slug:sug_c>/', views.home, name="product_by_category"),
   # path('<slug:sug_c>/<slug_p>/', views.prod_detail,name="product_details"),
    path('new',views.speed, name='speed'),


]







