# feed.py

import json

def get_articles():
    # parse xml here
    titles = [ 'title 1', etc. ]
    bylines = [ 'source 1', etc. ]
    links = [ 'link 1', etc. ]
    feed_data = { 'titles': titles, 'bylines':bylines, 'links':links}
          'OR'
    feed_data = {'titles'[0]:
                             {"Title": titles[0], "text": text(links[0]) }
                }
    feed_data = json.dumps(feed_data)

    
    return feed_data



"""adapt following code to get_articles()"""
import feedparser as F 
import json

feed_list = {'BGF (full)': "http://bengreenfieldfitness.com/feed/", 
            'BGF': "http://bengreenfieldfitness.libsyn.com/rss",
            'Morning Brew Stories': "https://www.morningbrew.com/stories.rss",
            'Morning Brew Archive': "https://www.morningbrew.com/archive.rss",
            'Chris Masterjohn': "https://chrismasterjohnphd.com/feed/",
            'AI in Medicine': "http://rss.sciencedirect.com/publication/science/09333657_OA/open-access"
}

data_now = {}
data2 = {}
standard_keys = ['title', 'title_detail', 'summary', 'summary_detail', 'content', 'published', 'published_parsed', 'links', 'link', 'id', 'guidislink', 'authors', 'author', 'author_detail']
for name,site in feed_list.items():
    feed_data = F.parse(site)
    #data_now[name] = feed_data
    #data2[name] = feed_data.entries[:]
    print(f"Number of posts by {name}: {len(feed_data.entries)}")
    print(f"    keys used: {feed_data.entries[1].keys()}")
    if 'link' in feed_data.entries[1].keys():
        print(f"     link: {feed_data.entries[1]['link']}")
    print("="*20)

# with open('data_now.txt', 'w') as fd:
#     jdata = json.dumps(data_now)
#     fd.write(jdata)

# with open('data2.txt', 'w') as fd2:
#     jdata2 = json.dumps(data2)
#     fd2.write(jdata2)


# for key in entry.keys():
#     print(str(key))
#     print(entry[key])
#     print("="*20)