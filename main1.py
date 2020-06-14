from tkinter import (Tk, Label, Button, TOP, CENTER, Text)
from PIL import ImageTk, Image
from tkhtmlview import HTMLLabel
from time import time, sleep
import requests

root = Tk()

root.geometry('1000x700')
root.title('Notification app')
root.configure(bg='skyblue')

#creating a Label widget
photo = ImageTk.PhotoImage(Image.open("bitcoinB.jpg"))
# Button(root, image = photo).pack(side = TOP, pady = 3.5)
myFirstData = Label(root, image = photo)
myFirstData.pack(side = TOP, pady = 10)
# Label(root, text="Hello world!").pack(side = TOP, pady = 30) 
#Shoving it onto the screen


# *******************
# Function to show app requirments on click of check_requirement button
def say_hi():
    myFirstData.destroy()
    global lbl1a, lbl1b, lbl1c, lbl1d, lbl1e
    lbl1a=Label(root, text = "Requirements :", bg="skyblue", fg="black", font="Times 18")
    lbl1a.config(anchor=CENTER)
    lbl1a.pack(pady = 5)
    lbl1b=Label(root, text = "1 - IFTTT Account.", bg="skyblue", fg="black", font="Times 18")
    lbl1b.config(anchor=CENTER)
    lbl1b.pack(pady = 5)
    lbl1c=Label(root, text = "2 - Applet created with webhooks.",bg="skyblue", fg="black", font="Times 18")
    lbl1c.config(anchor=CENTER)
    lbl1c.pack(pady = 5)
    lbl1d=Label(root, text = "3 - Two event for emergency alert and normal alerts.",bg="skyblue", fg="black", font="Times 18")
    lbl1d.config(anchor=CENTER)
    lbl1d.pack(pady = 5)
    lbl1e=Label(root, text = "4 - Suggested Message Format is\n    Normal Alert : {Bitcoin Alerts : <br> value1 }\n    Emergency Alert : {Emergency Alert : <br> value1}",bg="skyblue", fg="black", font="Times 18")
    lbl1e.config(anchor=CENTER)
    lbl1e.pack(pady = 5)

    check_requirement.destroy()
     
check_requirement = Button(root, text = "Check Requirments", command = say_hi)
check_requirement.pack(side = TOP, pady = 10)

# *******************
# Function to show available countries on click of countries button
def say_country():
    global lbl2
    lbl1a.destroy()
    lbl1b.destroy()
    lbl1c.destroy()
    lbl1d.destroy()
    lbl1e.destroy()
    check_requirement.destroy()
    # check_requirement['state']= NORMAL
    lbl2=Label(root, text = "Available Country :\nINR - INDIA\nUSD - UNITED STATES OF AMERICA\nJPY - JAPAN\nEUR - EUROPE\n AND Still more !", bg="skyblue", fg="black", font="Times 18", pady = 10)
    lbl2.config(anchor=CENTER)
    lbl2.pack(pady = 5)
    countries.destroy()

countries = Button(root, text = "Countries", command = say_country)
countries.pack(side = TOP, pady = 10)
  


# *******************
# Function to start the notifier app
def main_func():
    global start, lbl3, country, textExample, countryCode_button,html_label
    lbl2.destroy()
    countries.destroy()
    lbl3=Label(root, text = "---------------------------------------------------------------------------------\n---------------------------------------------------------------------------------\n---------------------------------------------------------------------------------\n---------------                                                 -----------------\n                        Programming is not a science.                        \n                              It is a craft ~~                         \n---------------                                                 -----------------\n---------------------------------------------------------------------------------\n---------------------------------------------------------------------------------\n---------------------------------------------------------------------------------", bg="skyblue", fg="maroon", font="Times 18", pady = 10)
    lbl3.config(anchor=CENTER)
    lbl3.pack(pady = 10)
    start.destroy()
    country = Label(root, text ='Enter the country code to setup the alerts',bg="skyblue", fg="black", font="Times 18", pady = 10)
    country.pack(side = TOP, pady = 10)
    textExample=Text(root, height=1, width=12)
    textExample.pack(side = TOP, pady = 5)
    countryCode_button= Button(root, text = "Enter", command = retrieve_input)
    countryCode_button.pack(side = TOP, pady = 10)
    html_label = HTMLLabel(root, html='<a href="https://blockchain.info/ticker" style="color: green; text-align: center"> Please visit:- https://blockchain.info/ticker, to know all the listed countries </a>')
    # html_label.pack(fill="both", expand=True)
    html_label.pack()
    html_label.fit_height()

