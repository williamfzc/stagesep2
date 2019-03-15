import json
from pyecharts import Line, Page

from stagesep2.logger import logger
from stagesep2.config import NormalConfig


# 如果后续图表需要更加复杂，这个部分最好用类似pandas的库进行比较规范的数据格式处理。只是简单展示就不用了
class ReportPainter(object):
    TAG = 'Painter'

    @classmethod
    def draw_with_file(cls, file_path: str, dst_path: str):
        """ draw with json file path, and export to dst path """
        with open(file_path, encoding=NormalConfig.CHARSET) as f:
            cls.draw(json.load(f), dst_path)

    @classmethod
    def draw_with_json(cls, json_str: str, dst_path: str):
        """ draw with raw json content, and export to dst path """
        content = json.loads(json_str)
        cls.draw(content, dst_path)

    @classmethod
    def draw(cls, content: list, dst_path: str):
        # base page
        page = Page()

        # time line，直接用float作为x轴会出现 echarts 兼容问题
        time_list = [str(each['current_time']) for each in content]

        # 目前只支持 match_template 与 trend 的图表绘制
        draw_type_dict = {
            'match_template': cls.build_match_template_line,
            'trend': cls.build_trend_line,
        }
        for each_type, each_func in draw_type_dict.items():
            # 以第一项为例检验是否包含该类分析结果
            if each_type not in content[0]:
                continue

            data_list = [each_data[each_type] for each_data in content]
            data_line = draw_type_dict[each_type](time_list, data_list)
            page.add(data_line)

        page.render(dst_path)
        logger.info(cls.TAG, msg='report built finished: "{}"'.format(dst_path))

    @classmethod
    def build_trend_line(cls, time_list: list, trend_list: list):
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
    def build_match_template_line(cls, time_list: list, match_template_list: list):
        """

        :param time_list:
        :param match_template_list:

            looks like:

            [
                {
                    "pic1": {
                        "min": -0.4684264361858368,
                        "max": 0.6224471926689148
                    },
                    "pic2": {
                        "min": -0.4022962152957916,
                        "max": 0.7294253706932068
                    },
                    "pic3": {
                        "min": -0.6132965087890625,
                        "max": 0.7038567066192627
                    }
                }

                ...
            ]

        :return:
        """

        # build data structure for drawing
        data_to_draw = {
            name: list()
            for name in match_template_list[0].keys()
        }

        for each_name in data_to_draw.keys():
            # draw only max values
            data_to_draw[each_name] = [i[each_name]['max'] for i in match_template_list]

        match_template_line = Line('match_template')
        for each_name, each_data in data_to_draw.items():
            match_template_line.add(
                each_name,
                x_axis=time_list,
                y_axis=each_data,
                is_more_utils=True,
            )

        return match_template_line
