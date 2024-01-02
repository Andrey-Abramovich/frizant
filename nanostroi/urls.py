from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='hello'),
    path('mark/<slug:category_slug>/', views.get_marks_list, name='mark'),
    path('marks/<slug:mark_slug>/', views.get_series_list, name='series'),
    path('cond/<slug:ser_slug>/', views.get_cond_list, name='conds'),
    path('order/<slug:cond_slug>', views.get_cond, name='order'),
    path('conf/', views.order_confirm, name='confirm'),
]
