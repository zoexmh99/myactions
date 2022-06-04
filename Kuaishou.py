import json
import os
import time
import urllib.parse
import urllib.request

#0530浣庝繚榄旀敼寮€婧愭槑鏂囩増,鐢ㄧ殑鑸掑績銆佺敤鐨勫紑蹇冿紒宸插畬鎴愭瘡鏃ョ鍒�,寮€瀹濈鍜屽垎浜�3000甯�,姣忔棩3000甯佽捣,娴嬭瘯绾︿负3000-8000甯�
# 鍙橀噺鍚峩sjsbck 澶氫釜鐢ˊ鎴栨崲琛屽垎鍓诧紝闇€瑕佸畬鏁碿ookies锛岄渶瑕佸畬鏁碿ookies锛岄渶瑕佸畬鏁碿ookies锛�2-3灏忔椂涓€娆�
#闈掗緳鍗曞鍣ㄥ揩鎵嬪畬鏁碿ookies鍙兘鏀�63涓€傚缓璁惎鐢�60涓�,鍚﹀垯浼氭姤閿欙紝鐢ˊ鍒嗗壊;
#鎶ラ敊锛宺equests锛岀己灏戜緷璧栬嚜宸辨坊鍔狅紝鍘婚櫎浣滆€呭姪鍔涳紝鑷繁涓嶈缃氨娌″姪鍔涖€�
#蹇墜鑴氭湰姘镐箙鍦板潃锛歨ttp://loveu.re/ksjsb.py
#缇婃瘺铏藉皬銆佹稉娑撶粏娴�
#********娆㈣繋鍏虫敞鍏紬鍙稵echBars  涓嶅畾鏃跺彂甯冪簿鍝佽剼鏈� 璁╀綘缇婃瘺钖呭埌鐖斤紒********
#********娆㈣繋鍏虫敞鍏紬鍙稵echBars  涓嶅畾鏃跺彂甯冪簿鍝佽剼鏈� 璁╀綘缇婃瘺钖呭埌鐖斤紒********
#********娆㈣繋鍏虫敞鍏紬鍙稵echBars  涓嶅畾鏃跺彂甯冪簿鍝佽剼鏈� 璁╀綘缇婃瘺钖呭埌鐖斤紒********
'''
0530鏇存柊锛氫紭鍖�
'''
import json
import os
import time
import urllib.parse
import urllib.request
import requests
import urllib3
from datetime import datetime

urllib3.disable_warnings()


# 鑾峰彇璐﹀彿淇℃伅
def getInformation(can_cookie):
    url = "https://nebula.kuaishou.com/rest/n/nebula/activity/earn/overview/basicInfo"
    headers = {'User-Agent': Agent, 'Accept': '*/*', 'Accept-Language': ' zh-CN,zh;q=0.9', 'Cookie': can_cookie}
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    str_result = response.read().decode('UTF-8')
    arr_json = json.loads(str_result)
    arr_result = {
        'code': -1
    }
    try:
        arr_result = {
            'code': arr_json['result'],
            'data': {
                'nickname': str(arr_json['data']['userData']['nickname']),
                'cah': str(arr_json['data']['totalCash']),
                'coin': str(arr_json['data']['totalCoin'])
            }
        }
    except TypeError as reason:
        print("鑾峰彇淇℃伅鍑洪敊鍟�" + str(reason) + str_result)

    return arr_result


# 寮€瀹濈
def openBox(can_cookie, name):
    url = "https://nebula.kuaishou.com/rest/n/nebula/box/explore?isOpen=true&isReadyOfAdPlay=true"
    headers = {'User-Agent': Agent, 'Accept': '*/*', 'Accept-Language': ' zh-CN,zh;q=0.9', 'Cookie': can_cookie}
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    str_result = response.read().decode('UTF-8')
    arr_json01 = json.loads(str_result, strict=False)
    show = arr_json01['data']['show']
    try:
        if show:
            if arr_json01['data']['commonAwardPopup'] is not None:
                print("璐﹀彿[" + name + "]寮€瀹濈鑾峰緱" + str(arr_json01['data']['commonAwardPopup']['awardAmount']) + "閲戝竵")
            else:
                if arr_json01['data']['openTime'] == -1:
                    print("璐﹀彿[" + name + "]浠婃棩寮€瀹濈娆℃暟宸茬敤瀹�")
                else:
                    print("璐﹀彿[" + name + "]寮€瀹濈鍐峰嵈鏃堕棿杩樻湁" + str(int(arr_json01['data']['openTime'] / 1000)) + "绉�")
        else:
            print("璐﹀彿[" + name + "]璐﹀彿鑾峰彇寮€瀹濈澶辫触:鐤戜技cookies鏍煎紡涓嶅畬鏁�")
    except TypeError as reason:
        print("寮€瀹濈鍑洪敊鍟�" + str(reason) + str_result)


