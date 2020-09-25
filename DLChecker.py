import re
import requests
import sys
from requests.exceptions import ConnectionError, Timeout

#Regular expression
regex = 'https?:\/\/[=a-zA-Z0-9\_\/\?\&\.\-]+'

#List of each links
links = []
dead_links = []

# --- functions ---
#Colour functions
def prGreen(skk): print("\033[92m {}\033[00m".format(skk))
def prRed(skk): print("\033[91m {}\033[00m".format(skk))
def prLightGray(skk): print("\033[90m {}\033[00m" .format(skk))

#file check function
def file_chekcer(file):
    with open(file, 'rt') as f:
        contentUrls = re.findall(regex, f.read())
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
            prGreen(links[-1])
        elif response.status_code >= 300 and response.status_code < 400:
            link_redirects(URL)
        elif response.status_code >= 400 and response.status_code <= 599:
            dead_links.append("FAILED [" + str(response.status_code) + "] " + URL + " - Bad")
            prRed(dead_links[-1])
        else:
            raise ConnectionError

    except (Timeout, ConnectionError) as e:
        prLightGray("UNKNOWN " + URL);

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
    print("\n------------- Checking is done ---------------")
    if(len(links) > 0):
        print("------ The following links were working ------")
        for link in links:
            prGreen("| " + link)
    if(len(dead_links) > 0):
        print("------ The following links were broken -------")
        for link in dead_links:
            prRed("| " + link)

#Help message function
#User can call this function when user do not write argument or wrtie -h or -H
def help_dead_link_check():
    prGreen(
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
        else:
            print("URL Checker is activated")
            for argv in sys.argv:
                #check URLs which users want to check
                if re.search(regex, argv):
                    check_dead_links(argv)
                #check the file
                else:
                    file_chekcer(argv)
            check_result()

    else:
        help_dead_link_check()
