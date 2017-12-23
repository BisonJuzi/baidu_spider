#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by liujuan on 2017/12/22
# content:

# 爬虫总调度
# 会以一个入口的url来爬取页面
# spider_main (爬虫总调度程序) url_manager(url管理器)  html_downloader(下载器)
# html_parser(html解析器)  html_outputer(将数据处理好的数据写出到 html 的页面)

import url_manager, html_downloader, html_parser, html_parser, html_outputer



class SpiderMain(object):
    # 初始化了4个对象
    def __init__(self):
        # urls 作为管理器
        self.urls = url_manager.UrlManager()
        # downloader作为下载器
        self.downloader = html_downloader.HtmlDownloader()
        # parser作为解析器
        self.parser = html_parser.HtmlParser()
        # outputer 将数据处理好的数据写出到 html 的页面
        self.outputer = html_outputer.HtmlOutputer()

    # 爬虫调度程序
    def craw(self, root_url):
        count = 1  # 当前爬取url
        # 添加入口url（单个）
        self.urls.add_new_url(root_url)

        # 爬虫循环：爬取所有相关页面
        while self.urls.has_new_url():
            try:
                # 当有带爬取的url时，从urls获取行的url
                new_url = self.urls.get_new_url()
                print('craw %s : %s' % (count, new_url))
                # 利用下载器下载url页面
                html_cont = self.downloader.download(new_url)
                # 利用解析器解析下载页面，得到新的url列表和数据，参数：当前爬取的url、下载好的url数据
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 将爬取到的批量new_urls 补充到 url 管理器
                self.urls.add_new_urls(new_urls)
                # 收集数据
                self.outputer.collect_data(new_data)

                if count == 100:
                    break
                count += 1
            except Exception as e:
                print('craw failed-- %s ' % e)

        # 输出收集好的数据
        self.outputer.output_html()


# 编写main函数
if __name__ == '__main__':
    # 设置要爬取的入口url
    root_url = "https://baike.baidu.com/item/Python/407313"
    # 创建一个spider
    obj_spider = SpiderMain()
    # 调用spider.craw方法来启动爬虫
    obj_spider.craw(root_url)

