import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
import time
import argparse

# ASCII Art
print(Fore.RED + "                              ___                        ")
print(" / ___| |__   ___  _ __ | | _| __ ) _ __ ___  __ _  ___| |__       ")  
print("| |   | '_ \ / _ \| '_ \| |/ /  _ \| '__/ _ \/ _` |/ __| '_  \    (^)--(^)")
print("| |___| | | | (_) | | | |   <| |_) | | |  __/ (_| | (__| | | |   :'  *_*  ':")
print(" \____|_| |_|\___/|_| |_|_|\_\____/|_|  \___|\__,_|\___|_| |_|    '.__u__,'")
print("----------------------------------------------------------------------------")
print("Scrape and parse breachforums.is database leak threads for keywords/strings")
print("----------------------------------------------------------------------------")                                                            


#Argument for help:
parser=argparse.ArgumentParser(
    description='''Reaches out to and queries breachforums.is for a specific search passed using -q flag.''')
parser.add_argument('-q', '--query', type=str, help="keyword for query, search is case-sensitive", required=True)
parser.add_argument('-o', '--outfile', action='store', type=argparse.FileType('w'), dest='output', help="Directs the output to a name of your choice", required=True)
args=vars(parser.parse_args())


#Prompt for keyword
keyword = args['query']
output_file = args['output']

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

for i in range(1,50):
    #GET request for URL
    URL = "https://breachforums.is/Forum-Databases?page=" + str(i)
    print(Fore.WHITE + "Querying page " + str(i) + "...")
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    text = soup.text
    for line in text.splitlines():
        if keyword in line:
            print(Fore.RED + "Possible database entry found on page " + str(i) + ": " + line)
            output_file.write("- Possible database entry found on page " + str(i) + ": " + line)
            formattedline = line.replace(" ", '-')
            formattedline2 = formattedline.replace(".", "-")
            print("--> URL to database leak: https://breachforums.is/Thread-"+ formattedline2)
            output_file.write("\n  --> URL to database leak: https://breachforums.is/Thread-"+ formattedline2)
            
