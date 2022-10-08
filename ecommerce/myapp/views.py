from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView,DetailView
from .models import product

# Create your views here.

class RegisterProductView(CreateView):
    model  = product
    fields = "__all__"
    template_name = "home/product_register.html"
    success_url="../list/"
class DeleteProductView(DeleteView):
    model  = product
    template_name = "home/product_delete.html"
    success_url="../list/"
class UpdateProductView(UpdateView):
    model  = product
    fields = "__all__"
    template_name = "home/product_register.html"
    success_url="../list/"
    
class ListProductView(ListView):
    model = product
    template_name = "home/product_list.html"
    context_object_name = 'products' 

class DetailProductView(DetailView):
    model = product
    template_name = "home/product_details.html"
    context_object_name = 'product'  