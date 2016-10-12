from bs4 import BeautifulSoup

class card:
    def __init__(self,ss,_log):
        self.ss = ss
        self._log = _log
        self.login()

    def login(self):
        '''
        学号登录
        :return:
        '''
        url = ''  #隐私预留
        r = self.ss.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        form_data = soup.select('#fm1 > input')
        data = {
            'lt': form_data[0].get('value'),
            'exe': form_data[1].get('value'),
            'event': form_data[2].get('value'),
            'vcode': form_data[3].get('value'),
        }
        params = {
            'username': '', #隐私预留
            'password': '', #隐私预留
            'lt': data['lt'],
            'execution': data['exe'],
            '_eventId': data['event'],
            'useVCode': data['vcode'],
        }
        r = self.ss.post(url, params=params)
        self._log.info('Login Successfully.')
    def getCardNum(self,xh_num):
        '''
        通过学号获得一卡通卡号
        :param xh_num:
        :return:
        '''
        r = self.ss.get('' + xh_num)  #隐私预留
        r = self.ss.get('') #隐私预留
        soup = BeautifulSoup(r.text, 'lxml')
        html = soup.select('td[class="neiwen"]')
        # rest = money_html[-5].get_text()
        card_num = html[3].get_text().strip()
        self.long_xh = html[8].get_text().strip()
        return card_num

    def getCardLog(self,xh_num):
        '''
        获得一卡通交易流水记录
        :return:
        '''
        card_num = self.getCardNum(xh_num)
        url1 = '' #隐私预留
        params1 = {
            'account': card_num.strip(),
            'inputObject': 'all',
            'submit': '+%C8%B7+%B6%A8+',
        }
        #date = str(time.strftime('%Y%m%d',time.localtime(time.time())))
        # params2 = {
        #     'inputStartDate': date,
        #     'inputEndDate': date,
        # }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
            'Upgrade-Insecure-Requests': '1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cache-Control': 'max-age=0'
        }
        r = self.ss.post(url1, params=params1,headers=headers)
        html = r.text
        soup = BeautifulSoup(html, 'lxml')
        #如果查不到信息则返回用户的卡号和空值的id
        try:
            trade_log = {
                'long_xh':self.long_xh,
                'time':soup.select('#tables > tr:nth-of-type(2) > td:nth-of-type(1)')[0].get_text().strip(),
                'name':soup.select('#tables > tr:nth-of-type(2) > td:nth-of-type(3)')[0].get_text().strip(),
                'place':soup.select('#tables > tr:nth-of-type(2) > td:nth-of-type(5)')[0].get_text().strip(),
                'money':soup.select('#tables > tr:nth-of-type(2) > td:nth-of-type(6)')[0].get_text().strip(),
                'rest':soup.select('#tables > tr:nth-of-type(2) > td:nth-of-type(7)')[0].get_text().strip(),
                'id':soup.select('#tables > tr:nth-of-type(2) > td:nth-of-type(8)')[0].get_text().strip()
            }
            return trade_log
        except IndexError:
            trade_log = {
                'long_xh': self.long_xh,
                'id':'null',
            }
            return trade_log