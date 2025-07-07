import time

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
    print("30 mins done")


timer1 = 30*60 #minutes
countdown(timer1)
