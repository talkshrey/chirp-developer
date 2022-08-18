from django.http import JsonResponse, HttpResponseRedirect
from .serializers import LoginSerializer, RegisterSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from django.contrib.auth import authenticate, login
from .models import User
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
    return JsonResponse(response.json())

def auth(request):
    oauth = tweepy.OAuth1UserHandler(env('CONSUMER_KEY'), env('CONSUMER_SECRET'))
    response = HttpResponseRedirect(oauth.get_authorization_url(True))
    return response

class RegisterAPI(GenericAPIView):
	
	serializer_class = RegisterSerializer
	
	def post(self,request,*args,**kwargs):
		data = request.data
		serializer = self.serializer_class(data=data)
		serializer.is_valid(raise_exception = True)
		user = serializer.save()
		token = Token.objects.create(user=user)
		return Response({'Success':'Your account is successfully created'},status=status.HTTP_201_CREATED)


class LoginAPI(GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.get(email=email)
        # user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            token = Token.objects.get(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

def search(request, query):
    print(query)
    url = f'https://api.twitter.com/2/tweets/search/recent?query=%23{query}'

    payload = {}
    headers = {
        'Authorization': 'Bearer ' + env('BEARER_TOKEN'),
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return JsonResponse(response.json())

def show_tweet(request, id):
    url = f'https://api.twitter.com/2/tweets/{id}?expansions=author_id'

    payload = {}
    headers = {
        'Authorization': 'Bearer ' + env('BEARER_TOKEN'),
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return JsonResponse(response.json())
