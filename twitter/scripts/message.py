import tweepy
consumer_key = 'lVbKvoKd8SLB4J38SWz0ku76P'
consumer_secret = 'wPKxz15tUcbK8LHNtIHcUhj2GLDq7xk75vYDhOSWwibIP0Y5cY'
access_token = '1432273857176489989-EJW2ePwP3sZmIpoqvtkWMApUWfQPK2'
access_token_secret = '4Caau5nAmOMZKx7NmHcKailf7TZNkJg3FDYpAuGLECukQ'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

recipient_id = 1268031081955102720
text = "This is a Direct Message. Check out my resume at https://drive.google.com/drive/u/0/folders/18fys9NSQi0nwqYhXGlHO_BOXHXgZqTDn"
direct_message = api.send_direct_message(recipient_id, text)