start = Button(root, text = "Start", command = main_func)
start.pack(side = TOP, pady = 10)


# *******************
# Function to remove quote and following labels and text(this comes after starting the notifier app function)
def retrieve_input():
    global countryCode, thresh, threshinput, threshLimit
    countryCode=textExample.get("1.0","end-1c")
    # print(countryCode)
    lbl3.destroy()
    country.destroy()
    html_label.destroy()
    textExample.destroy()
    countryCode_button.destroy()
    thresh = Label(root, text ='Enter Emergency Threshold',bg="skyblue", fg="black", font="Times 18" )
    thresh.pack(side = TOP, pady = 10)
    threshinput=Text(root, height=1, width=20)
    threshinput.pack(side = TOP, pady = 5)
    threshLimit= Button(root, text = "Enter", command = retrieve_inputForThresh_input )
    threshLimit.pack(side = TOP, pady = 10)

def retrieve_inputForThresh_input():
    global threshinput1, eventinput, event1,eventButton
    threshinput1=threshinput.get("1.0","end-1c")
    thresh.destroy()
    threshLimit.destroy()
    threshinput.destroy()
    event1 = Label(root, text ='Enter the event name that you created in IFTTT', bg="skyblue", fg="black", font="Times 18" )
    event1.pack(side = TOP, pady = 10)
    eventinput=Text(root, height=1, width=30)
    eventinput.pack(side = TOP, pady = 5)
    eventButton= Button(root, text = "Enter", command = retrieve_eventinput )
    eventButton.pack(side = TOP, pady = 10)


def retrieve_eventinput():
    global event2,event2input,event2Button, eventinput1
    eventinput1=eventinput.get("1.0","end-1c")
    eventinput.destroy()
    event1.destroy()
    eventButton.destroy()
    event2 = Label(root, text ='Enter the Emergency threshold event Name', bg="skyblue", fg="black", font="Times 18")
    event2.pack(side = TOP, pady = 10)
    event2input=Text(root, height=1, width=30)
    event2input.pack(side = TOP, pady = 5)
    event2Button= Button(root, text = "Enter", command = retrieve_event2input )
    event2Button.pack(side = TOP, pady = 10)
    # print(countryCode, eventinput1, threshinput1)


def retrieve_event2input():
    global event3, event3input, event3Button, eventinput2
    eventinput2=event2input.get("1.0","end-1c") 
    event2.destroy()
    event2input.destroy()
    event2Button.destroy()
    event3 = Label(root, text ='Enter the IFTTT token ,You Got from Webhooks', bg="skyblue", fg="black", font="Times 18")
    event3.pack(side = TOP, pady = 10)
    event3input=Text(root, height=1, width=30)
    event3input.pack(side = TOP, pady = 5)
    event3Button= Button(root, text = "Enter", command = retrieve_event3input )
    event3Button.pack(side = TOP, pady = 10)
    # print(countryCode, eventinput1, threshinput1, eventinput2)



def retrieve_event3input():
    global eventinput3, timer, timerinput, timerButton
    eventinput3=event3input.get("1.0","end-1c") 
    event3.destroy()
    event3input.destroy()
    event3Button.destroy()
    timer = Label(root, text ='Enter interval time for alerts\n NOTE use 720 for 1hr interval',bg="skyblue", fg="black", font="Times 18")
    timer.pack(side = TOP, pady = 10)
    timerinput=Text(root, height=1, width=5)
    timerinput.pack(side = TOP, pady = 5)
    timerButton= Button(root, text = "Enter", command = retrieve_timer )
    timerButton.pack(side = TOP, pady = 10)
    # print(countryCode, eventinput1, threshinput1, eventinput2, eventinput3)

    
