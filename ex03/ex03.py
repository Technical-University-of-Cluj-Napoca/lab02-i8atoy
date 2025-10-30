import datetime as dt
import os


RED = "\033[0;31m"
BLUE = "\033[0;34m"
YELLOW = "\033[1;33m"
LIGHT_GRAY = "\033[0;37m"
WHITE = "\033[0m"


def smart_log(*args, **kwargs) -> None:
    for arg in args:
        arg = str(arg)
    type = kwargs.get("Level")
    
    to_color = True
    if(kwargs.get("color") == False):
        to_color = False
    
    time_stamp = True
    if(kwargs.get("timestamp") == False):
        time_stamp = False

    save_path = kwargs.get("save_to", None)

    color = WHITE
    printable = ""
    if time_stamp == True:
        printable += str(dt.datetime.now())
    match type:
        case "info":
            printable += " [INFO] "
            if to_color:
                color = BLUE
        case "debug":
            printable += " [DEBUG] "
            if to_color:
                color = LIGHT_GRAY
        case "warning":
            printable += " [WARNING] "
            if to_color:
                color = YELLOW
        case "error": 
            printable += " [ERROR]"
            if to_color:
                color = RED

    for arg in args:
        printable += str(args) 
        printable += " "
    
    if save_path:
        with open(save_path, "a") as f:
            f.write(printable + "\n")
    print(f"{color}{printable}{WHITE}")


smart_log("System started succesfully.", Level="warning", save_to="system.log", color=False)