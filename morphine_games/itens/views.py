from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View

class ItensView(View):
    def get(self, request):
        return HttpResponse("Morphine chamou o GET")
    
    def post(self, request):
        return HttpResponse("Morphine chamou o POST")
    
    def put(self, request):
        return HttpResponse("Morphine chamou o PUT")
    
    def delete(self, request):
        return HttpResponse("Morphine chamou o DELETE")