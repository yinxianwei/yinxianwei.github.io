AUTHOR = "yinxianwei"
SITENAME = "一枝红杏出墙来"
SITEURL = ""
RELATIVE_URLS = True

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
