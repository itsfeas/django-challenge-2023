from app import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.AddView.as_view(), name='add'),
    path('edit/<int:id>/', views.EditView.as_view(), name='edit'),
    path('delete/<int:id>/', views.DeleteView.as_view(), name='delete')
]
