from django.urls import path
from . import views

urlpatterns = [
    path('<str:menu_name>/', views.render_menu, name='render_menu'),
]