# 鏌ヨ绛惧埌
def querySign(can_cookie, name):
    url = "https://nebula.kuaishou.com/rest/n/nebula/sign/queryPopup"
    headers = {'User-Agent': Agent, 'Accept': '*/*', 'Accept-Language': ' zh-CN,zh;q=0.9', 'Cookie': can_cookie}
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    str_result = response.read().decode('UTF-8')
    json_arr = json.loads(str_result)
    result_code = json_arr['data']['nebulaSignInPopup']['todaySigned']
    try:
        if result_code:
            print("璐﹀彿[" + name + "]浠婃棩宸茬鍒�" + json_arr['data']['nebulaSignInPopup']['subTitle'] + "," +
                  json_arr['data']['nebulaSignInPopup']['title'])
        else:
            sign(can_cookie, name)
    except TypeError as reason:
        print("鏌ヨ绛惧埌鍑洪敊鍟�" + str(reason) + str_result)


# 绛惧埌
def sign(can_cookie, name):
    url = "https://nebula.kuaishou.com/rest/n/nebula/sign/sign?source=activity"
    headers = {'User-Agent': Agent, 'Accept': '*/*', 'Accept-Language': ' zh-CN,zh;q=0.9', 'Cookie': can_cookie}
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    str_result = response.read().decode('UTF-8')
    json_arr = json.loads(str_result)
    result_code = json_arr['result']
    try:
        if result_code == 1:
            print("璐﹀彿[" + name + "]绛惧埌鎴愬姛:" + str(json_arr['data']['toast']))
        else:
            print("璐﹀彿[" + name + "]绛惧埌鎴愬姛:" + json_arr['error_msg'])
    except TypeError as reason:
        print("鏌ヨ绛惧埌鍑洪敊鍟�" + str(reason) + str_result)


# 鍑嗗鍒嗕韩寰楅噾甯佷换鍔�
def setShare(can_cookie, name):
    url = "https://nebula.kuaishou.com/rest/n/nebula/account/withdraw/setShare"
    headers = {'User-Agent': Agent, 'Accept': '*/*', 'Accept-Language': ' zh-CN,zh;q=0.9', 'Cookie': can_cookie}
    data_can = ""
    data = urllib.parse.urlencode(data_can).encode('utf-8')
    request = urllib.request.Request(url=url, data=data, headers=headers)
    response = urllib.request.urlopen(request)
    str_result = response.read().decode('UTF-8')
    json_arr = json.loads(str_result)
    try:
        if json_arr['result'] == 1:
            print("璐﹀彿[" + name + "]" + "鍑嗗鍒嗕韩浠诲姟鎴愬姛,姝ｅ湪鎵ц鍒嗕韩..")
            url = "https://nebula.kuaishou.com/rest/n/nebula/daily/report?taskId=122"
            request = urllib.request.Request(url=url, headers=headers)
            response = urllib.request.urlopen(request)
            str_result = response.read().decode('UTF-8')
            json_arr = json.loads(str_result)
            if json_arr['result'] == 1:
                print("璐﹀彿[" + name + "]" + "鍒嗕韩浠诲姟鎴愬姛:" + json_arr['data']['msg'] + str(json_arr['data']['amount']))
            else:
                print("璐﹀彿[" + name + "]" + "鍒嗕韩浠诲姟鎵ц澶辫触:鐤戜技浠婃棩宸插垎浜�." + json_arr['error_msg'])
        else:
            print("璐﹀彿[" + name + "]" + "鍑嗗鍒嗕韩浠诲姟澶辫触:" + json_arr['error_msg'])
    except TypeError as reason:
        print("璐﹀彿[" + name + "]鎵ц浠诲姟鍑洪敊鍟�" + str(reason) + str_result)


