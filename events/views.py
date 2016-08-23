from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Collection, Phase, Memory


def index(request):

	latest_collection_list = Collection.objects.order_by('-pub_date')[:5]
	latest_phase_list = Phase.objects.order_by('-pub_date')[:5]
	latest_memory_list = Phase.object.order_by('-pub_date')[:5]

	template = loader.get_template('events/index.html')

	context = {
		'latest_collection_list': latest_collection_list,
		'latest_phase_list': latest_phase_list,
		'latest_memory_list': latest_memory_list,
	}

	return HttpResponse(template.render(context, request))

def collection_detail(request):
    return HttpResponse("You're looking at collection %s." % collection_id)

def phase_detail(request):
    return HttpResponse("You're looking at phase %s." % phase_id)

def memory_detail(request):
    return HttpResponse("You're looking at memory %s." % memory_id)

