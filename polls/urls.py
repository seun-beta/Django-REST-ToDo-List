from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'polls'

urlpatterns = [
    path('', TemplateView.as_view(template_name='polls/main.html') ),
    path('cats', views.CatListView.as_view(template_name='polls/list_of_cats.html' ), name='cat-list'),
    path('cat/<int:pk_from_url>', views.CatDetailView.as_view(), name='cat-detail'),

]