def retrieve_timer():
    global eventinput4, arr
    eventinput4=timerinput.get("1.0","end-1c") 
    timerButton.destroy()
    timerinput.destroy()
    timer.destroy()
    serverNote = Label(root, text ='Server is synchronizing your data for notification !!!', bg="skyblue", fg="black", font="Times 18")
    serverNote.pack(side = TOP, pady = 10)
    # sleep(5)
    iftttLinked = Label(root, text ='IFTTT is linked.', bg="skyblue", fg="black", font="Times 18")
    iftttLinked.pack(side = TOP, pady = 5)
    exitButton= Button(root, text = "Click here to fire the notification", command = root.destroy )
    exitButton.pack(side = TOP, pady = 10)
    # print('here from outside:', countryCode, eventinput1, threshinput1, eventinput2, eventinput3,eventinput4)

    arr= [countryCode, eventinput1, threshinput1, eventinput2, eventinput3,eventinput4]
    # return arr

def test():
    root.mainloop()
    return(arr)



def link_telegram():
    def _end():
        print('Server has encountered error ! ')
        return
    try:
        check= test()
        # print(check)

        country = check[0]
        thresh = float(check[2])
        event = check[1]
        threshevent = check[3]
        ifttt_TOKEN = check[4]
        timer =int(check[5] )
        from time import sleep
        print('Your Project is getting created !!!')
        sleep(5)
        print('IFTTT is linked.')
    except Exception:
        print("Input is invalid !")
        _end()

    def get_data(country):
        try:
            connection = requests.get(url='https://blockchain.info/ticker')
            data_in__json = connection.json()
            return (str(data_in__json[country.upper()]['last']) +
                    ' ' + str(data_in__json[country.upper()]['symbol']))
        except Exception:
            print('Data is not accessable from the url provided.')

    from datetime import datetime
    from pytz import timezone

    def formatdata():
        try:
            data = get_data(country)
            format = "Date: %Y-%m-%d || Time: %H:%M:%S"
            now_utc = datetime.now(timezone('UTC'))
            now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
            time = (now_asia.strftime(format))
            return (f'Price : {data} <br>{time} <br> <br> ')
        except Exception:
            print("Problem occured in formatting !")

    from time import sleep
    import requests

    def sendtoIFTTT():
        datahistory = []
        i = 1
        # infinite loop is created as new bitcoin price uodates keep coming
        while True:
            # data variable is used to stored data recieved from formatdata
            # module.
            data = formatdata()
            # everytime a data is collected it is added to the list.

            try:
                com = float(data.split(" ")[2])
                if com < int(thresh):
                    price = com
                    symbol = (data.split(' ')[3])
                    string = f'{price} {symbol}'
                    requests.post(
                        url=f'https://maker.ifttt.com/trigger/{threshevent}/with/key/{ifttt_TOKEN}',
                        json={
                            'value1': (string)})
                    print('Posted Emergency Alert!')
                else:
                    datahistory.append(data)
            except Exception:
                print('Entered Wrong Details!')
            try:
                print(f'Data collected {i} times !')
                # incrementing the i variable after every loop
                i += 1
                # time is set here (seconds)!
                sleep(timer)
                # this is the IFTTT Token recieved from IFTTT services
                ifttt_url = f'https://maker.ifttt.com/trigger/{event}/with/key/{ifttt_TOKEN}'
            except Exception:
                print("Project is not setupp Properly !")
            if len(datahistory) == 5:
                try:

                    # the data in list is add to string module .
                    string = "".join([x + '\n' for x in datahistory])

                    # value1 is the datafield we provided in IFTTT applet so we
                    # are assigning our string to it
                    data = {'value1': (string)}
                    # session is opened to start posting
                    s = requests.session()
                    # url and and data is send as json
                    requests.post(ifttt_url, json=data)
                    print(f'\nsent ! ')
                    # session is closed immediatelt after data is posted.
                    s.close
                    # collected data is deleted
                    del data
                    # list is cleared to get new data in the new session
                    datahistory = []

                    print('Starting New Session !')
                    # again new sesssion is started
                    sendtoIFTTT()

                except Exception:
                    print('something went wrong !!')
                    sendtoIFTTT()

    def starter():
        from time import sleep
        from tqdm import tqdm
        import sys
        try:
            animation = "✒✔༼ つ ◕_◕ ༽つ|/-\\"
            for i in range(25):
                sleep(0.1)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()
            
            loop = tqdm(total=100, position=0, leave=False)
            for _ in range(100):
                loop.set_description("Starting the Server ! ")
                sleep(.1)
                loop.update(1)
            loop.close()
            sendtoIFTTT()
        except(Exception):
            print('Starting the Project !')
            sendtoIFTTT()
    starter()



link_telegram()
    

