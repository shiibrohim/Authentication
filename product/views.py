from rest_framework import generics
from product.models.product import Noutbooks
from .serializers import NoutbooksSerializer

class NoutbookListCreateView(generics.ListCreateAPIView):
    queryset = Noutbooks.objects.all()
    serializer_class = NoutbooksSerializer

class NoutbookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Noutbooks.objects.all()
    serializer_class = NoutbooksSerializer