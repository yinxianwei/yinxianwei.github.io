AUTHOR = "yinxianwei"
SITENAME = "一枝红杏出墙来"
SITEURL = "https://blog.yinxianwei.com"
# RELATIVE_URLS = True

PATH = "content"

TIMEZONE = "Asia/Shanghai"

DEFAULT_LANG = "zh-CN"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (("Pelican", "https://getpelican.com/"),)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10
STATIC_PATHS = ["media", "extra"]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/ads.txt": {"path": "ads.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/custom.css": {"path": "custom.css"},
}
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
GITHUB_URL = "https://github.com/yinxianwei"
DEFAULT_CATEGORY = "随笔"
# 隐藏分类
DISPLAY_CATEGORIES_ON_MENU = False
THEME_TEMPLATES_OVERRIDES = ["templates"]
STYLESHEET_URL = "/custom.css"
MENUITEMS = [
    ("首页", "/"),
    ("分类", "/categories.html"),
    ("标签", "/tags.html"),
    ("归档", "/archives.html"),
]
DISQUS_SITENAME = "yinxianwei"
