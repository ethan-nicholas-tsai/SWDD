#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 15:42
# @Author  : cendeavor
# @Site    : 
# @File    : utils.py
# @Software: PyCharm


import calendar
import sys
from lxml import etree
from bs4 import BeautifulSoup


class WeiboText:

    def __init__(self):
        from weibo_preprocess_toolkit import WeiboPreprocess
        from harvesttext import HarvestText
        import pyhanlp
        import re
        self.preprocess = WeiboPreprocess()
        self.ht = HarvestText()
        self.CharTable = pyhanlp.JClass('com.hankcs.hanlp.dictionary.other.CharTable')
        self.d1 = re.compile(r"（.*）")
        self.d2 = re.compile(r"点击播放")  # 点击播放>>
        self.d3 = re.compile(r"在.*获取更多信息")
        self.d4 = re.compile(r"速围观")
        self.d5 = re.compile(r"我获得了.*的红包")
        self.d6 = re.compile(r"#.*#")

    def get_cleaned_text(self, html):
        soup = BeautifulSoup(html, features="lxml")
        tmp_a = [i.extract() for i in soup.find_all('a')]
        # 保留图片表情文本（但是一些表情比如微笑可能有反讽意味）
        # for i in soup.find_all('span', class_='url-icon'):
        #     i.append(i.img.attrs['alt'])
        # return soup.get_text().lower().strip()
        text = soup.get_text()
        text = self.d1.sub("", text)
        text = self.d2.sub("", text)
        text = self.d3.sub("", text)
        text = self.d4.sub("", text)
        text = self.d5.sub("", text)
        text = self.d6.sub("", text)
        # 使用HarvestText清洗文本（空格压缩，去字符表情）
        content = self.CharTable.convert(text)
        cleaned_text = self.ht.clean_text(content, weibo_topic=True)
        # 使用weibo_preprocess_toolkit清洗文本（繁简体转化，去固定噪音，去数字，）
        cleaned_text = self.preprocess.clean(cleaned_text)
        return cleaned_text.strip()

    @staticmethod
    def get_raw_text(text_body):
        return etree.HTML(text_body).xpath('string(.)')

    @staticmethod
    def get_post_time(timestr="Mon Dec 14 11:26:56 +0800 2020"):
        if not timestr: return ""
        temp = timestr.split(" ")
        time_area = temp[-2]
        if time_area != '+0800':
            print(time_area)
        # day_time = ':'.join(temp[3].split(':')[:-1])
        day_time = temp[3]
        return temp[-1] + "-" + "{:0=2}".format(list(calendar.month_abbr).index(temp[1])) + "-" + temp[2] + " " + day_time

    @staticmethod
    def get_pics(weibo_info):
        """获取微博原始图片url"""
        if weibo_info.get('pics'):
            pic_info = weibo_info['pics']
            pic_list = [pic['large']['url'] for pic in pic_info]
            pics = ','.join(pic_list)
        else:
            pics = ''
        return pics

    @staticmethod
    def get_location(selector):
        """获取微博发布位置"""
        try:
            location_icon = 'timeline_card_small_location_default.png'
            span_list = selector.xpath('//span')
            location = ''
            for i, span in enumerate(span_list):
                if span.xpath('img/@src'):
                    if location_icon in span.xpath('img/@src')[0]:
                        location = span_list[i + 1].xpath('string(.)')
                        break
            return location
        except Exception as e:
            return ''

    @staticmethod
    def get_article_url(selector):
        """获取微博中头条文章的url"""
        try:
            article_url = ''
            text = selector.xpath('string(.)')
            if text.startswith(u'发布了头条文章'):
                url = selector.xpath('//a/@data-url')
                if url and url[0].startswith('http://t.cn'):
                    article_url = url[0]
            return article_url
        except Exception as e:
            return ''

    @staticmethod
    def get_topics(selector):
        """获取参与的微博话题"""
        try:
            span_list = selector.xpath("//span[@class='surl-text']")
            topics = ''
            topic_list = []
            for span in span_list:
                text = span.xpath('string(.)')
                if len(text) > 2 and text[0] == '#' and text[-1] == '#':
                    topic_list.append(text[1:-1])
            if topic_list:
                topics = ','.join(topic_list)
            return topics
        except Exception as e:
            return ''

    @staticmethod
    def get_at_users(selector):
        """获取@用户"""
        try:
            a_list = selector.xpath('//a')
            at_users = ''
            at_list = []
            for a in a_list:
                if '@' + a.xpath('@href')[0][3:] == a.xpath('string(.)'):
                    at_list.append(a.xpath('string(.)')[1:])
            if at_list:
                at_users = ','.join(at_list)
            return at_users
        except Exception as e:
            return ''



    @staticmethod
    def standardize_info(weibo):
        """标准化信息，去除乱码"""
        for k, v in weibo.items():
            if 'bool' not in str(type(v)) and 'int' not in str(
                    type(v)) and 'list' not in str(
                type(v)) and 'long' not in str(type(v)):
                weibo[k] = v.replace(u'\u200b', '').encode(
                    sys.stdout.encoding, 'ignore').decode(sys.stdout.encoding)
        return weibo
