from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import json

from itens.models import Produtos

@method_decorator(csrf_exempt, name='dispatch')
class ItensView(View):
    def get(self, request):
        return HttpResponse("Morphine chamou o GET")
    
    def post(self, request):
        data = json.loads(request.body)
        item = Produtos(
            name=data.get('name'),
            price=data.get('price'), 
            image_url=data.get('image_url')
        )
        item.save()
        return HttpResponse("Item created successfully!")
    
def put(self, request):
    data = json.loads(request.body)
    item_id = data.get('id')
    if item_id:
        try:
            item = Produtos.objects.get(id=item_id)
            item.name = data.get('name', item.name)
            item.price = data.get('price', item.price)
            item.image_url = data.get('image_url', item.image_url)
            item.save()
            return HttpResponse("Item updated successfully!")
        except Produtos.DoesNotExist:
            return HttpResponseNotFound("Item not found")
    else:
        return HttpResponseBadRequest("Item ID is required")
    
    def delete(self, request):
        return HttpResponse("Morphine chamou o DELETE")
    
