from django.urls import path
from .views import MeasureListView, MeasureDetailView, MeasureCreateView
from . import views

urlpatterns = [
    path('', MeasureListView.as_view(), name="measure-home"),
    path('id/<pk>/', MeasureDetailView.as_view(), name="measure-detail"),
    path('new/', MeasureCreateView.as_view(), name="measure-create"),
    path('about/', views.about, name="measure-about")
]
