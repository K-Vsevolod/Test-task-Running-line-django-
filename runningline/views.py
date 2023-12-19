from django.shortcuts import render, HttpResponse
from . import utils
from .models import History
from django.http import FileResponse

# Create your views here.


def home(request):
    if request.GET:
        History(text=request.GET["text"]).save()
        utils.text_to_video(request.GET["text"], (100, 100))
        text = request.GET['text']
    else:
        text = None

    history = History.objects.order_by('-id')[:10]
    return render(request, "home.html", context={"text": text, "history": history})


def download(request):
    f = open("result/result.mp4", "rb")
    response = HttpResponse(f.read(), content_type="video/mp4")
    response['Content-Disposition'] = 'attachment; filename=result.mp4'
    return response