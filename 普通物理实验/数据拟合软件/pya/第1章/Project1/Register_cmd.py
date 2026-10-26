#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import tkinter
from   tkinter import *
import Fun
uiName="Register"
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

#Form 'Form_1's Event :Load
def Form_1_onLoad(uiName):
    pass
#Button '注册's Event :Command
def register_onCommand(uiName,widgetName):
    strUserAccount = Fun.GetText(uiName,'Entry_1')
    strUserName = Fun.GetText(uiName,'Entry_2')
    Password1 = Fun.GetText(uiName,'Entry_3')
    Passwors2 = Fun.GetText(uiName,'Entry_4')
    if Password1==Passwors2:
        strUserPassword = Password1
    else:
        Fun.MessageBox(text='两次输入密码不同')
    print('导入sqlite3')
    import sqlite3
    print('连接数据库')
    conn = sqlite3.connect(':memory:')
    print('取得游标')
    cur = conn.cursor()
    print('如果不存在表则创建表member')
    try:
        cur.execute('create table if not exists member(id integer primary key autoincrement not null, useraccount text,username text,password text)')
        conn.commit()
    except:
        pass
    print('查询member表里是否有相同数据账号的数据')
    cur.execute('select * from member where useraccount ="'+strUserAccount+'"')
    if len(cur.fetchall())=0:
        try:
            print('将数据插入到当前数据表member中')
            cur.execute('insert into member (useraccount,username,password)values("'+strUserAccount+'","'+strUserName+'","'+strUserPassword+'")')
            conn.commit()
            Fun.MessageBox(text='注册成功')
        except:
            Fun.MessageBox(text='注册失败')
    else:
        Fun.MessageBox(text='存在同名账户，请重新注册')
