import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
from pelicanconf import *

SITEURL = "https://blog.yinxianwei.com"
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

ANALYTICS = """
<script>
    var link = document.createElement('a')
    link.style.marginRight = "10px"
    link.href = "https://beian.miit.gov.cn"
    link.target = "_blank"
    link.textContent = "豫ICP备16018939号-2"
    document.querySelector('#contentinfo > p').prepend(link)
</script>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-J8HMB6HPES"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());

gtag('config', 'G-J8HMB6HPES');
</script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1314323945395441"
    crossorigin="anonymous"></script>
<script defer src="https://cloud.umami.is/script.js" data-website-id="084e9ce4-c530-4851-8c0f-c4dd40fb0655"></script>
"""
DISQUS_SITENAME = "yinxianwei"

PLUGINS = ['sitemap']

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
