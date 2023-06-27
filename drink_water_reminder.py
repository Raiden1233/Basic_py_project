import time
import pyttsx3





global user_name
global Am_pm
    
    
Am_pm = ["AM", "PM"]
#______________________________________________________________________________________________________________________________________________________________________________
    
# def original_time_func(): #Just to get real time on output (pain in ass T_T)
#     x = time.ctime()
#     y = x[11:18]
        
#     hours, min_ , seconds_ = map(int,y.split(':'))
#    hours_with_zero = str(hours).zfill(2)
#     min_ = str(min_).zfill(2)
#     seconds_ = str(seconds_).zfill(2)


#     return f"{str(hours_with_zero)}:{str(min_)}:{str(seconds_)}"# To show off the time only , this one is an string original_time_
#______________________________________________________________________________________________________________________________________________________________________________



#______________________________________________________________________________________________________________________________________________________________________________
def Text_to_speach(Text):
    engine_instance = pyttsx3.init()
    engine_instance.setProperty('rate', 140)
    engine_instance.say(Text)
    engine_instance.runAndWait()
#______________________________________________________________________________________________________________________________________________________________________________


#______________________________________________________________________________________________________________________________________________________________________________
def water_drink_remind(modified, secs):
    while(True):
        modified_time = modified # contains the time when reminder should remind the user to drink water

        seconds_for_timesleep = 60 * secs # TO get the seconds for sleeptime method
            
            
        print("Reminder is executed...")
        if hours <= 12:
            a = Am_pm[0]
        else:
            a =Am_pm[1]

        
            
        time.sleep(seconds_for_timesleep)
        if original_time != modified_time:
            print(modified)
            Text_to_speach(f"Hey {user_name } You should consider drinking water now, Its already {a}.")
                

            
    #______________________________________________________________________________________________________________________________________________________________________________


    # ORIGINAL CODE AKA MAIN CODE 
    #______________________________________________________________________________________________________________________________________________________________________________

x = time.ctime()

    
y = x[11:18]
print(y)
hours, min_ , seconds_ = map(int,y.split(':'))
hours_with_zero = str(hours).zfill(2)


original_time = f"{str(hours_with_zero)}:{str(min_)}:{str(seconds_)}" # For show off the time only , this one is an string

if hours <= 12:
    a = Am_pm[0]
else:
    a =Am_pm[1]

user_name = input("Enter you name\n--> ")
reminder_option = ["After each 5 min", "After each 10 min", "After each 20 min", "After each 30 min"]

reminder = input(f"Enter how often do you wanna drink water\n1:{reminder_option[0]}\n2:{reminder_option[1]}\n3:{reminder_option[2]}\n4:{reminder_option[3]}\n----> ")
print(reminder)
match reminder:
    case "1":
        if reminder == "1" or reminder == reminder_option[0]:
            print(f"Current time is {original_time} {a}\nI'll remind you to drink water {reminder_option[0]} ")
            later = 5
            min_ = min_+ later
                
            modified_time = f"{str(hours_with_zero)}:{str(min_)}:{str(seconds_)}" 
                # print(f"{modified_time} modified")
            water_drink_remind(modified_time,later)
        
    case "2":
         if reminder == "2" or reminder == reminder_option[1]:
            print(f"Current time is {original_time} {a}\nI'll remind you to drink water {reminder_option[1]} ")
            later = 10
            min_ = min_+ later 
            modified_time = f"{str(hours_with_zero)}:{str(min_)}:{str(seconds_)}" 
                
            water_drink_remind(modified_time,later)
        
    case "3":
        if reminder == "3" or reminder == reminder_option[2]:
            print(f"Current time is {original_time} {a}\nI'll remind you to drink water {reminder_option[2]} ")
            later = 20
            min_ = min_+ later
            modified_time = f"{str(hours_with_zero)}:{str(min_)}:{str(seconds_)}" 
            water_drink_remind(modified_time,later)
        
    case "4":
        if reminder == "4" or reminder == reminder_option[3]:
            print(f"Current time is {original_time} {a}\nI'll remind you to drink water {reminder_option[3]} ")
            later = 30
            min_ = min_+ later
            modified_time = f"{str(hours_with_zero)}:{str(min_)}:{str(seconds_)}" 
            water_drink_remind(modified_time,later)
    case _:
        print("Choose valid option please. ")
    #______________________________________________________________________________________________________________________________________________________________________________

