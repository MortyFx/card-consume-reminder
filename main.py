from card import card
from mongo import mongo
from sms import dayu_sms
import requests,json
from log import log

class main:
    def __init__(self):
        self.mongo = mongo() #实例化mongodb对象
        self._log = log()
        self.sms = dayu_sms(self._log) #实例化大于SMS对象
        self.s = requests.session() #创建一个requests会话
        self.card = card(self.s,self._log) #实例化card对象
        self.getUsers()  #获取数据库中用户列表

    def getUsers(self):
        '''
        获得数据库的订阅学生学号列表
        :return:
        '''
        users_in_db = self.mongo.find('user')
        users = []
        for cursor in users_in_db:
            users.append(cursor)
        self.users = users

    def run(self):
        '''
        应用运行流程：获得学生列表->循环列表->比对数据库->发送短信
        :return:
        '''
        for user in self.users:
            xh_num = str(user['xh_num'])
            phone = str(user['phone'])
            trade_log = self.card.getCardLog(xh_num)
            self._log.info('[' + xh_num + '] ' + json.dumps(trade_log)) #打印日志
            is_trade_log_existed = self.mongo.isTradeLogExisted(trade_log['long_xh'])
            if trade_log['id'] == 'null':
                pass
            else:
                if len(is_trade_log_existed) > 0:
                    id = self.mongo.getID(is_trade_log_existed[0])
                    # 判断数据是否一致  一致则pass，不一致则更新数据，并发送短信
                    if(id != trade_log['id']):
                        trade_log['_id'] = is_trade_log_existed[0]
                        self.mongo.updateTrade(trade_log)
                        self.sms.sendMessage(phone,trade_log)
                    else:
                        self. _log.info('[' + xh_num + "] Don't have change.")
                elif len(is_trade_log_existed) == 0:
                    self.mongo.insertTrade(trade_log)
                    self.sms.sendMessage(phone, trade_log)

if __name__ == '__main__':
    main = main()
    main.run()
