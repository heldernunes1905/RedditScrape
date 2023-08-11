import mechanicalsoup
from bs4 import BeautifulSoup
import requests

#takes care of the whole script
def openinfo():

    #profile url
    url = "https://www.reddit.com/r/Archero/"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")


    #find container with posts
    posts = soup.find_all("shreddit-post", {"class": "block cursor-pointer relative bg-neutral-background focus-within:bg-neutral-background-hover hover:bg-neutral-background-hover xs:rounded-[16px] p-md my-2xs nd:visible"})
    
    i=0

    #get 3 first post and print info
    while i < 3:
        tite = posts[i].find("div" , {"slot" : "title"}).get_text()#title of post
        urlpost = posts[i].find("a")['href']#url of post
        urlpost = 'https://www.reddit.com' + urlpost
        print(tite)
        print(urlpost)
        i+=1



#create object with values of ms
browser = mechanicalsoup.StatefulBrowser()


#try connecting to youtube, if successful it sends to function where it does the rest else does a very simple print
try:
    browser.open('https://www.wikipedia.org')#just to verify yt is up
    stuff = openinfo()
    #print(stuff[0]['channelname']) #print the first one with channelname 
except:
    print('Error connecting to website')

