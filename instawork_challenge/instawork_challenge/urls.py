from app.views.add import AddView
from app.views.edit import EditView
from app.views.list import TeamMemberListView
from app.views.delete import DeleteView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TeamMemberListView.as_view(), name='index'),
    path('add/', AddView.as_view(), name='add'),
    path('edit/<int:id>/', EditView.as_view(), name='edit'),
    path('delete/<int:id>/', DeleteView.as_view(), name='delete')
]
