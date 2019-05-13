import threading
import urllib.request
import tweepy
import time
import random

api_key = "bIr0KfGn3IAPVPfwYNuLgEmN6"
api_secret = "V7mTHkkknzvV9EJMV6dqbr0muP3NYuUj3xCp1rkyte8on2dRYT"
access_token = "900189589603790850-XkZDnogPjQQ4z2tv9vn5wyT2bsrFgJ6"
access_token_secret = "NrqRdAfam9w8ZDjw2HSOezWa1dC48CYzDJ6hTpRU0lZh7"

def setInterval(func, time):
    e = threading.Event()
    while not e.wait(time):
        func()

def foo():
    print('hello')

def time_test():
    i = 1 
    while True:
        if i % 3 == 0 and i != 0:
            api.update_status('\nSeverous Snape\n')
            #time.sleep(1)
        else:
            rnd = random.randint(-1000, 1000)
            api.update_status(f'Snape {rnd}')
        time.sleep(60)
        if i % 3 != 0:
            i += 1
        else: 
            i = 1
if __name__ == '__main__':
    #setInterval(foo, 5)
    #f = urllib.request.urlopen('http://www.python.org')
    #print(f.read().decode('utf-8'))
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    #
    api = tweepy.API(auth)

#    tweets = api.home_timeline()
#    for t in tweets:
#        print(t.text)
    
    #api.update_status('Hi doggy')
    time_test()
    print('done')
