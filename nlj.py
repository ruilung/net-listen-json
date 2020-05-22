import json
import platform
import os
import sys

def get_netlisten():
    system = platform.system()
    exclude_list = []
    if len(sys.argv) > 1:
        for i in sys.argv[1:]:
            exclude_list.append(i.split('-'))
    # print exclude_list

    ipv4_listen_portlist = []
    ipv6_listen_portlist = []
    resultlist = []

    if system == 'Linux':
        ipv4_listen_portlist = list(os.popen(" ss -Htln4 | awk '{print $4}' | awk -F: '{print $2}'    | grep -v '^$' "))
        ipv6_listen_portlist = list(os.popen(" ss -Htln6 | awk '{print $4}' | awk -F']:' '{print $2}' | grep -v '^$' "))

        for i in set(ipv4_listen_portlist + ipv6_listen_portlist):
            str = ('{"{#PORT}":"' + i + '"}').replace('\n', '')
            append_flag = 1
            for e in exclude_list:
                if int(e[0]) <= int(i) <= int(e[1]):
                    append_flag = 0

            if append_flag:
                resultlist.append(str)

    if system=='Windows':
        ipv4_listen_portlist=os.popen('netstat -an | find /v "[::]" | findstr LISTEN')

        for i in ipv4_listen_portlist:
            j=i.split()[1]
            k=j.split(':')[1]
            append_flag=1
            for e in exclude_list:
                #print e[0], e[1]
                if int(e[0]) <= int(k) <= int(e[1]):
                    append_flag=0
            if append_flag:
                resultlist.append('{"{#PORT}":"'+k+'"}')

    return resultlist



if __name__ == '__main__':


    print(json.dumps({ "data":get_netlisten() }).replace('\\"','"').replace('"{"','{"').replace('"}"','"}'))
