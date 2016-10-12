# card-consume-reminder
某高校一卡通消费短信提醒Python脚本

使用crontab定期运行本脚本对一卡通系统的交易记录进行查询，如果存在新记录则调用阿里大于接口发送短信通知一卡通主人。

#### 环境需要

`Python3 + MongoDB`

#### 依赖库

`requests`

`BeautifulSoup4`

`lxml`

`pymongo`

#### 说明

本项目中的一卡通系统接口、登录学号与阿里大于短信接口appID等隐私信息已去除预留，以防产生安全问题。



