from django.urls import path
from interns.views import empListView, empDetailView

urlpatterns = [
    path('list', empListView.as_view(), name='emp-list'),
    path('list/<int:pk>', empDetailView.as_view(), name='emp-detail'),
]