from django.urls import path
from .views import *

app_name = 'board'

urlpatterns = [
    path('', board_list),
    path('post/create/', board_post),
    path('post/detail/<int:post_id>/', board_detail),
    path('post/update/<int:post_id>/', board_detail),
    path('post/delete/<int:post_id>/', board_detail),
    path('post/comment/create/<int:post_id>/', comment_post),
    path('post/comment/list/<int:post_id>/', comment_post),
]