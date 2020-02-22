from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {
            'titulo': 'Video Aperitivo: Motivação',
            'vimeo_id': 393131909,
        },

        'instalacao-windows': {
            'titulo': 'Instalação no windows',
            'vimeo_id': 393131909,
        },
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
