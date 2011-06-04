from django.http import HttpResponseRedirect
from django.shortcuts import render
from models import Poll

def show(request, poll_id):
    poll =  Poll.objects.get(id=poll_id)
    if poll.is_visable():
        return render(request, "poll/show.html", {'poll' : poll})
    
    return HttpResponseRedirect("/")


