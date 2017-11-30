import urllib
import time
import urllib.request
from builtins import NameError, eval, str, IndexError, KeyError


def player(nickname):
    user = 'https://api.worldoftanks.ru/wot/account/list/?application_id=6c1125fd6b6faa33876141df4c4000f1&limit=1' \
           '&search=' + nickname
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


# информация о событиях на глобальной карте
def global_map_events():
    url = 'https://api.worldoftanks.ru/wot/globalmap/events/?application_id=6c1125fd6b6faa33876141df4c4000f1'
    events = bin_to_string(url)
    return events


# информация об участии аккаунта в событии
def company(user_id):
    events = global_map_events()
    front_id = "gambit_latest"
    try:
        for event in events['data']:
            if event['status'] == "ACTIVE":
                event_id = event['event_id']
            else:
                pass
        company_info = \
            'https://api.worldoftanks.ru/wot/globalmap/eventaccountinfo/?application_id=6c1125fd6b6faa33876141df4c4000f1' \
            '&account_id=' \
            + str(user_id) \
            + '&event_id=' \
            + event_id \
            + '&front_id=' \
            + front_id
    except:
        company_info = ''

    company_info = bin_to_string(company_info)

    try:
        frame_points = company_info['data'][str(user_id)]['events'][event_id][0]['fame_points']
        updated_at = company_info['data'][str(user_id)]['events'][event_id][0]['updated_at']
        battles = company_info['data'][str(user_id)]['events'][event_id][0]['battles']
        rank = company_info['data'][str(user_id)]['events'][event_id][0]['rank']
        updated_at = time.strftime("%d %b %Y | %H:%M:%S", time.localtime(updated_at))
    except:
        frame_points = 'Игрок не принимал участия в событии'
    return company_info, frame_points, battles, rank, updated_at


def bin_to_string(data):
    try:
        url = urllib.request.urlopen(data)
        HTTPResponse = url
        string = HTTPResponse.read().decode('utf-8')
        false = 'false'
        null = '0'
        data = eval(string)
    except NameError:
        data = "Ошибка, попробуйте позже"
    return data


def account(user_id):
    user_info = 'https://api.worldoftanks.ru/wot/account/info/?application_id=6c1125fd6b6faa33876141df4c4000f1' \
                '&account_id=' + str(user_id)
    user_info = bin_to_string(user_info)
    try:
        clan_id = user_info['data'][str(user_id)]['global_rating']
    except:
        clan_id = 0
    return clan_id


