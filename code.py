import Requests

URL = 'https://api.chess.com/pub/player/' # used to retrieve basic data
ARCHIVE = '/games/archives' # used to retrieve comprehensive game data
user = input("Enter username")

req = Requests(URL + user)


