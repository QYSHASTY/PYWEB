from random import random
from django.views import View
from django.http import HttpResponse

random_number = random()

class RandomView(View):
   def get(self, request):
       html = f"{random()}"
       return HttpResponse(html)