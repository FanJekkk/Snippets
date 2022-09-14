"""Snippets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from MainApp import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.index_page, name="home"),
                  path('snippets/add', views.add_snippet_page, name="add_snippet"),
                  path('snippets/del/<int:id>', views.del_snippet_page, name="del_snippet"),
                  path('snippets/upd/<int:id>', views.upd_snippet_page, name="upd_snippet"),
                  path('snippets/list', views.snippets_page, name="snippets"),
                  path('snippets/list_all', views.snippets_all, name="snippets_all"),
                  path('snippets/list_hidden', views.snippets_hidden, name="snippets_hidden"),
                  path('snippets/list_my', views.my_snippets, name="my_snippets"),
                  path('snippet/<int:id>', views.snippet_detail, name="snippet_detail"),
                  path('accounts/login', views.login_page, name='login_page'),
                  path('login', views.login, name='login'),
                  path('logout', views.logout, name='logout'),
                  path('registration', views.register, name='registration'),
                  path('comment/add', views.comment_add, name="comment_add"),
                  path('search_snippet/', views.search_snippet, name="search_snippet"),
                  path('user_filter/<int:id>', views.filter_by_user, name="filter_by_user"),
                  path('lang_filter/<str:lang>', views.filter_by_lang, name="filter_by_lang"),
                  path('rating_users', views.rating_users, name="rating"),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
                + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

