from django.shortcuts import render
import requests

from django.http import Http404 , HttpResponseRedirect
from bs4 import BeautifulSoup


def get_matches(date):
    """date should equal 'future'  or   'past'    """
    matches = []
    url = 'https://www.cybersport.ru/matches?date='+date
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    teams1 = soup.find_all('div', class_ = 'root_6Q2Jn participant_DJi5J participant1_xWFn2')
    teams2 = soup.find_all('div', class_ = 'root_6Q2Jn participant_DJi5J participant2_P9p5D')
    res = soup.find_all('div', class_ = 'score_+pSbU')  
    date = soup.find_all('div', class_ = 'date_Qyw+T')


    for i in zip(teams1, teams2, res, date):

        matches.append({'team1': str(i[0].text).strip(), 'team2': str(i[1].text).strip(), 'res': str(i[2].text).strip(), 'date':str(i[3].text).strip()})

    return matches 

def get_leaderboard():
    params = {
        'division': 'europe',
        'leaderboard': '0',
    }

    response = requests.get('https://www.dota2.com/webapi/ILeaderboard/GetDivisionLeaderboard/v0001', params=params).json()
    table = response.get('leaderboard')
    return table
    


def leaderboard(request):
    leaderbord = get_leaderboard()
    return render(request, 'main/leaderboard.html', {'leaderboard': leaderbord})

def index(request):
    matches_past = get_matches('past')
    matches_future = get_matches('future')

    return render(request, 'main/index.html', {'matches_past': matches_past, 'matches_future': matches_future})


