from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.ProfileListView.as_view(), name='profile'),
    path('profile/<int:pk>', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('ngo/', views.NgoListView.as_view(), name='ngo'),
    path('ngo/<int:pk>', views.NgoDetailView.as_view(), name='ngo-detail')
]