#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by liujuan on 2017/12/22
# content:
from urllib import request


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        response = request.urlopen(url)

        if response.getcode() != 200:
            return None
        return response.read()
