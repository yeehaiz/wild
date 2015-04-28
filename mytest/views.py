# coding: utf-8

from django.shortcuts import render
from django.http.response  import (
    HttpResponse, HttpResponseForbidden, HttpResponseNotAllowed,
    HttpResponseRedirect,
)

from event import models
import json
from helpers import decorators


#@decorators.login()
def test(request):


    return render(request, 'test.html', {})








def event_1(request):
    e = models.Event()

    e.title = '【星座路线】一个人，一个世界，探秘吴哥窟'
    e.type = models.EventType.objects.get(id=2)
    e.intensity = 3
    e.days = 4
    e.places = 12
    e.price = 3299

    e.covers = json.dumps(['/static/images/resource/product-1.jpg', '/static/images/resource/product-1.jpg'])
    e.outline = '自由自在，无拘无束，对外界包罗万象的事物的永无止境的好奇心，这两种自由风格结合简直就是为双子座量身定做！ 自由自在，无拘无束，对外界包罗万象的事物的永无止境的好奇心，这两种自由风格结合简直就是为双子座量身定做！'
    e.route = '上海 > 丽水 > 云和 > 武义 > 上海'
    e.planning = '''
@ 上海 > 宁国
早餐后出发，乘车沿秀美青衣江直上，穿越国内最长的公路隧道二郎山隧道，经历阴阳两重天后抵达大渡河（川西最大最深峡谷），经泸定、情歌故乡康定古城抵达老榆林，从电站开始轻装进山，到达今天的大草坝营地。

路程：车程约4小时
住宿：扎营/农家, 可选农家住宿2/4人间, 约50元/人

@ 换线盘川铁匠山
早餐后出发，乘车沿秀美青衣江直上，穿越国内最长的公路隧道二郎山隧道，经历阴阳两重天后抵达大渡河（川西最大最深峡谷），经泸定、情歌故乡康定古城抵达老榆林，从电站开始轻装进山，到达今天的大草坝营地。

路程：车程约4小时
住宿：扎营/农家, 可选农家住宿2/4人间, 约50元/人

@ 鬼斧神工仙人洞 > 上海
早餐后出发，乘车沿秀美青衣江直上，穿越国内最长的公路隧道二郎山隧道，经历阴阳两重天后抵达大渡河（川西最大最深峡谷），经泸定、情歌故乡康定古城抵达老榆林，从电站开始轻装进山，到达今天的大草坝营地。
7:00 触发的啊发生的飞飞
8:00 触发的啊发生的飞飞
<img src="http://img.qunawan.com/ecmme/wan/xl/goods/20150211/201502110919163987.jpg">

路程：车程约4小时
住宿：扎营/农家, 可选农家住宿2/4人间, 约50元/人

'''
    e.fee_desc = '''
次路线费保证成团路线, 请您付款前先资讯下我们的克服人员

费用包含
1. 交通：全程巴士，我们将根据活动人数选择合适的车型
2. 领队：资深领队全程带队
3. 向导：当地向导一名

费用不包含
1. 住宿：农家2/4人间, 预计两晚住宿100元/人
2. 其他：其他可能发生的个人消费
'''

    e.equipment = '个人餐具、65L背包、25L小包、睡袋（舒适温度5、6、10月-20℃，7、8、9-10℃）、保暖衣服（冲锋衣裤、抓绒衣裤）、速干衣裤、保暖手套、高帮徒步鞋、保温水壶、太阳镜、头灯、头巾、带沿的帽子、登山杖、唇膏、防晒霜（SPF30++以上）、垃圾袋、常备药品、个人用品（如洗漱用品、换洗衣物、袜子等） 公共装备：高原炊具、炊事帐篷、双人帐篷、对讲机、防潮垫（可自行携带，如需提供请联系客服说明）'


    e.save()
