from django.urls import path
from utilisateurs import views
from .views import SignUpView

urlpatterns = [
    #Auth
    path("signup/", SignUpView.as_view(), name="signupuser"),
    #path('signup/', views.signupuser, name = 'signupuser'),
    #path('logout/', views.logoutuser, name = 'logoutuser'),
    #path('login/', views.loginuser, name = 'loginuser'),

    #User
    #path('', views.home, name='home'),
]
