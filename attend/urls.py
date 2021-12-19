from django.urls import path
from .views import indexfunc, resultfunc, loginfunc, logoutfunc, \
    signupfunc, listfunc

urlpatterns = [
    path('index/', indexfunc, name='index'),
    path('result/<int:pk>', resultfunc, name='result'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
    path('signup/', signupfunc, name='signup'),
    path('list/', listfunc, name='list'),
]
