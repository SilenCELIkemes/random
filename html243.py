import re
import urllib
url='http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html'
page=urllib.urlopen(url)
paged=page.read()
reg=r'<a title="" target="_blank" href="(http://blog.sina.com.cn/s/blog.+?.html)">'
regs=re.compile(reg)
html=re.findall(regs,paged)
print html
f=1
for test in html:
    urllib.urlretrieve(test,str(f)+'.html')#Ò²¿ÉÐ´×÷'%s .html' % x
    f+=1
