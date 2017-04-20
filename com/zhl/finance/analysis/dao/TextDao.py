# -*- coding: utf-8 -*-

import MySQLdb


class text_retrive(object):
    def __init__(self):
        self.conn = MySQLdb.connect("10.3.2.33", "hlzou", "zhl123456", "fltreportdb2", charset="utf8")

    def get_by_sql(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()


if __name__ == '__main__':
    tr = text_retrive()
    res = tr.get_by_sql("select report_title from sina_comment limit 1")
    print res[0][0]
