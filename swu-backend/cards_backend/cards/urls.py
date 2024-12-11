from django.urls import path
# from cards.views import CardListAPIView, CardDetailAPIView, 
from cards.views import CardViewSet, SetViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cards', CardViewSet, basename='cards')
router.register('sets', SetViewSet, basename='sets')
urlpatterns = router.urls

# urlpatterns = [
#     path('cards/', CardListAPIView.as_view()),
#     path('cards/<int:pk>/', CardDetailAPIView.as_view())
# ]