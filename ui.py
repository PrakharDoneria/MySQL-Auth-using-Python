import os
import time
from colorama import Fore, Style

# Console Cleaner
def clear():
    time.sleep(2)
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception as e:
        pass

# Color Blue
def colorBlue(input_text):
    try:
        print(Fore.BLUE + input_text + Style.RESET_ALL)
    except Exception as e:
        pass

# Color Red
def colorRed(input_text):
    try:
        print(Fore.RED + input_text + Style.RESET_ALL)
    except Exception as e:
        pass

# Color Green
def colorGreen(input_text):
    try:
        print(Fore.GREEN + input_text + Style.RESET_ALL)
    except Exception as e:
        pass
