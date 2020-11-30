from colorama import Fore


def info(text):
    print(Fore.GREEN + text + Fore.RESET)

def INFO(text):
    print(Fore.GREEN + "[CryptoNet] INFO: " + text + Fore.RESET)

def warn(text):
    print(Fore.YELLOW + text + Fore.RESET)

def WARN(text):
    print(Fore.YELLOW + "[CryptoNet] WARNING: " + text + Fore.RESET)

def critical(text):
    print(Fore.RED + text + Fore.RESET)

def CRITICAL(text):
    print(Fore.RED + "[CryptoNet] CRITICAL: " + text + Fore.RESET)
