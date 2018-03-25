#coding=utf-8
from Urlpage import Urlpage
import requests
from lxml import etree
import string
import time
import xlsxwriter

class Write2excel(Urlpage):
    header={'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)'}
    row=0
    def __init__(self):
        self.wait_write_lists=[]

        #继承Urlpage
        super(Write2excel,self).__init__()
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
                job_name=selectors.xpath('//h1/@title')[0]                                      #职位名称
                job_company=selectors.xpath('//a[@data-promid=""]/text()')[0].strip()           #公司名称
                job_salary=selectors.xpath('//p[@class="job-item-title"]/text()')[0].strip()    #薪资
                job_edu=selectors.xpath('//div[@class="job-qualifications"]//span//text()')[0]  #学历
                '''
                job_workyears=selectors.xpath('//div[@job-qualifications]//span//text()')[1]   #工作年限
                job_age=selectors.xpath('//div[@job-qualifications]//span//text()')[3]      #年龄要求
                '''
                job_area=selectors.xpath('//p[@class="basic-infor"]/span//a/text()')[0].strip() #地区
                job_detail=selectors.xpath('//div[@class="content content-word"]')[0].xpath('.//text()')
                job_detail='\n'.join(job_detail)     #职位描述
                self.wait_write_lists.append([job_name,job_company,job_salary,job_area,job_edu,job_detail])
                self.row+=1
            except:
                pass
'''
            #self.write2(self.wait_write_lists)

    def write2(self,url):
        for i in range(0,len(url)):
            sheet.write(self.row,i,url[i])
        self.format_excel()

     #设置excel列宽
    def format_excel(self):
        sheet.set_column('A:A',30)
        sheet.set_column('B:B',20)
        sheet.set_column('C:C',12)
        sheet.set_column('D:D',12)
        sheet.set_column('E:E',12)


if __name__=='__main__':
    xls_book=xlsxwriter.Workbook('d:\\liepin.xlsx')
    sheet=xls_book.add_worksheet('sheet')
    aa=Write2excel()
    print aa.wait_write_lists
    xls_book.close()
'''







