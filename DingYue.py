
import random
import time
import requests
import re
import os

cookie = os.environ["GHCOOKIE"]
filter_list = ["#",";","","/"]

headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
        "cookie":cookie
    }
def getPage(num):
    url = "https://github.com/search?o=desc&p="+str(num)+"&q=%5Bserver_remote%5D&s=indexed&type=Code"
    resp = requests.get(url,headers=headers).text

    tt = re.compile(r'href="(.*?)\.conf"').findall(resp)

    return tt

def getServer(url_raw):
    resp = requests.get(url_raw).text

    temp = resp.split("\n")

    ans = []

    try:
        #处理远程节点
        remote_start = temp.index("[server_remote]") + 1
        while True:
            #print(temp[remote_start])
            if temp[remote_start][0]=='h':
                ans.append(temp[remote_start])
            elif temp[remote_start][0]=='[':
                break
            remote_start+=1
    except:
        pass
        #print("not found server_remote")

    try:
        #处理本地节点
        local_start = temp.index("[server_local]") + 1
        while True:
            #print(temp[local_start])
            if temp[local_start][0] in filter_list:
                pass
            elif temp[local_start][0] == '[':
                break
            else:
                ans.append(temp[local_start])
            local_start +=1
    except:
        pass
        #print("not found server_local")
    if ans!=[]:
        print(f"成功获取到=>{len(ans)}个机场订阅")
    return ans

def getAll(start,end=None):
    ans = []
    if end!=None:
        page = [i for i in range(start,end+1)]
    else:
        page = [i for i in range(1,start+1)]

    for i in page:
        temp = getPage(i)
        if temp!=[]:
            ans.extend(temp)
        print(f"查询到=>{len(temp)}个仓库，睡眠一会儿\n")
        time.sleep(random.randint(2,5))
    print(f"获取完毕，总共=>{len(ans)}个仓库")
    return ans

def startGET(start,end=None):
    ans = []

    url_temp = getAll(start,end)
    urls = []
    for i in url_temp:
        tt = "https://raw.githubusercontent.com"+str(i).replace('blob/','')+".conf"
        urls.append(tt)

    for _ in urls:
        try:
            print(f"开始爬取=>{_}仓库节点")
            temp = getServer(_)
            if temp!=[]:
                ans.extend(temp)
        except:
            print(f"{_}仓库爬取失败，原因未知")

        time.sleep(random.randint(2, 5))

    return ans


if __name__ == '__main__':

    #填一个参数就是从0开始爬虫到多少页，两个参数，是从start到end页
    temp = startGET(50)
    txt = ""
    print(temp)
    temp = list(set(temp))
    tt = []
    t1 = []
    for i in temp:
        if i[0]=='h':
            tt.append(i)
        else:
            t1.append(i)
    tr = []
    tr.extend(tt)
    tr.extend(t1)
    temp = tr
    for i in temp:
        if "网易云" in i:
            continue
        elif "免费" in i:
            continue
        txt = txt + i+"\n"
    with open("Node.txt","w+",encoding="utf-8") as f:
        f.write(txt)




