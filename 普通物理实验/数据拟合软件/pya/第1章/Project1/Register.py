#coding=utf-8
#import libs 
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import Register_cmd
import Register_sty
import Fun
import EXUIControl
EXUIControl.G_ExeDir = Fun.G_ExeDir
EXUIControl.G_ResDir = Fun.G_ResDir
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Register:
    def __init__(self,root,isTKroot = True,params=None):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UIParamsDictionary[uiName]=params
        Fun.G_UICommandDictionary[uiName]=Register_cmd
        Fun.Register(uiName,'root',root)
        style = Register_sty.SetupStyle()
        if isTKroot == True:
            root.title("加入卷卷")
            Fun.WindowDraggable(root,False,0,'#ffffff')
            Fun.CenterDlg(uiName,root,960,640)
            root.wm_attributes("-topmost",1)
            root['background'] = '#efefef'
        root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 960)
        Form_1.configure(height = 640)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.G_RootSize=[960,640]
        #Create the elements of root 
        Label_2 = tkinter.Label(Form_1,text="账号")
        Fun.Register(uiName,'Label_2',Label_2,'Label_1')
        Fun.SetControlPlace(uiName,'Label_2',123,84,100,48)
        Label_2.configure(bg = "#efefef")
        Label_2.configure(fg = "SystemButtonText")
        Label_2.configure(relief = "flat")
        Label_4 = tkinter.Label(Form_1,text="用户名")
        Fun.Register(uiName,'Label_4',Label_4,'Label_2')
        Fun.SetControlPlace(uiName,'Label_4',123,172,100,48)
        Label_4.configure(bg = "#efefef")
        Label_4.configure(fg = "SystemButtonText")
        Label_4.configure(relief = "flat")
        Label_6 = tkinter.Label(Form_1,text="密码")
        Fun.Register(uiName,'Label_6',Label_6,'Label_3')
        Fun.SetControlPlace(uiName,'Label_6',123,272,100,48)
        Label_6.configure(bg = "#efefef")
        Label_6.configure(fg = "SystemButtonText")
        Label_6.configure(relief = "flat")
        Label_8 = tkinter.Label(Form_1,text="再次输入密码")
        Fun.Register(uiName,'Label_8',Label_8,'Label_4')
        Fun.SetControlPlace(uiName,'Label_8',124,371,100,48)
        Label_8.configure(bg = "#efefef")
        Label_8.configure(fg = "SystemButtonText")
        Label_8.configure(relief = "flat")
        Entry_3= EXUIControl.CustomEntry(Form_1)
        Fun.Register(uiName,'Entry_3',Entry_3,'Entry_1')
        Entry_3.SetBGColor("#FFFFFF")
        Entry_3.SetFGColor("#000000")
        Entry_3.SetTipFGColor("#888888")
        Entry_3.SetRelief("sunken")
        Fun.SetControlPlace(uiName,'Entry_3',330,84,240,48)
        Entry_5= EXUIControl.CustomEntry(Form_1)
        Fun.Register(uiName,'Entry_5',Entry_5,'Entry_2')
        Entry_5.SetBGColor("#FFFFFF")
        Entry_5.SetFGColor("#000000")
        Entry_5.SetTipFGColor("#888888")
        Entry_5.SetRelief("sunken")
        Fun.SetControlPlace(uiName,'Entry_5',330,172,240,48)
        Entry_7= EXUIControl.CustomEntry(Form_1)
        Fun.Register(uiName,'Entry_7',Entry_7,'Entry_3')
        Entry_7.SetBGColor("#FFFFFF")
        Entry_7.SetFGColor("#000000")
        Entry_7.SetTipFGColor("#888888")
        Entry_7.SetRelief("sunken")
        Fun.SetControlPlace(uiName,'Entry_7',330,272,240,48)
        Entry_9= EXUIControl.CustomEntry(Form_1)
        Fun.Register(uiName,'Entry_9',Entry_9,'Entry_4')
        Entry_9.SetBGColor("#FFFFFF")
        Entry_9.SetFGColor("#000000")
        Entry_9.SetTipFGColor("#888888")
        Entry_9.SetRelief("sunken")
        Fun.SetControlPlace(uiName,'Entry_9',330,371,240,48)
        Button_10 = tkinter.Button(Form_1,text="注册")
        Fun.Register(uiName,'Button_10',Button_10,'register')
        Fun.SetControlPlace(uiName,'Button_10',390,482,120,48)
        Button_10.configure(bg = "#EFEFEF")
        Button_10.configure(command=lambda:Fun.CommandFunction_Adaptor(Register_cmd.register_onCommand,uiName,"register"))
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        Fun.RunForm1_CallBack(uiName,"Load",Register_cmd.Form_1_onLoad)
        #Add Some Logic Code Here: (Keep This Line of comments)



        #Exit Application: (Keep This Line of comments)
        if self.isTKroot == True and Fun.GetElement(self.uiName,"root"):
            self.root.protocol('WM_DELETE_WINDOW', self.Exit)
            
    def GetRootSize(self):
        return Fun.G_RootSize[0],Fun.G_RootSize[1]
    def GetAllElement(self):
        return Fun.G_UIElementDictionary[self.uiName]
    def Escape(self,event):
        if Fun.AskBox('提示','确定退出程序？') == True:
            self.Exit()
    def Exit(self):
        if self.isTKroot == True:
            Fun.DestroyUI(self.uiName)

    def Configure(self,event):
        Form_1 = Fun.GetElement(self.uiName,'Form_1')
        if Form_1 == event.widget:
            Fun.ReDrawCanvasRecord(self.uiName)
        if self.root == event.widget:
            Fun.ResizeRoot(self.uiName,self.root,event)
            Fun.ResizeAllChart(self.uiName)
            uiName = self.uiName
            pass
        Fun.ActiveElement(self.uiName,event.widget)
#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Register(root)
    root.mainloop()
