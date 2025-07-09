import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv('API_URL')
USERNAME = os.getenv('USERNAME')

# leetcode.com/problems/two-sum, leetcode.com/problems/four-divisors
x = input("Enter the Problem URL: ")
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
    hints = x.json().get("hints", [])
    print("Hint(s): ")
    for h in hints:
        print("-", h)


def submission(t):
    while True:
        try:
            x = requests.get(API_URL + 'user/' + USERNAME +
                             '/submissions?limit=3')
            data = x.json()
            if data[0].get("title") == slug and data[0].get("statusDisplay") == "Accepted":
                if t == 1:
                    print("Congrats +10 pts for you.")
                else:
                    print("Congrats +5 pts for you.")
                break
        except Exception as e:
            print(f"Error fetching data {e}")
        time.sleep(t)


def main():
    countdown(3)
    submission(1)
    print("30 mins done")

    print("Did you solve it? y/N")
    ans = input("y/N: ")
    if (ans == 'y'):
        print("+10 points or you")
    else:
        print("Okay here's a hint and additional 10 mins")
        hint()
        countdown(1)  # minutes
        print("10 mins have passed. Did you solve it? y/N")
        again = input("y/N: ")
        if (again == 'y'):
            print("+5 points for you")
        else:
            print("You're worthless!! See the solution and learn you fool.")


if __name__ == "__main__":
    main()
