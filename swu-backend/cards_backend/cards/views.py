from django.shortcuts import render
from rest_framework import generics, viewsets
from cards.models import SwCard, SwSet
from cards.serializer import CardSerializer, SetSerializer



# class CardListAPIView(generics.ListAPIView):
#     queryset = SwCard.objects.all()
#     serializer_class = CardSerializer

# class CardDetailAPIView(generics.RetrieveAPIView):
#     queryset = SwCard.objects.all()
#     serializer_class = CardSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = SwCard.objects.filter(variant__contains="Normal").order_by("setid", "setcardid")
    serializer_class = CardSerializer

class SetViewSet(viewsets.ModelViewSet):
    queryset = SwSet.objects.all()
    serializer_class = SetSerializer