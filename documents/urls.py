
from django.urls import path

from documents.views import (
    DocsListView, 
    DocsRevisionsView, 
    DocsLatestView,
    DocsRevisionView,
)

urlpatterns = [
    path('', DocsListView.as_view()),
    path('<str:slug>/', DocsRevisionsView.as_view()),
    path('<str:slug>/latest/', DocsLatestView.as_view()),
    path('<str:slug>/<date:revision>/', DocsRevisionView.as_view()),
]