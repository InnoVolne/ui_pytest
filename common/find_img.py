#!/usr/bin/python3
# coding=utf-8
"""
@project : ui_pytest
@Author : Sophie
@Data : 2024/1/22 20:52
"""
import aircv as ac
import cv2

from common.tools import get_project_path, sep, get_now_date_time_str
from common.report_add_img import add_img_path_to_report
class FinImg:
    def img_imread(self, img_path):
        """
        读取图片
        :param img_path:
        :return:
        """
        return ac.imread(img_path)

    def get_confidence(self, source_path, search_path):
        """
        查找图片
        :param source_path: 原图路径
        :param search_path: 需要查找的路径
        :return:
        """
        img_src = self.img_imread(source_path)
        img_sch = self.img_imread(search_path)
        result = ac.find_template(img_src, img_sch)
        cv2.rectangle(img_src, result["rectangle"][0], result["rectangle"][3], (255, 0, 0), 2)

        diff_img_path = get_project_path() + sep(["img", "diff_img". get_now_date_time_str() + "-对比的图.png"], add_sep_before=True)
        cv2.imencode(".png", img_src)[1].tofile(diff_img_path)
        add_img_path_to_report(diff_img_path, "查找的图")
        return result["confidence"]

if __name__== '__main__':
    source_path = get_project_path() + sep(["img", "source_img", "head_img.png"], add_sep_before=True)
    search_path = get_project_path() + sep(["img", "assert_img", "head_img.png"], add_sep_before=True)
    FinImg().get_confidence(source_path, search_path)
    FinImg().get_confidence(source_path, search_path)