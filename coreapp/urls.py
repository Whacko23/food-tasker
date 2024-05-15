from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import IndexView, RestaurantSignupView, SignupSuccessView, UserCreateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('restaurant/signup/', RestaurantSignupView.as_view(), name='signup'),
    path('restaurant/signup/success/', SignupSuccessView.as_view(), name='signup_success'),
    path('user/signup/', UserCreateView.as_view(), name='user_signup'),

]


