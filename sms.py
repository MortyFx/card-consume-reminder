from alidayu import AlibabaAliqinFcSmsNumSendRequest
import json

class dayu_sms:
    def __init__(self,_log):
        self._log = _log

    def sendMessage(self,phone,data):
        url = 'http://gw.api.taobao.com/router/rest'
        appkey = '' #隐私预留
        secret = '' #隐私预留
        req = AlibabaAliqinFcSmsNumSendRequest(appkey, secret, url)
        req.extend = "123"
        req.sms_type = "normal"
        req.sms_free_sign_name = "" #隐私预留
        if len(data['place']) > 8:
            data['place'] = data['place'][-8:]
        params = {
            'n':data['name'],
            't':data['time'][-8:],
            'm':data['money']+'元',
            'r':data['rest']+'元',
            'p':data['place'],

        }
        req.sms_param = json.dumps(params,ensure_ascii=False)
        req.rec_num = phone
        req.sms_template_code = "" #隐私预留
        try:
            resp = req.getResponse()
            self._log.info(resp)
        except Exception as e:
            self._log.warning(resp)
