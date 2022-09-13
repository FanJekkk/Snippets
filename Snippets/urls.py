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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from MainApp import views

urlpatterns = [
    path('', views.index_page, name="home"),
    path('snippets/add', views.add_snippet_page, name="add_snippet"),
    path('snippets/del/<int:id>', views.del_snippet_page, name="del_snippet"),
    path('snippets/upd/<int:id>', views.upd_snippet_page, name="upd_snippet"),
    path('snippets/list', views.snippets_page, name="snippets"),
    path('snippets/list_all', views.snippets_all, name="snippets_all"),
    path('snippets/list_hidden', views.snippets_hidden, name="snippets_hidden"),
    path('snippet/<int:id>', views.snippet_detail, name="snippet_detail"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

