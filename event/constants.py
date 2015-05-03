# coding: utf-8

from helpers import utils
from datetime import date

LIST_PAGE_SIZE = 2
LIST_NAV_COUNT = 11



MONTH_NAMES = [None, '一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月']


EVENT_TYPES = [
    {
        'id': 1,
        'name': '徒步',
        'icon': "/static/images/base/hiking.png",
        'is_active': True,
    },
    {
        'id': 2,
        'name': '深度游',
        'icon': "/static/images/base/deep.png",
        'is_active': True,
    },
    {
        'id': 3,
        'name': '自驾游',
        'icon': "/static/images/base/driving.png",
        'is_active': True,
    },
    {
        'id': 4,
        'name': '摄影游',
        'icon': "/static/images/base/photo.png",
        'is_active': True,
    },
    {
        'id': 5,
        'name': '农家乐',
        'icon': "/static/images/base/leisure.png",
        'is_active': True,
    },
    {
        'id': 6,
        'name': '海岛游',
        'icon': "/static/images/base/island.png",
        'is_active': True,
    },
    {
        'id': 7,
        'name': '潜水游',
        'icon': "/static/images/base/diving.png",
        'is_active': True,
    },

]



def get_peroid_types():

    def get_festival():
        # 节日
        festivals = [
            {
                'name': '国庆节',
                'show': lambda: True,
                'where': lambda: "sess.start_dt between '%s' and '%s'" % (
                    utils.df(date(date.today().year, 10, 1)),
                    utils.df(date(date.today().year, 10, 7)),
                ),
            }
        ]

        for f in festivals:
            if f['show']():
                return f

        return {
            'name': '',
            'show': lambda: False,
            'where': lambda: None,
        }

    peroid_types = [
        {
            'id': 0,
            'name': '全部',
            'show': True,
            'where': None,
        },

        {
            'id': 1,
            'name': '一周内',
            'show': True,
            'where': "sess.start_dt between '%s' and '%s'" % (
                utils.df(utils.date_add(date.today(), 1)),
                utils.df(utils.date_add(date.today(), 7)),
            ),
        },

        {
            'id': 2,
            'name': '双休日',
            'show': True,
            'where': "weekday(sess.start_dt) in (5, 6)",
        },

        {
            'id': 3,    # 固定假日
            'name': get_festival()['name'],
            'show': get_festival()['show'](),
            'where': get_festival()['where'](),
        },

        {
            'id': 4,    # 当月
            'name': MONTH_NAMES[date.today().month],
            'show': True,
            'where': "sess.start_dt between '%s' and '%s'" % (
                utils.df(utils.month_begin_add(date.today(), 0)),
                utils.df(utils.month_end_add(date.today(), 0)),
            ),

        },

        {
            'id': 5,     # 下月
            'name': MONTH_NAMES[(date.today().month ) % 12 + 1 ],
            'show': True,
            'where': "sess.start_dt between '%s' and '%s'" % (
                utils.df(utils.month_begin_add(date.today(), 1)),
                utils.df(utils.month_end_add(date.today(), 1)),
            ),

        },

        {
            'id': 6,     # 下下月
            'name': MONTH_NAMES[(date.today().month + 1) % 12 + 1 ],
            'show': True,
            'where': "sess.start_dt between '%s' and '%s'" % (
                utils.df(utils.month_begin_add(date.today(), 2)),
                utils.df(utils.month_end_add(date.today(), 2)),
            ),
        },

        {
            'id': 7,     # 下下月以后
            'name': MONTH_NAMES[(date.today().month + 1) % 12 + 1 ] + '以后',
            'show': True,
            'where': "sess.start_dt > '%s' " % (
                utils.df(utils.month_end_add(date.today(), 2)),
            ),
        },

    ]

    return filter(lambda x: x['show'], peroid_types)
