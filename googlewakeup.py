from datetime import datetime
import pyttsx3
from plyer import notification
def notifyme(message):
    notification.notify(
        title="TO-DO-LIST",
        message=message,
        app_name='gaurav',
        app_icon="C:\\Users\\gkush\\Downloads\\to.ico",
        timeout=30
    )
speak='Wake up Gaurav !!'*3 + '''This is time to Do something '''
todo='''
1. Brush your teeth properly 
2. Please clean me today
3. Finish your last pending project 
4. You have to call to someone
5. 4 pending notification '''
alarm_time=input("Enter Your alarm time: ")
while True:
	a=datetime.now().time()
	a=a.strftime("%I:%M")
	#for am or pm use %p
	# print(a)
	if a==alarm_time:
		engine=pyttsx3.init()
		engine.setProperty('rate', 175)
		engine.say(speak)
		engine.say(todo)
		notifyme(todo)
		engine.runAndWait()
		continue