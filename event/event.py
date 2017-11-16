import urllib
from decimal import Decimal
from django.conf import settings


def player(nickname):
    user = 'https://api.worldoftanks.ru/wot/account/list/?application_id=6c1125fd6b6faa33876141df4c4000f1&limit=1&search=' + nickname
    url = urllib.request.urlopen(user)
    HTTPResponse = url
    string = HTTPResponse.read().decode("utf-8")
    account_id = eval(string)
    try:
        user_id = account_id['data'][0]['account_id']
        nickname = account_id['data'][0]['nickname']
    except IndexError:
        user_id = 'Игрока с таким никнеймом не существует'
    except KeyError:
        user_id = 'Игрока с таким никнеймом не существует'
    # array = [user_id, nickname]
    return user_id, nickname


def company(user_id):
    company_info = 'https://api.worldoftanks.ru/wot/globalmap/eventaccountinfo/?application_id=6c1125fd6b6faa33876141df4c4000f1&event_id=steel_corrida_third_step&front_id=campaign_05_ru_west&account_id=' + str(user_id)
    company_info = bin_to_string(company_info)
    frame_points = company_info['data'][str(user_id)]['events']['steel_corrida_third_step'][0]['fame_points']
    return company_info, frame_points


def bin_to_string(data):
    try:
        url = urllib.request.urlopen(data)
        HTTPResponse = url
        string = HTTPResponse.read().decode('utf-8')
        data = eval(string)
    except NameError:
        data = "Ошибка, попробуйте позже"
    return data
