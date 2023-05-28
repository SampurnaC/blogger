from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('about/', views.about, name='about'),
    path('new/', views.new_view, name='new'),
    path('edit/<int:id>', views.update_view, name='update'),
    # path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.destroy_view, name='delete'),

    path('search/', views.search_blog, name='search-blog'),

]
