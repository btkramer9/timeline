from .models import Collection, Phase, Memory

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
# from django.urls import reverse
from django.views import generic


def index(request):

	user_id = request.user.id

	user_collections = Collection.objects.filter(user=user_id)
	collection_list = user_collections.order_by('-pub_date')

	context = {
		'collection_list': collection_list,
	}

	return render(request, 'events/index.html', context)

def collection_detail(request, pk):

	user_id = request.user.id

	user_collection = Collection.objects.get(pk=pk)
	# user_phases = Phase.objects.filter(collection=pk)
	user_memories = Memory.objects.filter(collection=pk).order_by('memory_date')

	context = {
		'collection_list': user_collection,
		# 'user_phases': user_phases,
		'user_memories': user_memories,
	}

	return render(request, 'events/collection_detail.html', context)

# def collection_detail(request, collection_id):
#    return HttpResponse("You're looking at collection %s." % collection_id)

def phase_detail(request, phase_id):
    return HttpResponse("You're looking at phase %s." % phase_id)

def memory_detail(request, memory_id):
    return HttpResponse("You're looking at memory %s." % memory_id)
