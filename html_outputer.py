 #!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by liujuan on 2017/12/22
# content:


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        # 写入html文件
        fout = open('output.html', 'w', encoding='utf-8')

        fout.write("<html>")
        fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            # 输出每行内容
            fout.write("<tr>")
            # 输出每个单元格的内容
            fout.write("<td>%s</td>" % data['url'])
            # 因为title的编码是assi
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()