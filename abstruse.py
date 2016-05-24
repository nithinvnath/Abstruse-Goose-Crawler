from bs4 import BeautifulSoup
import urllib
import urllib2
import time

base_url='http://abstrusegoose.com/'
for x in xrange(1,572):
    cur_url = base_url+str(x)
    print "\n\nParsing "+cur_url+"...\n"
    r = urllib2.urlopen(cur_url).read()
    soup = BeautifulSoup(r)
    try:
        title = soup.body.section.h1.a.contents[0]
        file_extension = soup.body.section.img['src'][-4:]
        try:
            title_text = soup.body.section.img['title']
            break
        except Exception, e:
            print cur_url+' has no title text'
            title_text = 'N/A'
        try:
            blog_text = soup.body.section.div.p.contents[0]
            break
        except Exception, e:
            print cur_url+' has no blog_text'
            blog_text = 'N/A'
        urllib.urlretrieve(soup.body.section.img['src'], str(x)+file_extension)
        fo = open(str(x)+'.txt',"wb")
        fo.write("Title: " + title+ "\nCaption: "+ title_text+"\nBlog text: "+blog_text)
        fo.close()
        print "Parsing complete\n"
    except Exception, e:
        print "Page does not exist\n"
    time.sleep(2)
print "ALL DONE :)"