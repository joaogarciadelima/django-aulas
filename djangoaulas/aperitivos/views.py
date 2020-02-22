from django.shortcuts import render, get_object_or_404
from djangoaulas.aperitivos.models import Video


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})


def indice(request):
    videos = Video.objects.order_by('creation').all()
    return render(request, 'aperitivos/indice.html', context={'videos': videos})
