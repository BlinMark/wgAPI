from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from .forms import PlayerForm
from .event import player, company


def index(request):
    print(request.POST, request.method)

    form = PlayerForm()

    return render(request, 'event/index.html', {'index': index,
                                                'form': form})


def search(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            user_id = player(request.POST['nickname'])[0]
            nickname = player(request.POST['nickname'])[1]
            company_info = company(user_id)[0]
            frame_points = company(user_id)[1]
    form = PlayerForm()

    return render(request, 'event/index.html', {'index': index,
                                                'form': form,
                                                'user_id': user_id,
                                                'nickname': nickname,
                                                # 'company_info': company_info,
                                                'frame_points': frame_points,
                                                })

