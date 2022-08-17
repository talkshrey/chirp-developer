from operator import concat
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from rest_framework.response import Response
import requests
import base64
import environ
import tweepy

url = "https://api.twitter.com/oauth2/token?grant_type=client_credentials"

env = environ.Env()
environ.Env.read_env()

# Create your views here.


def index(request):
    print(request)
    word = env('CONSUMER_KEY') + ':' + env('CONSUMER_SECRET')
    word2 = word.encode('ascii')
    word3 = base64.b64encode(word2)
    payload = {}
    headers = {
        'Authorization': 'Basic ' + word3.decode('ascii'),
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    return HttpResponse('Hello, World!')


# class Auth():
#     oauth = tweepy.OAuth1UserHandler(env('CONSUMER_KEY'), env('CONSUMER_SECRET'))
#     auth_url = oauth.get_authorization_url(True)
#     def search(request, query):
#         print(oauth)
#         api = tweepy.API(oauth)
        
#         return HttpResponseRedirect(auth_url)


def search(request, query):
    print(query)
    url = f'https://api.twitter.com/2/tweets/search/recent?query=%23{query}'

    payload = {}
    headers = {
        'Authorization': 'Bearer ' + env('BEARER_TOKEN'),
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    # print(serializers.serialize('json', response.json()['data']))

    return JsonResponse(response.json())

def show_tweet(request, id):
    url = f'https://api.twitter.com/2/tweets/{id}?expansions=author_id'

    payload = {}
    headers = {
        'Authorization': 'Bearer ' + env('BEARER_TOKEN'),
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return JsonResponse(response.json())
