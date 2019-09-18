import requests, sys, webbrowser, bs4

#request : to download the webpage
#sys : to get the command line arguments
#webbrowser : to open the perticular link using the Web Browser of your PC
#bs4 : to get the HTML of the downloaded web page

print("Googling...")  #print this while the process is going on

res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))   #search with command line arguments and download the web page

res.raise_for_status()  #check the status of the 'res'

soup = bs4.BeautifulSoup(res.text, 'html.parser')   #get the html of the web page

linkElems = soup.select('div#main > div > div > div > a')   #select the relevent html items using the Selector

numOpen = min(2, len(linkElems))   #get the first two links from the list

for i in range(numOpen):  #open the first two links using the browser
    webbrowser.open('http://google.com' + linkElems[i].get('href'))



