#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# Author  : ok075588
# Urlpage.py

import requests
from lxml import etree
import string

class Urlpage(object):

    def __init__(self,startpage,endpage):
        self.header={'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)'}
        self.start_url='https://www.liepin.com/zhaopin/?pubTime=&ckid=2a8a1a12abcb06bc&fromSearchBtn=2&compkind=&isAnalysis=&init=-1&searchType=1&dqs=&industryType=&jobKind=&sortFlag=15&degradeFlag=0&industries=&salary=&compscale=&key=python&clean_condition=&headckid=2a8a1a12abcb06bc&d_pageSize=40&siTag=I-7rQ0e90mv8a37po7dV3Q~fA9rXquZc5IkJpXC-Ycixw&d_headId=53249f248587e759016aac73954d52ae&d_ckId=53249f248587e759016aac73954d52ae&d_sfrom=search_prime&d_curPage=0&curPage='
        self.startpage=startpage   #开始页
        self.endpage=endpage     #结束页
        self.job_lists=[]
        self.get_pages()

    #获取分页
    def get_pages(self):
        for k in range(self.startpage,self.endpage):
            page=self.start_url+str(k)      #拼接网址
            self.job_links(page,self.header)


    #分页源码
    def job_links(self,page,header):
        res=requests.get(page,header)
        html=res.text
        self.get_job_links(html)
        res.close()

    #  最终详情页面
    def get_job_links(self,html):
        response=etree.HTML(html)
        jobs_link=response.xpath('//div[@class="job-info"]/h3/a/@href')
        for job in jobs_link:
            self.job_lists.append(job)



