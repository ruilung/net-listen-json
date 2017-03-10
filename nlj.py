import json
import platform
import os

def get_netlisten():
    system=platform.system()
    lst=[]
    rlst=[]

    if system=='Linux':
        lst=os.popen("ss -tln | awk '{print $4}' | grep -v '^:' | awk -F: '{print $2}' | grep -v '^$'")
        for i in lst:
            str=('{"{#PORT}":"'+i+'"}').replace('\n','')
            rlst.append(str)

    if system=='Windows':
        lst=os.popen('netstat -an | find /v "[::]" | findstr LISTEN')

        for i in lst:
            j=i.split()[1]
            k=j.split(':')[1]
            rlst.append('{"{#PORT}":"'+k+'"}')
    return rlst



if __name__ == '__main__':

    print json.dumps({ "data":get_netlisten() }).replace('\\"','"').replace('"{"','{"').replace('"}"','"}')
    #print json.dumps({"data": get_netlisten()}).replace('\\"', "\"").replace('\"\"', "\"")
    #print json.dumps( get_netlisten()).replace('\\"',"\"")
    #print get_netlisten()
    #print json.dumps({"data": json.JSONDecoder().decode(get_netlisten())})


