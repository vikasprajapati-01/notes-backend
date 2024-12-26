from django.urls import path

from .views import CreateUserView, NoteCreate, NoteDelete

urlpatterns = [
    path('notes/', NoteCreate.as_view(), name="notes-list"),
    path('notes/delete/<int:pk>/', NoteDelete.as_view(), name="notes-delete"),
]