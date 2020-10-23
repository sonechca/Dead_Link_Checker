import sys
import DLFunctions
import re

# #Regular expression
regex = DLFunctions.regex

# #List of each links
goodLinks = DLFunctions.goodLinks
badLinks = DLFunctions.badLinks
jsonArr = DLFunctions.jsonArr
unknownLinks = DLFunctions.unknownLinks

#--- Main ---
#Check the argument first what users want to do it
#Can call "help", "version", "URLs checker", "file checker"
if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.search('^-[vV]', sys.argv[1]):
            print("Program name: Dead-URL-Check")
            print("Version: 0.1 by Mintae Kim")
        elif re.search('^-[hH]', sys.argv[1]):
            DLFunctions.help_dead_link_check()
        elif re.search('^--[jJ]', sys.argv[1]):
            print("URL JSON file is created...")
            DLFunctions.create_JSON(sys.argv[2])
            print(jsonArr)

        elif re.search('^--good', sys.argv[1]):
            print("Good URL Checker is activated")
            DLFunctions.file_chekcer(sys.argv[2], "g")
        elif re.search('^--bad', sys.argv[1]):
            print("Bad URL Checker is activated")
            DLFunctions.file_chekcer(sys.argv[2], "b")
        elif re.search('^--all', sys.argv[1]):
            print("All URL Checker is activated")
            DLFunctions.file_chekcer(sys.argv[2], "a")
        elif re.search('^--ignore', sys.argv[1]):
            DLFunctions.file_chekcer(sys.argv[3], "i")
            DLFunctions.check_result()
        else:
            print("URL Checker is activated")
            for argv in sys.argv:
                #check URLs which users want to check
                if re.search(regex, argv):
                    DLFunctions.check_dead_links(argv, "a")
                #check the file
                else:
                    DLFunctions.file_chekcer(argv, "a")
            DLFunctions.check_result()

    else:
        DLFunctions.help_dead_link_check()
