from skimage.measure import compare_ssim

from stagesep2.analyser.base import BaseAnalyser


class TrendAnalyser(BaseAnalyser):
    """ trend analyser """
    name = 'trend'

    @classmethod
    def run(cls, frame, ssv):
        """
        return a dict, eg: {'first': 0.9, 'last': 0.2}

        :param frame:
        :param ssv:
        :return:
        """
        first_sim = compare_ssim(ssv.first_frame, frame)
        last_sim = compare_ssim(ssv.last_frame, frame)
        result_dict = {
            'first': first_sim,
            'last': last_sim,
        }
        return result_dict