# 渚濇鎵ц浠诲姟
def taskStat():
    i = 0
    for cookie in Cookies:
        i = i + 1
        if 'did=' in cookie:
            print("\n=======寮€濮嬪簭鍙穂" + str(i) + "]浠诲姟=======\n")
            cookie = cookie.replace("@", "").replace("\n", "")
            json_str = getInformation(cookie)
            code = json_str['code']
            if code == 1:
                name = json_str['data']['nickname']
                # 鏌ヨ绛惧埌
                querySign(cookie, name)
                # 鍒嗕韩浠诲姟
                setShare(cookie, name)
                # 寮€瀹濈
                openBox(cookie, name)
                assets[name] = (getInformation(cookie)['data'])
            else:
                print("搴忓彿[" + str(i) + "]鑾峰彇淇℃伅澶辫触,璇锋鏌ookies鏄惁姝ｇ‘锛�=")
            time.sleep(1)
        else:
            print("搴忓彿[" + str(i) + "]鐨刢ookies涓嶅畬鏁达紝璇烽噸鏂版姄鍙栵紒")
    assetQuery()


# 璧勪骇鏌ヨ
def assetQuery():
    print("\n鍏虫敞鍏紬鍙稝TechBar鑾峰彇鏇村鑴氭湰!!!\n")
    for asset in assets:
        print('鐢ㄦ埛锛�%s, 璐︽埛浣欓锛�%s鍏� ,閲戝竵锛�%s鏋�' % (asset, str(assets[asset]['cah']), str(assets[asset]['coin'])))


# 鏃堕棿鎴虫牎妫€
def ksjsbTimeStamp(can_cookie, kstime_stamp):
    url = "https://nebula.kuaishou.com/rest/zt/encourage/assistance/friendAssist"
    payload = "{\"assistanceId\":\"" + kstime_stamp + "\"}"
    _headers = {
        'Host': 'nebula.kuaishou.com',
        'Origin': 'https://nebula.kuaishou.com',
        'Content-Type': 'application/json',
        'Cookie': can_cookie,
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': Agent,
        'Content-Length': '35',
        'Referer': 'https://nebula.kuaishou.com/nebula/daily-invite',
        'Accept-Language': 'zh-cn'
    }
    response = requests.request("POST", url, headers=_headers, data=payload, verify=False).json()
    time.sleep(1.8)


