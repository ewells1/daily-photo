import requests
import bs4

captions = []

def main():
    currentDay = requests.get('http://binghamton.edu/photos/')
    soup = bs4.BeautifulSoup(currentDay.text)
    #caption = soup.select(".caption")[1].p
    caption = soup.find('p').contents[0]
    print (caption) # debug

    while caption not in captions:
        captions.append(caption)
        nextLink = soup.select('a[href^="http://www.binghamton.edu/photos/index.php/gallery/archives/"]')[0].attrs.get('href')
        print (nextLink) # debug
        currentDay = requests.get(nextLink)
        soup = bs4.BeautifulSoup(currentDay.text)
        #caption = soup.select(".caption")[1].p
        caption = soup.find('p').contents[0]
        print (caption) # debug

main()
