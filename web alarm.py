import time
import webbrowser

set_alarm=input('set the website alarm as H:M:S')
url=input('enter the website URL')
actual_time=time.strftime('%I:%M:%S')

while(actual_time!=set_alarm):
  print('the alarm is ' + actual_time)
  actual_time=time.strftime('%I:%M:%S')
  time.sleep(1)

if(actual_time==set_alarm):
  print('your webpage is opening')
  webbrowser.open(url)
