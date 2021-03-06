from django.urls import path
from core.views import (
      CheckListsAPIView,
      CheckListAPIView
      )

urlpatterns = [
      path('api/checklists/', CheckListsAPIView.as_view()),
      path('api/checklists/<int:pk>/', CheckListAPIView.as_view()),
]