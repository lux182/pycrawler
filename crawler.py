#!/usr/bin/env python
#!coding=utf-8

import time
import fetcher

class Crawler:

  #启动爬虫 
  def crawl(self):
    print 'start crawling'
    #实例化多线程抓取模块，指定3个线程
    f = fetcher.Fetcher(3)
    f.start()

    while True:
      print '------------ running threads : %s ------------' % f.get_running_count()
      time.sleep(5)
