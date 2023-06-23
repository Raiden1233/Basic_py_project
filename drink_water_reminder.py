import time
import pyttsx3



while(True):

    global user_name
    global Am_pm
    
    Am_pm = ["AM", "PM"]
#______________________________________________________________________________________________________________________________________________________________________________
    
    def original_time_func(): #Just to get real time on output (pain in ass T_T)
        x = time.ctime()
        y = x.lstrip("Sat Jun 24") 
        new_y = y
        real_time = new_y.rstrip("2023")
        hours, min_ , seconds_ = map(int, real_time.split(':'))
        hours_with_zero = str(hours).zfill(2)

        global original_time
        return  f"{str(hours_with_zero)}:{str(min_)}:{str(seconds_)}"# For show off the time only , this one is an string 
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
        seconds_for_timesleep = 60 * secs # TO get the seconds for sleeptime method
        original_time = original_time_func() # To provide a value to original  time before using it in for loop
        if original_time == "12:00:00":
            add_pm_to_time = f" {original_time} {Am_pm[1]}"  
        else:
            add_pm_to_time = f"{original_time} {Am_pm[0]}"
        
        print("Reminder is executed...")

        for  i in range(1,seconds_for_timesleep):
            original_time = original_time_func()
            print(original_time)
            time.sleep(1)

        time.sleep(seconds_for_timesleep)
        
        time.sleep(seconds_for_timesleep)
        
        if original_time != modified:
            print(modified)
            Text_to_speach(f"Hey{user_name} You should consider drinking water now, Its already {add_pm_to_time}.")
    #______________________________________________________________________________________________________________________________________________________________________________


    # ORIGINAL CODE AKA MAIN CODE 
    #______________________________________________________________________________________________________________________________________________________________________________

    x = time.ctime()
    y = x.lstrip("Sat Jun 24") 
    new_y = y
    real_time = new_y.rstrip("2023")
    hours, min_ , seconds_ = map(int, real_time.split(':'))
    hours_with_zero = str(hours).zfill(2)


    original_time = f"{str(hours_with_zero)}:{str(min_)}:{str(seconds_)}" # For show off the time only , this one is an string



    user_name = input("Enter you name\n--> ")
    reminder_option = ["After each 5 min", "After each 10 min", "After each 20 min", "After each 30 min"]

    reminder = input(f"Enter how when do you wanna drink water\n1:{reminder_option[0]}\n2:{reminder_option[1]}\n3:{reminder_option[2]}\n4:{reminder_option[3]}\n----> ")
    print(reminder)
    match reminder:
        case "1":
            if reminder == "1" or reminder_option[0]:
                print(f"Current time is {original_time} {Am_pm[0]}\nI'll remind you to drink water {reminder_option[0]} ")
                later = 5
                min_ = min_+ later
                modified_time = f"{str(hours_with_zero)}:{str(min_)}:{str(seconds_)}" 
                water_drink_remind(modified_time,later)
        case "2":
            if reminder == "2" or reminder_option[1]:
                print(f"Current time is {original_time} {Am_pm[0]}\nI'll remind you to drink water {reminder_option[1]} ")
                later = 10
                min_ = min_+ later 
                modified_time = f"{str(hours_with_zero)}:{str(min_)}:{str(seconds_)}" 
                water_drink_remind(modified_time,later)
        case "3":
            if reminder == "3" or reminder_option[2]:
                print(f"Current time is {original_time} {Am_pm[0]}\nI'll remind you to drink water {reminder_option[2]} ")
                later = 20
                min_ = min_+ later
                modified_time = f"{str(hours_with_zero)}:{str(min_)}:{str(seconds_)}" 
                water_drink_remind(modified_time,later)
        case "4":
            if reminder == "4" or reminder_option[3]:
                print(f"Current time is {original_time} {Am_pm[0]}\nI'll remind you to drink water {reminder_option[3]} ")
                later = 30
                min_ = min_+ later
                modified_time = f"{str(hours_with_zero)}:{str(min_)}:{str(seconds_)}" 
                water_drink_remind(modified_time,later)
        case _:
            print("Choose valid option please. ")
    #______________________________________________________________________________________________________________________________________________________________________________

