from skimage.measure import compare_ssim

from stagesep2.analyser.base import BaseAnalyser


class TrendAnalyser(BaseAnalyser):
    """ trend analyser """
    name = 'trend'
    previous_frame = None

    @classmethod
    def run(cls, frame, ssv):
        """
        return a dict, eg: {'previous': 1.0, 'first': 0.9, 'last': 0.2}

        :param frame:
        :param ssv:
        :return:
        """
        # init previous frame
        if cls.previous_frame is None:
            cls.previous_frame = frame

        # calculate sim
        previous_sim = compare_ssim(cls.previous_frame, frame)
        first_sim = compare_ssim(ssv.first_frame, frame)
        last_sim = compare_ssim(ssv.last_frame, frame)

        # update previous frame
        cls.previous_frame = frame

        result_dict = {
            'previous': previous_sim,
            'first': first_sim,
            'last': last_sim,
        }
        return result_dict

    @classmethod
    def clean(cls, *args, **kwargs):
        cls.previous_frame = None
