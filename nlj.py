import json
import platform
import os
import sys

def get_netlisten():
    exclude_list=[]
    if len(sys.argv) > 1:
        for i in sys.argv[1:]:
            exclude_list.append(i.split('-'))
        #print exclude_list

    system=platform.system()
    lst=[]
    rlst=[]

    if system=='Linux':
        lst=os.popen("ss -tln | awk '{print $4}' | grep -v '^:' | awk -F: '{print $2}' | grep -v '^$'")
        for i in lst:
            str=('{"{#PORT}":"'+i+'"}').replace('\n','')
            append_flag = 1
            for e in exclude_list:
                # print e[0], e[1]
                if int(e[0]) <= int(i) <= int(e[1]):
                    append_flag = 0
            if append_flag:
                rlst.append(str)


    if system=='Windows':
        lst=os.popen('netstat -an | find /v "[::]" | findstr LISTEN')

        for i in lst:
            j=i.split()[1]
            k=j.split(':')[1]
            append_flag=1
            for e in exclude_list:
                #print e[0], e[1]
                if int(e[0]) <= int(k) <= int(e[1]):
                    append_flag=0
            if append_flag:
                rlst.append('{"{#PORT}":"'+k+'"}')

    return rlst



if __name__ == '__main__':


    print json.dumps({ "data":get_netlisten() }).replace('\\"','"').replace('"{"','{"').replace('"}"','"}')
    #print json.dumps({"data": get_netlisten()}).replace('\\"', "\"").replace('\"\"', "\"")
    #print json.dumps( get_netlisten()).replace('\\"',"\"")
    #print get_netlisten()
    #print json.dumps({"data": json.JSONDecoder().decode(get_netlisten())})


