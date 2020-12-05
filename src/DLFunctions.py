import re
import requests
import sys
from requests.exceptions import ConnectionError, Timeout
from colorama import init, Fore

init()

# Regular expression
regex = 'https?://[^\s<>"].[^\s<>"]+'

# List of each links
goodLinks = []
badLinks = []
jsonArr = []
unknownLinks = []

# --- functions ---
# Colour functions
def prLightGray(skk):
    print("\033[90m {}\033[00m".format(skk))


# file check function
def file_chekcer(file, flag):
    with open(file, "rt") as f:
        contentUrls = re.findall(regex, f.read())
    if flag == "g":
        for url in contentUrls:
            check_dead_links(url, flag)
    elif flag == "b":
        for url in contentUrls:
            check_dead_links(url, flag)
    elif flag == "i":
        comment = False
        if len(sys.argv) == 4:
            try:
                with open(sys.argv[2], "r") as f:
                    line = f.read()
                    if line[0] == "#":
                        comment = True
                    ignoredUrls = re.findall(regex, line)
                if len(ignoredUrls) == 0 and comment is False:
                    raise FileNotFoundError

                # Remove all ignored urls then check result
                urls = [x for x in contentUrls if x not in ignoredUrls]
                for url in urls:
                    check_dead_links(url, flag)
            except FileNotFoundError:
                print(Fore.RED + "Error: invalid text file!")
        else:
            print("Fore.RED + Error: invalid number of arguments!")
    else:
        for url in contentUrls:
            check_dead_links(url, "a")


# Dead link checker, Check the resonse status and show users that URL is dead or not
# Save in the list each URLs
# Using Request libarary
# The link which have connection error print the "Unknown URls"
def check_dead_links(URL, flag):
    try:
        response = requests.get(URL)
        if response.status_code == 200 and flag != "b":
            good_links(URL, response.status_code)
        elif (
            response.status_code >= 300
            and response.status_code < 400
            and flag != "g"
            and flag != "b"
        ):
            link_redirects(URL)
        elif (
            response.status_code >= 400 and response.status_code <= 599 and flag != "g"
        ):
            bad_links(URL, response.status_code)
        else:
            raise ConnectionError

    except (Timeout, ConnectionError):
        if flag != "g" and flag != "b":
            prLightGray("UNKNOWN " + URL)


def good_links(URL, status):
    goodLinks.append("PASSED [" + str(status) + "] " + URL + " - Good")
    print(Fore.GREEN + goodLinks[-1])


def bad_links(URL, status):
    badLinks.append("FAILED [" + str(status) + "] " + URL + " - Bad")
    print(Fore.RED + badLinks[-1])


def single_link_status_checker(url):
    request = requests.get(url)
    return request.status_code


def link_redirects(r_url):
    while True:
        yield r_url
        res = requests.head(r_url)
        if 300 <= res.status_code < 400:
            r_url = res.headers["location"]
        else:
            break


# Showing the result after checking all of the URLs in the file
def check_result():
    print(Fore.RESET + "\n------------- Checking is done ---------------")
    if goodLinks:
        print("------ The following links were working ------")
        for link in goodLinks:
            print(Fore.GREEN + "| " + link)
    if badLinks:
        print(Fore.RESET + "------ The following links were broken -------")
        for link in badLinks:
            print(Fore.RED + "| " + link)


# Help message function
# User can call this function when user do not write argument or wrtie -h or -H
def help_dead_link_check():
    print(
        Fore.GREEN
        + """
-----------------------------------------------------
|                      help                         |
-----------------------------------------------------"""
    )
    prLightGray(
        """-----------------------------------------------------
|           How to use Dead Link checker?           |
| 1)URLs Checker                                    |
|   - DLCheck [URL] [URL] ...                       |
|   ex) DLCheck youtube.ca google.ca                |
| 2)Files Checker                                   |
|   - DLCheck [File name] [File name]...            |
|   ex) DLCheck urls.txt                            |
| 3)Version Check                                   |
|   - DLCheck -v or DLCheck -v or DLCheck -Version  |
-----------------------------------------------------"""
    )


def create_JSON(file):
    with open(file, "rt") as f:
        contentUrls = re.findall(regex, f.read())
    for url in contentUrls:
        try:
            response = requests.get(url, timeout=1.5)
            jsonObj = {"url": url, "status": response.status_code}

            if response.status_code == 200:
                jsonArr.append(jsonObj)
            elif response.status_code >= 400 and response.status_code <= 599:
                jsonArr.append(jsonObj)
            else:
                raise ConnectionError

        except (Timeout, ConnectionError):
            jsonArr.append(jsonObj)


# check the lastest 10 telescope url
def telescope_url_check():
    f = open("telescope.txt", mode="wt", encoding="utf-8")
    localUrl = "http://localhost:3000/posts"
    urls = requests.get(localUrl).json()
    for url in urls:
        id = url.get("id")
        post = f"{localUrl}/{id}"
        f.write(f"{post}\n")
