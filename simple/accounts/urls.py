from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views



app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.Login1View.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset/', views.PassResetView.as_view(), name='reset'),
    path('reset/done/', views.PassResetDoneView.as_view(), name='pass_reset_done'),
    path('reset/<uidb64>/<token>/', views.PassConfirmView.as_view(), name='pass_confirm'),
    path('reset/complete/', views.PassCompleteView.as_view(), name='pass_complete'),
    path('change/', views. PassChangeView.as_view(), name='pass_change'),
    path('change/done/', views.PassChangeDoneView.as_view(), name='pass_change_done'),
    path('my_account/', views.UserUpdateView.as_view(), name='my_account'),
]