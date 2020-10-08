import re
import requests
import sys
from requests.exceptions import ConnectionError, Timeout
from colorama import init, Fore, Back, Style
init()

#Regular expression
regex = 'https?:\/\/[=a-zA-Z0-9\_\/\?\&\.\-]+'

#List of each links
links = []
dead_links = []

unknown_links = []
# --- functions ---
#Colour functions
def prLightGray(skk): print("\033[90m {}\033[00m" .format(skk))

#file check function
def file_chekcer(file, flag):
    with open(file, 'rt') as f:
        contentUrls = re.findall(regex, f.read())
    if flag == "g":
        for url in contentUrls:
            check_good_links(url)
    elif flag == "b":
        for url in contentUrls:
            check_bad_links(url)
    else:
        for url in contentUrls:
            check_dead_links(url)

#Dead link checker, Check the resonse status and show users that URL is dead or not
#Save in the list each URLs
#Using Request libarary
#The link which have connection error print the "Unknown URls"
def check_dead_links(URL):
    try:
        response = requests.get(URL, timeout=1.5)
        if response.status_code == 200:
            links.append("PASSED [" + str(response.status_code) + "] " + URL + " - Good")
            print(Fore.GREEN + links[-1])
        elif response.status_code >= 300 and response.status_code < 400:
            link_redirects(URL)
        elif response.status_code >= 400 and response.status_code <= 599:
            dead_links.append("FAILED [" + str(response.status_code) + "] " + URL + " - Bad")
            print(Fore.RED + dead_links[-1])
        else:
            raise ConnectionError

    except (Timeout, ConnectionError) as e:
        prLightGray("UNKNOWN " + URL);

def check_good_links(URL):
    try:
        response = requests.get(URL, timeout=1.5)
        if response.status_code == 200:
            links.append("PASSED [" + str(response.status_code) + "] " + URL + " - Good")
            print(Fore.GREEN + links[-1])
    except (Timeout, ConnectionError) as e:
        unknown_links.append("UNKNOWN " + URL);

def check_bad_links(URL):
    try:
        response = requests.get(URL, timeout=1.5)
        if response.status_code >= 400 and response.status_code <= 599:
            dead_links.append("FAILED [" + str(response.status_code) + "] " + URL + " - Bad")
            print(Fore.RED + dead_links[-1])
    except (Timeout, ConnectionError) as e:
        unknown_links.append("UNKNOWN " + URL);
def link_redirects(r_url):
    while True:
        yield r_url
        res = requests.head(r_url)
        if 300 <= res.status_code < 400:
            r_url = res.headers['location']
        else:
            break

#Showing the result after checking all of the URLs in the file
def check_result():
    print(Fore.RESET + "\n------------- Checking is done ---------------")
    if links:
        print("------ The following links were working ------")
        for link in links:
            print(Fore.GREEN + "| " + link)
    if dead_links:
        print(Fore.RESET + "------ The following links were broken -------")
        for link in dead_links:
            print(Fore.RED + "| " + link)

#Help message function
#User can call this function when user do not write argument or wrtie -h or -H
def help_dead_link_check():
    print(Fore.GREEN +
        """
-----------------------------------------------------
|                      help                         |
-----------------------------------------------------""")
    prLightGray("""-----------------------------------------------------
|           How to use Dead Link checker?           |
| 1)URLs Checker                                    |
|   - DLCheck [URL] [URL] ...                       |
|   ex) DLCheck youtube.ca google.ca                |
| 2)Files Checker                                   |
|   - DLCheck [File name] [File name]...            |
|   ex) DLCheck urls.txt                            |
| 3)Version Check                                   |
|   - DLCheck -v or DLCheck -v or DLCheck -Version  |
-----------------------------------------------------""")

#--- Main ---
#Check the argument first what users want to do it
#Can call "help", "version", "URLs checker", "file checker"
if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.search('^-[vV]', sys.argv[1]):
            print("Program name: Dead-URL-Check")
            print("Version: 0.1 by Mintae Kim")
        elif re.search('^-[hH]', sys.argv[1]):
            help_dead_link_check()
        elif re.search('^--good', sys.argv[1]):
            print("Good URL Checker is activated")
            file_chekcer(sys.argv[2], "g")
        elif re.search('^--bad', sys.argv[1]):
            print("Bad URL Checker is activated")
            file_chekcer(sys.argv[2], "b")
        elif re.search('^--all', sys.argv[1]):
            print("All URL Checker is activated")
            file_chekcer(sys.argv[2], "a")
        else:
            print("URL Checker is activated")
            for argv in sys.argv:
                #check URLs which users want to check
                if re.search(regex, argv):
                    check_dead_links(argv)
                #check the file
                else:
                    file_chekcer(argv, "a")
            check_result()

    else:
        help_dead_link_check()
