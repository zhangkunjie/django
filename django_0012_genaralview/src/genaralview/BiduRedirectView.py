from _ast import Str
from django.views.generic.base import RedirectView

class BaiduRedirectView(RedirectView):
    url = 'http://www.baidu.com' # 要跳转的网址，
    # url 可以不给，用 pattern_name 和 get_redirect_url() 函数 来解析到要跳转的网址
    permanent = False #是否为永久重定向, 默认为 True
    query_string = True # 是否传递GET的参数到跳转网址，True时会传递，默认为 False
    pattern_name = 'about' # 用来跳转的 URL, 看下面的 get_redirect_url() 函数
     
    # 如果url没有设定，此函数就会尝试用pattern_name和从网址中捕捉的参数来获取对应网址
    # 即 reverse(pattern_name, args) 得到相应的网址，
    # 在这个例子中是一个文章的点击数链接，点击后文章浏览次数加1，再跳转到真正的文章页面
    def get_redirect_url(self, *args, **kwargs):
        #If url is not set, get_redirect_url() tries to reverse the pattern_name using what was captured in the URL (both named and unnamed groups are used).
        return super(BaiduRedirectView, self).get_redirect_url(*args, **kwargs)