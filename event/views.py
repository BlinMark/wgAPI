from django.shortcuts import render
from .event import player, company
from .forms import PlayerForm


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
            battles = company(user_id)[2]
            rank = company(user_id)[3]
            updated_at = company(user_id)[4]
            rank_delta = company(user_id)[5]
    form = PlayerForm()

    return render(request, 'event/event.html', {'index': index,
                                                'form': form,
                                                'user_id': user_id,
                                                'nickname': nickname,
                                                'frame_points': frame_points,
                                                # 'company_info': company_info,
                                                'battles': battles,
                                                'rank': rank,
                                                'updated_at': updated_at,
                                                'rank_delta': rank_delta,
                                                })

