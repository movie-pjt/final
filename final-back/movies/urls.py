from django.urls import path
from . import views

urlpatterns = [
    # 영화 목록 출력
    path('', views.movie_list),
    # 영화 상세 페이지
    path('<int:movie_pk>/', views.movie_detail),
    # 리뷰 생성
    path('<int:movie_pk>/reviews/', views.review_create),
    # 리뷰 게시글 조회, 업데이트, 삭제
    path('reviews/<int:review_pk>/', views.review_detail),
    # 영화 좋아요
    path('<int:movie_pk>/like/', views.like_movie),
    # 리뷰 좋아요
    path('reviews/<int:review_pk>/like/', views.like_review),
    # 영화 본 횟수
    path('<int:movie_pk>/movie_count/', views.movie_count),
    # 추천 영화 목록
    path('recommendations/', views.recommendations),
]