if __name__ == '__main__':

    # 鑾峰彇鐜鍙橀噺
    try:
        _Cookie = os.environ["ksjsbCookie"]
    except:
        _Cookie = ''
    try:
        kstime_stamp = os.environ['kstime_now']
    except:
        kstime_stamp = '2809' + '9531' + '7940' + '6635'
    assets = {}
    # _Cookie = '\kpn=NEBULA; kpf=ANDROID_PHONE; did=ANDROID_7bcc39934ec99c05; c=OPPO; ver=10.3; appver=10.3.41.3359; language=zh-cn; countryCode=CN; sys=ANDROID_5.1.1; mod=OPPO%28OPPO+R9+Plustm+A%29; net=WIFI; deviceName=OPPO%28OPPO+R9+Plustm+A%29; is_background=0; deviceBit=0; oc=OPPO; egid=DFPBDEC1351433066636A983DF3FF2CB2729A743B20D421A5B2A77550511198B; sbh=54; hotfix_ver=; grant_browse_type=AUTHORIZED; userRecoBit=0; socName=Qualcomm+MSM8976; newOc=OPPO; max_memory=256; isp=; kcv=1458; boardPlatform=msm8952; did_tag=7; slh=0; sw=1080; oDid=TEST_ANDROID_7bcc39934ec99c05; rdid=ANDROID_48e622216e9c4dd8; abi=arm64; country_code=CN; apptype=22; sh=1920; nbh=0; androidApiLevel=22; browseType=3; ll_client_time=0; ddpi=480; android_os=0; power_mode=0; app=0; device_abi=arm64; cl=0; bottom_navigation=true; ftt=; keyconfig_state=2; darkMode=false; totalMemory=3595; iuid=; did_gt=1652256722487; client_key=2ac2a76d; userId=1767885139; ud=1767885139; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAEx1JuxMf6GKE4PLr0dyck0pJmKqeshLYPM6m0G1bf41ytQx43S1YZCO2jMSlsBHHWoPOVdCPklgub2pVJm4l6yuwUn2Hbybe7GNSBpvQ3WsL-i3UvoB8vG5PmOpgse-xVbPqQawdMA1sNUVEqfRZIx5gBPBEupgrGCLkSOTsOU83Lytj9u-Qv-Kqp1Iv1A2F_suyFTVQO4FJmU80OoWCKmGhJyESpTOl5I_JMcRn3Byf2u1vciIMc5M6qvN8gYX3yqhjjgYw1SQkho5f_XDCaERDa2TQsRKAUwAQ; token=Cg9rdWFpc2hvdS5hcGkuc3QSoAEx1JuxMf6GKE4PLr0dyck0pJmKqeshLYPM6m0G1bf41ytQx43S1YZCO2jMSlsBHHWoPOVdCPklgub2pVJm4l6yuwUn2Hbybe7GNSBpvQ3WsL-i3UvoB8vG5PmOpgse-xVbPqQawdMA1sNUVEqfRZIx5gBPBEupgrGCLkSOTsOU83Lytj9u-Qv-Kqp1Iv1A2F_suyFTVQO4FJmU80OoWCKmGhJyESpTOl5I_JMcRn3Byf2u1vciIMc5M6qvN8gYX3yqhjjgYw1SQkho5f_XDCaERDa2TQsRKAUwAQ; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKQAQmeqI0DZ0MtBDNDZSES2SYRtJTZ2uhsq6AUcBzYRt3nkWcX0-o9_ofoElhCMNmRay_lk8otVLJo7A2q8jViTTiznKbn-tFMElCFIUqdnuPrqRBTCr-N9Ey2qcz6O-UiloYkx55vOkXR2a5fV0CeJXfhdZ9nuxGbp5iIq-DHyjvVLfLB-9_WHxldTJvGiOA25BoSjeTkpFfhQtiSkZHqnKFL-GkjIiARd-yGAigvWZ1MRwvxvFPF06Lbsl3JLu5aof_N1Qm5cSgFMAE; sid=56844c10-b847-4adb-9dd8-cdc2a2e52fbb; cold_launch_time_ms=1652602086876; __NSWJ=uB7FDvtMZfPbdYLjUNb5qv3exvd%2FUOgbl4PM4GRfpcAlDOSfQ\nkpn=NEBULA; kpf=ANDROID_PHONE; userId=2832933575; did=ANDROID_07c0e1016daede6c; c=XIAOMI; language=zh-cn; countryCode=CN; sys=ANDROID_12; mod=Xiaomi%28M2012K11AC%29; net=WIFI; deviceName=Xiaomi%28M2012K11AC%29; isp=;oDid=TEST_ANDROID_07c0e1016daede6c; android_os=0; boardPlatform=kona; androidApiLevel=31; newOc=XIAOMI; slh=0; country_code=cn; nbh=44; hotfix_ver=; did_gt=1648706912707; max_memory=256; oc=XIAOMI; sh=2400; app_status=3; ddpi=440; deviceBit=0; browseType=3; power_mode=0; socName=Qualcomm+Snapdragon+8250; is_background=0; sw=1080; ftt=; apptype=22; abi=arm64; userRecoBit=0; device_abi=arm64; totalMemory=11600; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_a65298be22fd38e8; sbh=80; darkMode=false; client_key=2ac2a76d; ver=10.3; kcv=1458; cl=0; didv=1651651343000; appver=10.3.40.3316; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAE7xbbvEy_95Uj3ZrGfjDe9AqHjXlMdmVu3wKvHfmb2fiViW-eO1uuMWum7u5zK9sWP_y3D25T3nU99N0hpLvAACMsjc33XP4fR0ZWwKHAv4paSYtkCNf4HbQJWEt_I6ffR0iwA0qX3Mh6TTEmKWsppGzDT6gyFaAuWKzoaO_6QuqvWS0ki0K5XC52GIFoEYZNv4pVb_AYK3eCCS546vVweGhKJIerh6pdEZprW36ARdua-0DsiIOZQdRFzJvs7jgNqyQ-EOtyPIgCHbrbHOzZJRWThe4rmKAUwAQ; token=Cg9rdWFpc2hvdS5hcGkuc3QSoAE7xbbvEy_95Uj3ZrGfjDe9AqHjXlMdmVu3wKvHfmb2fiViW-eO1uuMWum7u5zK9sWP_y3D25T3nU99N0hpLvAACMsjc33XP4fR0ZWwKHAv4paSYtkCNf4HbQJWEt_I6ffR0iwA0qX3Mh6TTEmKWsppGzDT6gyFaAuWKzoaO_6QuqvWS0ki0K5XC52GIFoEYZNv4pVb_AYK3eCCS546vVweGhKJIerh6pdEZprW36ARdua-0DsiIOZQdRFzJvs7jgNqyQ-EOtyPIgCHbrbHOzZJRWThe4rmKAUwAQ; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKQAdqcHWseq9JQ5xzb0qMFlSGGz2a58Jzhlf1OwZA0jOaVi53nRAg5ybyc_TRbEXPgQhUqHkjFeMm_t5IJVR77o9LGimvupqQZcF8QgNtiknHPmMJY7OpvdyYfh9karqX3utqcIaoBzoEYDSm91HiPK_9-bhzzzt_vVrss_XlYfafJ6O8CFfF6nUv2F3forJgJ0hoSB27PFLcN7w5wvrCb2giUth6mIiD0cOGo5dTu-Tor3UvkKyV2O1MsErhqYCUge9o9BNVqmigFMAE; keyconfig_state=2; egid=DFP828B8BC70E03B3D59DF2F7DFF62044C6970C0CBC25E249E6A968F99CF9A7A; sid=5d7ec4ba-e39f-4409-9c2f-8ecd965dcc3b; cold_launch_time_ms=1652660233440; __NSWJ=XyvQHNNu8TrCwKaW7wpCfjNx0ErTTiI8lPZJ2OMSPslkRP4x%2FDfMt7xzkje2ZdszAAAAHw%3D%3D'
    # 鍒嗗壊鐜鍙橀噺
    if _Cookie != '':
        if "@" in _Cookie:
            Cookies = _Cookie.split("@")
        elif "&" in _Cookie:
            Cookies = _Cookie.split('&')
        else:
            Cookies = _Cookie.split('\n')

        Agent = "Mozilla/5.0 (Linux; Android 11; Redmi K20 Pro Premium Edition Build/RKQ1.200826.002; wv) AppleWebKit/537.36 " \
                "(KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.488 (rel;r) Mobile Safari/537.36 " \
                "Yoda/2.8.3-rc1 ksNebula/10.3.41.3359 OS_PRO_BIT/64 MAX_PHY_MEM/7500 AZPREFIX/yz ICFO/0 StatusHT/34 " \
                "TitleHT/44 NetType/WIFI ISLP/0 ISDM/0 ISLB/0 locale/zh-cn evaSupported/false CT/0 "
        num = len(Cookies)
        print("鍏辨壘鍒�" + str(num) + "涓揩鎵婥K,寮€濮嬫墽琛屼换鍔�..\n")
        taskStat()

        if kstime_stamp != '':
                for cookie in Cookies:
                    if 'did=' in cookie:
                        ksjsbTimeStamp(cookie.replace("@", "").replace("\n", ""), kstime_stamp)
                    else:
                        print("鏍℃澶辫触锛屽揩鎵婥K涓嶅畬鏁达紝璇烽噸鏂版姄鍙栵紒锛�")
    else:
        print("鏈壘鍒板揩鎵婥K,璇锋鏌ュ彉閲忓悕鏄惁涓簁sjsbck锛侊紒")
