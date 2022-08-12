from operator import concat
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests, base64, environ, tweepy

url = "https://api.twitter.com/oauth2/token?grant_type=client_credentials"

env = environ.Env()
environ.Env.read_env()

# Create your views here.
def index(request):
    print(request)
    word = env('CONSUMER_KEY')+ ':' + env('CONSUMER_SECRET')
    word2 = word.encode('ascii')
    word3 = base64.b64encode(word2)
    payload = {}
    headers = {
    'Authorization': 'Basic '+ word3.decode('ascii'),
    }
    response = requests.request("POST", url, headers=headers, data = payload)
    print(response.text)
    return HttpResponse('Hello, World!')

def auth(request):
    oauth = tweepy.OAuthHandler(env('CONSUMER_KEY'), env('CONSUMER_SECRET'))
    auth_url = oauth.get_authorization_url(True)
    response = HttpResponseRedirect(auth_url)
    request.session['request_token'] = oauth.request_token
    print(auth_url)
    return response