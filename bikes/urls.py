from django.urls import path
from .views import BikeListView, BikeDetailView,handle_purchase_request, AddReviewView, DeleteReviewView, UpdateReviewView, BikesByCategoryView


app_name = 'bikes'

urlpatterns = [
    path('', BikeListView.as_view(), name='home'),
    path('category/<int:pk>/', BikesByCategoryView.as_view(), name='category'),
    path('bike/<int:pk>/', BikeDetailView.as_view(), name='bike-detail'),
    path('bike/<int:pk>/add-review/', AddReviewView.as_view(), name='add-review'),
    path('handle_purchase_request/', handle_purchase_request, name='handle_purchase_request'),
    path('review/<int:pk>/delete/', DeleteReviewView.as_view(), name='delete-review'),
    path('review/<int:pk>/update/', UpdateReviewView.as_view(), name='update-review'),
]
