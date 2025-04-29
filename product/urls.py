from django.urls import path
from .views import NoutbookListCreateView, NoutbookRetrieveUpdateDestroyView

urlpatterns = [
    path('noutbooks/', NoutbookListCreateView.as_view(), name='noutbook-list-create'),
    path('noutbooks/<int:pk>/', NoutbookRetrieveUpdateDestroyView.as_view(), name='noutbook-detail'),
]