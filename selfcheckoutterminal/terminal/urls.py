from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('additem_text/', views.addItemText),
    path('additem_scan/', views.addItemScan),
    path('additem_image/', views.addItemImage),
    path('deleteitem/', views.deleteItem),
    path('delete/', views.cancelCart),
    path('ageCheck/', views.ageCheck),
    path('verifyAge/', views.verifyAge),
    path('payment/', views.payment),
]
