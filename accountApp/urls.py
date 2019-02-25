from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('welcome/',views.welcome,name='welcome'), #link to welcome [name]
    path('add5ToAccount/<int:accountID>/',views.add5ToAccount,name='add5ToAccount'), #link to increment
]