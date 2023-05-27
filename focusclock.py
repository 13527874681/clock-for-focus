import time

def pomodoro_timer(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print('Time is up!')

pomodoro_timer(25)  # 专注时钟的时间为 25 分钟
