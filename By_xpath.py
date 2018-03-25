#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# Author  : ok075588
# By_xpath.py

from Urlpage import Urlpage
import requests
from lxml import etree
import string

class By_xpath(Urlpage):

    def __init__(self,startpage,endpage):
        super(By_xpath,self).__init__(startpage,endpage)
        self.header={'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)'}
        self.wait_write_lists=[]   #储存工作名称，公司名称，薪资等详情
        self.create_lists_waitforwrite()

    def create_lists_waitforwrite(self):
        for job in self.job_lists:
            if 'https://www.liepin.com' in job:    #拼接完整链址
                res=requests.get(job,self.header)
            else:
                res=requests.get('https://www.liepin.com{}'.format(job),self.header)
            html=res.text
            res.close()
            selectors=etree.HTML(html)
            try:
                '''
                职位名称
                公司名称
                薪资
                学历
                地区
                职位描述
                '''
                job_name=selectors.xpath('//h1/@title')
                job_company=selectors.xpath('//a[@data-promid=""]/text()[normalize-space()]')
                job_salary=selectors.xpath('//p[@class="job-item-title"]/text()')
                job_edu=selectors.xpath('//div[@class="job-qualifications"]//span//text()')
                job_area=selectors.xpath('//p[@class="basic-infor"]/span/a/text()[normalize-space()]')
                job_detail=selectors.xpath('//div[@class="content content-word"]')[0].xpath('string(.)')

                job_name=job_name[0] if len(job_name)>0 else 'Null'
                job_company=job_company[0] if len(job_company)>0 else 'Null'
                job_salary=job_salary[0].replace('\r\n','').strip() if len(job_salary)>0 else 'Null'
                job_edu=job_edu[0] if len(job_edu)>0 else 'Null'
                job_area=job_area[0] if len(job_area)>0 else 'Null'
                self.wait_write_lists.append([job_name,job_company,job_salary,job_area,job_edu,job_detail])

            except Exception as e:
                print 'Sorry,Has Error:{}'.format(e.message)


