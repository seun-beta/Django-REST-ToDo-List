from django.http import HttpResponse, Http404, request
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView 

from .models import Cat

class CatListView(ListView):
    model = Cat


class CatDetailView(DetailView):
    model = Cat
    #template_name = 'polls/list_of_cats.html'


#class DogListView(View):
 #   def get(self, request):
  #      modelname = self.model.meta.verbose_name.title().lower()
   #     stuff = self.model.objects.all()
    #    ctnx = {modelname+'_list': stuff}
     #   return render(request, 'gview/'+modelname+ '_list.html', ctnx)
