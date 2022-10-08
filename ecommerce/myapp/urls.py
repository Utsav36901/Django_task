from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.RegisterProductView.as_view()),
    path('list/',views.ListProductView.as_view()),
    path('delete/<int:pk>',views.DeleteProductView.as_view(),name="delete_product"),
    path('details/<int:pk>',views.DetailProductView.as_view(),name="product_details"),
    path('update/<int:pk>',views.UpdateProductView.as_view(),name="update_product")
]