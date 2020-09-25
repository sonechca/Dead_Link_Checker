# Dead_Link_Checker
## RELEASES
### [Dead Link Checker (Release 0.1)](https://github.com/sonechca/Dead_Link_Checker)
<p align="center">
  <img src="./venv/img/DLC1.png" alt="DLChecker" width="738">
</p>

## About DLChecker
This repository is a command-line tool to find and report a dead URL status in a file. This tool can help users to check broken link and show them list of broken link

### Features
 - Searching for the URLs in the input file
 - Checking multiple URLs by typing URL in the command line
 - Organizing links each working and broken URLs
 - Providing [Help] option to show users how to use this tool
 - Providing version of this tool
 - Printing good status[200] URLs with green colour and bad status[400,404] URLs with red colour
 - Printing unknown URLs with gray colour which have error or long loading by using timeout 

## Getting Started
 
  1. Clone the repo
  
  ```bash
  git clone https://github.com/sonechca/Dead_Link_Checker.git
  ```
  
  2. the DLChecker file in DEAD_LINK_CHECKER folder on command line
  
  ```bash
  cd DEAD_LINK_CHECKER
  ```
  3. DLChecker run command
  ```bash
  python3 DLChecker.py <filename> or <URL>
  ```
## Help/Usage
 Users can call help/usage box if they do not know how to use this tool
 ```bash
 python3 DLChecker.py or python3 DLChecker.py -h/-H
 ```
