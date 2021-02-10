from collections import namedtuple
from bs4 import BeautifulSoup
import requests


URL = 'https://www.codewars.com/users/leaderboard'


class LeaderBoard:
    def __init__(self, board=None):
        self._board = board

    def __getitem__(self, key):
        return self._board[key]

    def __len__(self):
        return 500


def solution():
    Board = namedtuple('Board', 'position')
    User = namedtuple('User', 'name clan honor')

    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')

    members = soup.select('.leaderboard tr')[1:]
    top_users = ['zero-index']
    for item in members:
        name = item.find('a').text
        attrs = item.find_all('td')[-2:]
        clan = attrs[0].text
        honor = int(attrs[1].text.replace(',', ''))
        top_users.append(User(name, clan, honor))

    leader_board = LeaderBoard(top_users)
    return Board(leader_board)

