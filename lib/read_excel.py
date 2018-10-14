#coding:utf-8
"""读取excel数据"""
import xlrd
import sys
import os
sys.path.append('..')
from config import config as cf  #提别名

# 从excel 中获取一行用例的数据
# data_file:数据文件  sheet：所在表名，case_name：用例名称
def get_case_data(data_file,sheet,case_name):
    data_file_path=os.path.join(cf.data_path,data_file)
    wb=xlrd.open_workbook(data_file_path)#打开excel
    sh=wb.sheet_by_name(sheet)#获取工作表

    for i in range(1,sh.nrows):#[1,3) 1,2
       if sh.cell(i,0).value==case_name:
           return sh.row_values()

if __name__=='__main__':
    r=get_case_data("test_user_data.xlsx","TestUserLogin","test_user_login_nomal")
    print(r)

