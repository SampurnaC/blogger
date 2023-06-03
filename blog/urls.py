from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm

urlpatterns = [
    path('', views.index_view, name='index'),
    path('about/', views.about, name='about'),
    path('new/', views.new_view, name='new'),
    path('show/<int:id>', views.detail_view, name='detail-view'),
    path('edit/<int:id>', views.update_view, name='update'),
    # path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.destroy_view, name='delete'),
    path('search/', views.search_blog, name='search-blog'),
    path('blog/<int:id>/comment', views.add_comment, name='add_comment'),

    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html', authentication_form=LoginForm), name='login'),

    path('logout/', views.logout_user, name='logout'),
]
