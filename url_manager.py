#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by liujuan on 2017/12/22
# content:

class UrlManager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    # 向管理器中添加入口url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 向管理器中添加刚爬取到的新的批量url
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    # 判断管理器中是否有这个url
    def has_new_url(self):
        # 若长度不为0，就说明有代爬取的url
        return len(self.new_urls) != 0

    # 从管理器中获取一个新的带爬取的url
    def get_new_url(self):
        # 从new_urls移除 new_url
        new_url = self.new_urls.pop()
        # 将new_url添加到new_urls
        self.old_urls.add(new_url)
        return new_url


