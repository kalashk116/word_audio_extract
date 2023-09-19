import requests
from bs4 import BeautifulSoup
from playsound import playsound

def get_audio_url(word):
    url = 'https://www.howtopronounce.com/'
    res = requests.get(url + word)
    soup = BeautifulSoup(res.text, 'html.parser')
    audio_url = soup.find('audio', {'class': 'htp__audio'})['src']
    return audio_url

# function to play audio
def play_audio(audio_url):
    response = requests.get(audio_url, stream=True)
    with open('pronunciation.mp3', 'wb') as f:
        f.write(response.content)
    playsound('pronunciation.mp3')

# get word from user input
word = input("Enter word to pronounce: ")

# get audio url and play audio
audio_url = get_audio_url(word)
play_audio(audio_url)
