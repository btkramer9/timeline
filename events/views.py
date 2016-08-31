from .models import Collection, Phase, Memory

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
# from django.urls import reverse
from django.views import generic


def index(request):

	latest_collection_list = Collection.objects.order_by('-pub_date')[:5]
	latest_phase_list = Phase.objects.order_by('-pub_date')[:5]
	latest_memory_list = Memory.objects.order_by('-pub_date')[:5]

	context = {
		'latest_collection_list': latest_collection_list,
		'latest_phase_list': latest_phase_list,
		'latest_memory_list': latest_memory_list,
	}

	return render(request, 'events/index.html', context)

class CollectionView(generic.DetailView):
	model = Collection
	template_name = 'events/collection_detail.html'

# def collection_detail(request, collection_id):
#    return HttpResponse("You're looking at collection %s." % collection_id)

def phase_detail(request, phase_id):
    return HttpResponse("You're looking at phase %s." % phase_id)

def memory_detail(request, memory_id):
    return HttpResponse("You're looking at memory %s." % memory_id)
