from django.urls import path
from fbapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('user_register/',views.register,name='user_register'),
    path('user_login/',views.user_login,name='user_login'),
    path('main/',views.main,name='main'),
    path('delete/',views.delety,name='delete'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('chat/',views.chat_page,name='chat'),

]