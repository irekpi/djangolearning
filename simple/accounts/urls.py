from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from .views import Login1View

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', Login1View.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]