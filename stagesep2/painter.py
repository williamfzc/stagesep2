import json
from pyecharts import Line, Page

from stagesep2.logger import logger
from stagesep2.config import NormalConfig


class ReportPainter(object):
    TAG = 'Painter'

    @classmethod
    def draw_with_file(cls, file, dst):
        with open(file, encoding=NormalConfig.CHARSET) as f:
            cls.draw_with_dict(json.load(f), dst)

    @classmethod
    def draw_with_json(cls, json_str, dst):
        content = json.loads(json_str)
        cls.draw_with_dict(content, dst)

    @classmethod
    def draw_with_dict(cls, content, dst):
        # base page
        page = Page()

        # time line，直接用float作为x轴会出现 echarts 兼容问题
        time_list = [str(each['current_time']) for each in content]

        # trend
        if 'trend' in content[0]:
            trend_list = [each['trend'] for each in content]
            trend_line = cls.build_trend_line(time_list, trend_list)
            page.add(trend_line)

        # match template
        if 'match_template' in content[0]:
            match_template_list = [each['match_template'] for each in content]
            match_template_line = cls.build_match_template_line(time_list, match_template_list)
            page.add(match_template_line)

        page.render(dst)
        logger.info(cls.TAG, msg='report built finished: "{}"'.format(dst))

    @classmethod
    def build_trend_line(cls, time_list, trend_list):
        trend_line = Line('trend')
        for each_attr in ['previous', 'first', 'last']:
            each_list = [i[each_attr] for i in trend_list]
            trend_line.add(
                each_attr,
                time_list,
                each_list,
                yaxis_min='dataMin',
                is_more_utils=True,
            )
        return trend_line

    @classmethod
    def build_match_template_line(cls, time_list, match_template_list):
        match_template_dict = dict()
        for each_template in match_template_list:
            for each_name, each_value in each_template.items():
                if each_name in match_template_dict:
                    match_template_dict[each_name].append(each_value)
                else:
                    match_template_dict[each_name] = [each_value]

        match_template_line = Line('match_template')
        for each_name, each_value_list in match_template_dict.items():
            for each_attr in ['min', 'max']:
                each_list = [i[each_attr] for i in each_value_list]
                match_template_line.add(
                    '{}_{}'.format(each_name, each_attr),
                    x_axis=time_list,
                    y_axis=each_list,
                    is_more_utils=True,
                )
        return match_template_line
