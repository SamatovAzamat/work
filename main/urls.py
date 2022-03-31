from django.urls import path
from .views import main_index, main_rasm, main_video, main_audio, main_menu, main_add_post, \
    main_delete_post, main_view_post, main_edit_post, main_cat, main_like

app_name = "main"
urlpatterns = [
    path('', main_index, name="index"),
    path('cat/<int:pk>/', main_cat, name="cat"),
    path('rasm/', main_rasm, name="rasm"),
    path('video/', main_video, name="video"),
    path('audio/', main_audio, name="audio"),
    path('menu/', main_menu, name="menu"),
    path('add-post/', main_add_post, name="add-post"),
    path('delete-post/<int:pk>/', main_delete_post, name="delete-post"),
    path('view/<int:pk>/', main_view_post, name="view"),
    path('edit/<int:pk>/', main_edit_post, name="edit"),
    path('post/<str:type>/<int:id>/', main_like, name="like")
]