# YahooFinance
import urllib
import re
dStr=urllib.urlopen('http//finance.com/q/cp?s=%5EDJI+Componets').read()
m=re.finadall('<td><td class=\'yfnc_tabledata1\'><b><a href=\'.*?\'>\(.*?)</a></b></td><td class=\'yfnc_tabledata1\'>(.*?)</td>.*?<b>.*?</tr>',dStr)

if m:
   print m
   print '\n'
   print len(m)
else
   print'not match'
