from django.views import View
from django.http import HttpResponse


class HelloView(View):
   def get(self, request):
       html = "Hello, World"
       return HttpResponse(html)
