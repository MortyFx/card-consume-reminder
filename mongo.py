import pymongo

class mongo:
    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        cczu_card_sms = client['cczu_card_sms']
        self.user = cczu_card_sms['user']
        self.trade_log = cczu_card_sms['trade_log']

    def find(self,collection):
        '''
        查询表中数据
        :param collection:
        :return:
        '''
        if collection == 'user':
            collection = self.user
        elif collection == 'trade_log':
            collection = self.trade_log
        return collection.find()

    def isTradeLogExisted(self,long_xh):
        '''
        用户一卡通交易记录是否已存在
        :param long_xh:
        :return:
        '''
        log_in_db = self.trade_log.find({"long_xh": long_xh})
        logs = []
        for log in log_in_db:
            logs.append(log['_id'])
        return logs

    def insertTrade(self,trade_log):
        '''
        插入交易记录
        :param trade_log:
        :return:
        '''
        self.trade_log.insert_one(trade_log)

    def updateTrade(self,trade_log):
        '''
        更新交易记录
        :param trade_log:
        :return:
        '''
        self.trade_log.save(trade_log)

    def getID(self,_id):
        '''
        通过索引_id值获得已有记录的id(刷卡次数)值
        :param _id:
        :return:
        '''
        log_in_db = self.trade_log.find({"_id": _id})
        for log in log_in_db:
            id = log['id']
        return id










