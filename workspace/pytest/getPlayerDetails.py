import requests, bs4
import re

def getTargetUrl(playerName):
    searchTarget = requests.get('http://search.espncricinfo.com/ci/content/site/search.html?search=' + playerName)
    searchTarget.raise_for_status()
    soup = bs4.BeautifulSoup(searchTarget.text, 'html.parser')
    
    targetUrlData = soup.select('.name > a')
    targetUrl = ""
    if len(targetUrlData) > 0:
        targetUrl = targetUrlData[0].get('href') 
        targetUrl = "http://www.espncricinfo.com" + str(targetUrl)
        print "Target URL: " + targetUrl
    return targetUrl

def getStats(targetUrl):
    # target = requests.get('http://www.espncricinfo.com/india/content/player/253802.html')
    target = requests.get(targetUrl)
    
    target.raise_for_status()
    soup = bs4.BeautifulSoup(target.text, 'html.parser')
     
    stats = soup.select('.data1')
    return stats

def getPlayerDetails(playerName):
    #playerName = "ms+dhoni"
    stats = ""
    targetUrl = getTargetUrl(playerName)
    if len(targetUrl) > 0:
        stats = getStats(targetUrl)
    return stats