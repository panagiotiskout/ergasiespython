import urllib
import json
import datetime

cur_date=datetime.datetime.now()

def compare_lists(l1,l2):
    s=0
    for i in l1:
        if i in l2:
            s+=1
    return s
mynums=[4,7,19,22,39,77]
for i in range(31):
    cur_date= cur_date - datetime.timedelta(days=1)
    date_str= cur_date.strftime("%d-%m-%Y")
    url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
    print(url)
    req = urllib.Request(url)
    response = urllib.urlopen(req)
    data = response.read()
    data=json.loads(data)
    klhrwseis= data['draws']['draw']
    r=[]
    for k in klhrwseis:
        tmp=k["results"]
        r.append(compare_lists(mynums,tmp))
    print( "apotelesmata",date_str)
    print (min(r),r.count(min(r)))
    print (max(r),r.count(max(r)))
    print (10*"-")
