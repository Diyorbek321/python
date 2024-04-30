from django.urls import path

urlpatterns=[
    path('articles/<int:year>/',),
    path('articles/<int:year>/<int:month>/'),
    path('articles/<int:year>/<int:month>/<int:pk>/')
]