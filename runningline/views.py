from django.shortcuts import render
from . import utils
from .models import History

# Create your views here.


def home(request):
    if request.GET:
        History(text=request.GET["text"]).save()
        utils.text_to_video(request.GET["text"], (100, 100))
    return render(request, "home.html", context={"text": request.GET, "history": History.objects.order_by('-id')[:10]})
