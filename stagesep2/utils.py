"""
public functions
"""
import numpy as np
import cv2
import contextlib

from stagesep2.analyser import ANALYSER_DICT


def check_analyser(analyser_list):
    """ check if analyser existed, and return list of runnable analyser """
    new_analyser_list = list()
    for each in analyser_list:
        if each not in ANALYSER_DICT:
            raise NotImplementedError('analyser {} not found'.format(each))
        new_analyser_list.append(ANALYSER_DICT[each])
    return new_analyser_list


def rotate_pic(old_pic, rotate_time):
    """ 帧逆时针旋转 90*rotate_time 度 """
    new_pic = np.rot90(old_pic, rotate_time)
    return new_pic


@contextlib.contextmanager
def video_capture(ssv):
    """ 打开视频的上下文控制 """
    video_cap = cv2.VideoCapture(ssv.video_path)
    yield video_cap
    video_cap.release()


__all__ = [
    'check_analyser',
    'rotate_pic',
    'video_capture',
]
