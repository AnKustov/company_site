from django.urls import path, include
from django.contrib.auth import views as auth_views
from .models import *
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('history/', HistoryView.as_view(), name='history_page'),
    path('mission/', MissionView.as_view(), name='mission_page'),
    path('workers/', WorkerListView.as_view(), name='worker-list'),
    path('project/<slug:slug>/', ProjectDetailView.as_view(), name='project-detail'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('offers/<int:pk>/', OfferDetailView.as_view(), name='offer_detail'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]