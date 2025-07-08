import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv('API_URL')

x = input("Enter the Problem URL: ") # leetcode.com/problems/merge-intervals/
slug = x.strip().split("/")[2]
print(f"The timer is starting for {slug}")


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1

def hint():
    x = requests.get(API_URL + 'problem/' + slug)
    print(x.json()["hints"])

timer1 = 3 #minutes
countdown(timer1)
hint()
print("30 mins done")

print("Did you solve it? y/N")
ans = input()
if(ans == 'y'):
    print("+10 points for you")
else:
    print("Okay here's a hint and additional 10 mins")
    countdown(1) #minutes
    print("10 mins have passed. Did you solve it? y/N")
    again = input()
    if(again == 'y'):
        print("+5 points for you")
    else:
        print("You're worthless!! See the solution and learn you fool.")
