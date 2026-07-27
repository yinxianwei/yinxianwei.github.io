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
<script defer src="https://cloud.umami.is/script.js" data-website-id="084e9ce4-c530-4851-8c0f-c4dd40fb0655"></script>
<script type="text/javascript" src="//cpro.baidustatic.com/cpro/ui/cm.js" async="async" defer="defer" >
</script>
"""
DISQUS_SITENAME = "yinxianwei"

PLUGINS = ['sitemap']

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
