from django.urls import path
from . import views

urlpatterns = [
    path('', views.discuss_list),
    path('<int:discuss_pk>/', views.discuss_detail),
    path('<int:discuss_pk>/choice_a/', views.choice_a),
    path('<int:discuss_pk>/choice_b/', views.choice_b),
    path('<int:discuss_pk>/comments/', views.create_comment),
    path('<int:discuss_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete)
]
