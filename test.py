# -*- coding: utf-8 -*-
import time
import math
import unittest
from unittest import TestCase
import config
from core.baiduzhidao import search_result_number
from core.nearby import calculate_relation
import operator

def test_txt_load(filename=config.txt_data_fname):
    f = open(filename, "r")
    ret =  []
    for kase in f.readlines():
        text_list = kase.split()
        ret.append((text_list[0], text_list[1:]))
    f.close()
    return ret
def test_txt_append(question, answer, filename = config.txt_data_fname):
    f = open(filename, "a")
    f.write('\t'.join([question] + answer))
    f.write("\n")
    f.close()
# class OcrTestCase(TestCase):
#     """unittest"""
#
#     def test_baidu_ocr(self):
#         """
#         test baidu ocr
#
#         :return:
#         """
#         from core.ocr.baiduocr import get_text_from_image
#
#         print("test baidu ocr")
#         app_id = "10661627"
#         app_key = "h5xcL0m4TB8fiiFWoysn7uxt"
#         app_secret = "HGA1cgXzz80douKQUpII7K77TYWSGcfW"
#
#         with open("screenshots/text_area.png", "rb") as fp:
#             message = get_text_from_image(fp.read(), app_id, app_key, app_secret, 5)
#             print(message)
#
#     def test_search_result_number(self):
#         print(search_result_number("唐朝"))

class ProblemTestCase(TestCase):
    """manually type problems to optimize AI."""
    def test_previous_problem(self):
        start = time.time()
        case_list = test_txt_load()
        for question, answers in case_list:
            print("-" * 50)
            print("Q: ", question)
            print("-" * 50)
            print("\n".join(answers))
            print("-" * 50, "\n" * 2)
            weight_li, final, index = calculate_relation(question, answers)
            summary = {
                a: b
                for a, b in
                zip(answers, weight_li)
            }
            is_face = True
            if question.find('错误') != -1 or question.find('不') != -1:
                is_face = False
            summary_li = sorted(summary.items(), key=operator.itemgetter(1), reverse=is_face)
            print("-" * 50)
            print("\n".join([a + ":" + str(b) for a, b in summary_li]))
            print("*" * 50)
            print(summary_li[0][0])
            end = time.time()
            print("use {0} 秒".format(end - start))
    def test_problem(self):
        """
        :return:
        """


        start = time.time()
        question = input("Q: ")
        answers = []
        for i in range(3):
            answers.append(input("Answer"+ str(i) + ": "))
        print("-" * 50)
        print("Q: ", question)
        print("-" * 50)
        print("\n".join(answers))
        print("-" * 50, "\n" * 2)
        weight_li, final, index = calculate_relation(question, answers)
        summary = {
            a: b
            for a, b in
            zip(answers, weight_li)
        }
        summary_li = sorted(summary.items(), key=operator.itemgetter(1))
        print("-" * 50)
        print("\n".join([a + ":" + str(b) for a, b in summary_li]))
        print("*" * 50)
        if math.log(summary_li[1][1]) - math.log(summary_li[0][1]) < math.log(summary_li[2][1]) - math.log(summary_li[1][1]):
            print(summary_li[2][0])
        else:
            print(summary_li[0][0])

        end = time.time()
        print("use {0} 秒".format(end - start))
        test_txt_append(question, answers)

if __name__ == "__main__":
    unittest.main()