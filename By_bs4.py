#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# Author  : ok075588
# By_bs4.py

from Urlpage import Urlpage
import requests
from bs4 import BeautifulSoup
import lxml
import string

class By_bs4(Urlpage):

    def __init__(self,startpage,endpage):
        super(By_bs4,self).__init__(startpage,endpage)
        self.header={'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)'}
        self.row=0
        self.wait_write_lists=[]
        self.create_lists_waitforwrite()

    def create_lists_waitforwrite(self):
        for job in self.job_lists:

            if 'https://www.liepin.com' in job:    #偶有链接不完整，予以拼接
                res=requests.get(job,self.header)
            else:
                res=requests.get('https://www.liepin.com{}'.format(job),self.header)

            html=res.text
            res.close()
            soup=BeautifulSoup(html,'lxml')

            try:
                job_name=soup.find('h1').string
                job_company=soup.find('div',class_="title-info").a.string
                job_area=soup.find('p',class_="basic-infor").span.a.string
                job_salary=soup.find('p',class_="job-item-title").contents[0].strip()
                job_edu=soup.find('div',class_="job-qualifications").span.string
                job_detail=soup.find('div',class_="content content-word").get_text().strip()
                self.wait_write_lists.append([job_name,job_company,job_salary,job_area,job_edu,job_detail])

            except Exception as e:
                print 'Sorry,Has Error:{}'.format(e.message)