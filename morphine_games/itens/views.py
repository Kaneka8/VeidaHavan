from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import json

from itens.models import Produtos

@method_decorator(csrf_exempt, name='dispatch')
class ItensView(View):
    def get(self, request,):
        if 'id' in request.GET:
            item_id = request.GET.get('id')
            try:
                item = Produtos.objects.get(id=item_id)
                data = {
                    'id': item.id,
                    'name': item.name,
                    'price': str(item.price),
                    'image_url': item.image_url
                }
                return HttpResponse(json.dumps(data), content_type='application/json')
            except Produtos.DoesNotExist:
                return HttpResponseNotFound("Item not found")
        else:
            items = Produtos.objects.all()
            data = []
            for item in items:
                data.append({
                    'id': item.id,
                    'name': item.name,
                    'price': str(item.price),
                    'image_url': item.image_url
                })
            return HttpResponse(json.dumps(data), content_type='application/json')
        
    def post(self, request):
        data = json.loads(request.body)
        item = Produtos(
            name=data.get('name'),
            price=data.get('price'), 
            image_url=data.get('image_url')
        )
        item.save()
        return HttpResponse("Item Criado painho!")
    
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
                return HttpResponseNotFound("Item não encontrado")
        else:
            return HttpResponseBadRequest("necessario Item ID")
    
    def delete(self, request):
        data = json.loads(request.body)
        item_id = data.get('id')
        if item_id:
            try:
                item = Produtos.objects.get(id=item_id)
                item.delete()
                return HttpResponse("Item deleted successfully!")
            except Produtos.DoesNotExist:
                return HttpResponseNotFound("Item not found")
        else:
            return HttpResponseBadRequest("Item ID is required")
