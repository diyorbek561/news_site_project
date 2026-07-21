from django.urls import path
from .views import NewsListView,NewsCreateView,NewsDeleteView,NewsDetailView,NewsUpdateView
urlpatterns = [
    path('', NewsListView.as_view(), name='home'),
    path('create/', NewsCreateView.as_view(), name='create'),
    path('<slug:slug>/delete/', NewsDeleteView.as_view(), name='delete'),
    path('<slug:slug>/update/', NewsUpdateView.as_view(), name='update'),
    path('<slug:slug>/', NewsDetailView.as_view(), name='post_detail'),

]