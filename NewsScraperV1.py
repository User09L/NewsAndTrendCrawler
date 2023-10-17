#import the libraries
from requests_html import HTMLSession
session = HTMLSession()
from datetime import date

# Scrape News from trending news in Google and Bing News in the Philippine

#use session to get the page
r = session.get('https://news.google.com/home?hl=en-PH&gl=PH&ceid=PH:en')

#render the html, sleep=1 to give it a second to finish before moving on. scrolldown= how many times to page down on the browser, to get more results. 5 was a good number here
r.html.render(sleep=1, scrolldown=5)

#find all the articles by using inspect element and create blank list
articles = r.html.find('article')
newslist = []

#loop through each article to find the title and link. try and except as repeated articles from other sources have different h tags.
for item in articles:
    try:
        newsitem = item.find('h4', first=True)
        title = newsitem.text
        link = newsitem.absolute_links
        newsarticle = {
            'title': title,
        }
        newslist.append(newsarticle)
    except:
       pass


# Bing News
#use session to get the page
r2 = session.get('https://www.bing.com/news/search?q=Top+stories&nvaug=%5bNewsVertical+Category%3d%22rt_Top+stories%22%5d&FORM=HDRSC7')

#render the html, sleep=1 to give it a second to finish before moving on. scrolldown= how many times to page down on the browser, to get more results. 5 was a good number here
r2.html.render(sleep=1, scrolldown=5)

#find all the articles by using inspect element and create blank list
articles2 = r2.html.find("a.news_fbcard.wimg")
newslist2 = []

#loop through each article to find the title and link. try and except as repeated articles from other sources have different h tags.
for item in articles2:
    try:
        newsitem2 = item.find('div.na_t.news_title.ns_big', first=True)
        title = newsitem2.text
        newsarticle2 = {title}
        newslist2.append(newsarticle2)
    except:
       pass

# open file
with open("NewsScraped" + str(date.today()) + ".txt", 'w+') as f:
    # Write elements of both lists
    f.write("Top News from Google and Bing \n")  # Write "Top News" to the file
    f.write("\n")  
    for items in newslist + newslist2:
        f.write('%s\n' % items)
     
    print("File written successfully")

 
# close the file
f.close()

