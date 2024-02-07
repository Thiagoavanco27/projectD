from django.shortcuts import render

from utils.philo.factory import MakeMeditation


def home(request):
    return render(request, 'philosofia/pages/index.html', context={
        'meditations': [MakeMeditation() for _ in range(10)],
    })

def meditation(request, id):
    return render(request, 'philosofia/pages/meditation-view.html', context={
        'meditations': MakeMeditation(),
        'is_detail_page': True,
    })