#coding=utf-8
import feedparser
import re

def getwordCounts(url):
    d = feedparser.parse(url)
    wc = {}
    tilte = {}
    if len(d.entries) == 0:
        return tilte,wc;
    for e in d.entries:
        if 'summary' in e:
            summary = e.summary
        else:
            summary = e.description

        words = getwords(e.title+' '+summary)
        for word in words:
            wc.setdefault(word,0)
            wc[word] += 1
    tilte = d.feed.title;
    return tilte,wc

def getwords(html):
    txt = re.compile(r'<[^>]+>').sub('',html)
    words = re.compile(r'[^A-Z^a-z]+').split(txt)
    return [word.lower() for word in words if word != '']



if __name__ == '__main__':
    apcount = {}
    wordcount = {}
    feedurls = [line for line in file('feedlist.txt')]
    for feedurl in feedurls:
        tilte, wc = getwordCounts(feedurl)
        if len(wc) == 0:
            continue
        wordcount[tilte] = wc
        for word,count in wc.items():
            apcount.setdefault(word,0)
            if count > 0:
                apcount[word] += 1;

    print  apcount




