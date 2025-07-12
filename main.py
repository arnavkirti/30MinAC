import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv('API_URL')
USERNAME = os.getenv('USERNAME')

# leetcode.com/problems/two-sum, leetcode.com/problems/four-divisors


def get_problem_slug(url):
    try:
        return url.strip().split('/problems')[1].strip('/').lower()
    except IndexError:
        print("Invalid URL format. Please enter a valid URL")
        exit(1)


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    print("\nTime's Up!\n")


def hint(slug):
    try:
        res = requests.get(f"{API_URL}problem/{slug}")
        hints = res.json().get("hints", [])
        print("Hint(s):")
        for h in hints:
            print("-", h)
    except Exception as e:
        print(f"Could not fetch hints: {e}")


def submission(slug, timer):
    start = time.time()
    print("Waiting for your submission...")

    while time.time() - start < timer:
        try:
            res = requests.get(f"{API_URL}user/{USERNAME}/submissions?limit=3")
            data = res.json()

            if not data:
                continue

            latest = data[0]
            title_slug = latest.get("titleSlug", "").lower().strip()

            if title_slug == slug and latest.get("statusDisplay") == "Accepted":
                return True
        except Exception as e:
            print(f"Error checking submission: {e}")

        time.sleep(10)

    return False


def main():
    x = input("Enter the problem URL: ")
    slug = get_problem_slug(x)
    print(f"The timer is starting for {slug}")

    countdown(3)

    if submission(slug, 1):
        print("Congrats +10 pts for you")
        return

    print("Time's up and no accepted submission detected.")
    print("Here's a hint and 10 more minutes to try again.")
    hint(slug)
    countdown(1)

    if submission(slug, 1):  # 1 minute grace period again
        print("Nice recovery! +5 points for you.")
    else:
        print("Still not solved. No worries — check the solution and learn from it!")


if __name__ == "__main__":
    main()
