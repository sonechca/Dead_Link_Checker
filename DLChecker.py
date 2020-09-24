import re
import requests
import sys
from requests.exceptions import ConnectionError, Timeout

regex = 'https?:\/\/[=a-zA-Z0-9\_\/\?\&\.\-]+'
links = []
dead_links = []
redirect_links = []

def prGreen(skk): print("\033[92m {}\033[00m".format(skk))
def prRed(skk): print("\033[91m {}\033[00m".format(skk))
def prLightGray(skk): print("\033[90m {}\033[00m" .format(skk))

def check_dead_links(URL):
    try:
        response = requests.get(URL, timeout=1.5)
        if response.status_code == 200:
            links.append("PASSED [" + str(response.status_code) + "] " + URL + " - Good")
            prGreen(links[-1])
        elif response.status_code >= 400 and response.status_code <= 599:
            dead_links.append("FAILED [" + str(response.status_code) + "] " + URL + " - Bad")
            prRed(dead_links[-1])
        # elif response.status_code >= 300 and response.status_code < 400:
        #     link_redirects(URL)
        else:
            raise ConnectionError

    except (Timeout, ConnectionError) as e:
        prLightGray("UNKNOWN " + URL);

# def link_redirects(r_url):
#     while True:
#         yield r_url
#         res = requests.head(r_url)
#         if 300 <= res.status_code < 400:
#             r_url = res.headers['location']
#         else:
#             break

def result():
    print("\n---Checking is done")
    if(len(links) > 0):
        print("---The following links were working: ")
        for link in links:
            prGreen("\t" + link)
    if(len(dead_links) > 0):
        print("---The following links were broken: ")
        for link in dead_links:
            prRed("\t" + link)
    if(len(redirect_links) > 0):
        print("---The following links were redirected: ")
        for resp in redirect_links.history:
            print(resp.url, resp.text)


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
|   - DLCheck [File name]                           |
|   ex) DLCheck urls.txt                            |
| 3)Version Check                                   |
|   - DLCheck -v or DLCheck -v or DLCheck -Version  |
-----------------------------------------------------""")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.search('^-[vV]', sys.argv[1]):
            print("Program name: Dead-URL-Check")
            print("Version: 0.1")
        elif re.search('^-[hH]', sys.argv[1]):
            help_dead_link_check()
        else:
            print("URL Checker is activated")
            for argv in sys.argv:
                if re.search(regex, argv):
                    check_dead_links(argv)
                    result()
                else:
                    try:
                        with open(argv, 'rt') as f:
                            contentUrls = re.findall(regex, f.read())
                        for url in contentUrls:
                            check_dead_links(url)
                    except Exception as e:
                        print("Error: " + str(e))
                        help_dead_link_check()
                        break
                f.close()
                result()

    else:
        help_dead_link_check()
