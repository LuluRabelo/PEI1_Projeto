from django.contrib import admin
from django.urls import path
from cadastro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.criar_curriculo, name='criar_curriculo'),
    path('escolher-template/', views.escolher_template, name='escolher_template'),
    path('visualizar/<int:modelo_id>/', views.visualizar_curriculo, name='visualizar_curriculo'),
]

