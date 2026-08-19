from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path("index",views.index, name='home'),
    path("about",views.about, name='about'),
    path("registration",views.registration,name='registration'),
    path("login", views.login, name="login"),
    path("edit/<int:id>",views.edit,name='edit'),
    path("delete/<int:id>", views.delete, name="delete"),
    path("contact",views.contact,name='contact'),
    path("logout", views.logout, name="logout")
]