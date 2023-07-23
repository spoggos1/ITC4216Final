from django.urls import path
from .views import MyLoginView, RegisterView, MyProfile #, profile



from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', MyLoginView.as_view(redirect_authenticated_user=True),name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('register/', RegisterView.as_view(),name='register'),    
    path('profile/', MyProfile.as_view(), name='profile'),
]

