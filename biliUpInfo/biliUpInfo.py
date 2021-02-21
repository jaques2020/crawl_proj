import requests,json,re
from tools.myUAPool import myUArandom
import datetime



class biliUpInfo(object):
    """
    实现搜索up主信息
    """


    def __init__(self,up):
        
        self.up = up
        self.urlForUp = 'https://search.bilibili.com/upuser?keyword=%s'%up
        self._headers = {'user-agent': myUArandom()}

    @staticmethod
    def hot_word():
        hotWords_api = 'https://s.search.bilibili.com/main/hotword?mid=&buvid=44B5712D-ECA5-418A-88E9-14792952AA8C143109infoc&jsonp=jsonp'
        hotWords_resp = requests.get(url=hotWords_api,headers={'user-agent': myUArandom()}).text
        res = json.loads(hotWords_resp)
        filter_kw = lambda x:x['keyword']
        kw_val = map(filter_kw,res['list'])
        print('''当前日期:{}   
        B站热搜关键字排名'''.format(datetime.datetime.now()))
        for index,value in enumerate(kw_val):
            print(index+1,value)


    def up_search(self):
        search_res = requests.get(url=self.urlForUp,headers=self._headers).text
        regexp1 = re.compile(r'"result":(.*),"noMore"')
        re_res = re.findall(regexp1,search_res)[0]
        res = re_res.split('[',1)[-1][:-1]
        mid_res = re.findall(r'"mid":(\d{1,})',res)
        uname_res = re.findall(r'"uname":"([\u4e00-\u9fa5-の゛\d\w]+)",',res)
        fans_res = re.findall(r'"fans":(\d{1,})', res)
        video_res = re.findall(r'"videos":(\d{1,})', res)
        for i in range(len(mid_res)):
            u_info = {}
            u_info['用户名'] = uname_res[i]
            u_info['mid'] = mid_res[i]
            u_info['粉丝数'] = fans_res[i]
            u_info['投稿数'] = video_res[i]
            print(u_info)






if __name__ == '__main__':

    a = biliUpInfo('阿巴')
    a.up_search()
    # a.hot_word()