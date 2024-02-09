from django.contrib import admin
from django.urls import path
from studentapp import views
urlpatterns = [
   # path('admin/', admin.site.urls),
  #  path('testing',views.testing),
    path('index',views.create),
    path('dashboard',views.dashboard),
    path('edit/<id>',views.edit),
    path('delete/<id>',views.delete),
    path('login',views.login),
    path('home',views.home),

   
]


