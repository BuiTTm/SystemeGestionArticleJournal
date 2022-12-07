from django.urls import path
from utilisateurs import views


urlpatterns = [
    #Auth
    path('signup/', views.signupuser, name = 'signupuser'),
    path('logout/', views.logoutuser, name = 'logoutuser'),
    path('login/', views.loginuser, name = 'loginuser'),

    #User
    #path('', views.home, name='home'),
]
