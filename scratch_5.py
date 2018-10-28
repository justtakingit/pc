#coding:utf-8
import re
import requests
ss={'http://cs.whu.edu.cn/news_list.aspx?category_id=54','http://cs.whu.edu.cn/news_list.aspx?category_id=54&page=2','http://cs.whu.edu.cn/news_list.aspx?category_id=54&page=3','http://cs.whu.edu.cn/news_list.aspx?category_id=54&page=4','http://cs.whu.edu.cn/news_list.aspx?category_id=54&page=5','http://cs.whu.edu.cn/news_list.aspx?category_id=54&page=6','http://cs.whu.edu.cn/news_list.aspx?category_id=54&page=7','http://cs.whu.edu.cn/news_list.aspx?category_id=54&page=8','http://cs.whu.edu.cn/news_list.aspx?category_id=54&page=9','http://cs.whu.edu.cn/news_list.aspx?category_id=54&page=10','http://cs.whu.edu.cn/news_list.aspx?category_id=54&page=11','http://cs.whu.edu.cn/news_list.aspx?category_id=54&page=12',}
def get_html(url):
    html=requests.get(url)
    html.encoding='utf-8'
    return html
for s in ss:
    html=get_html(s)
    links=re.findall('<a href="/news_show.aspx\?id=(.*?)">',html.text,re.S)
    for link in links:
        urls='http://cs.whu.edu.cn/news_show.aspx?id='+link,
        for url in urls:
            html = get_html(url)
            times = re.findall('iconfont icon-date"></i>(.*?)</span>', html.text, re.S)
            titles = re.findall('sp1">(.*?)</div>', html.text, re.S)
            articles = re.findall('仿*宋体*">(.*?)</span>', html.text, re.S)
            info={'times':times,'titles':titles,'articles':articles}
            print(times,titles,url)

