#coding=utf-8
#import libs 
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import Project1_cmd
import Project1_sty
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
class  Project1:
    def __init__(self,root,isTKroot = True,params=None):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UIParamsDictionary[uiName]=params
        Fun.G_UICommandDictionary[uiName]=Project1_cmd
        Fun.Register(uiName,'root',root)
        style = Project1_sty.SetupStyle()
        if isTKroot == True:
            root.title("Project1")
            Fun.WindowDraggable(root,False,0,'#ffffff')
            Fun.CenterDlg(uiName,root,300,160)
            root['background'] = '#EFEFEF'
        root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 300)
        Form_1.configure(height = 160)
        Form_1.configure(bg = "#EFEFEF")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.G_RootSize=[300,160]
        #Create the elements of root 
        Label_2 = tkinter.Label(Form_1,text="账号")
        Fun.Register(uiName,'Label_2',Label_2)
        Fun.SetControlPlace(uiName,'Label_2',20,20,80,23)
        Label_2.configure(bg = "#EFEFEF")
        Label_2.configure(fg = "SystemButtonText")
        Label_2.configure(relief = "flat")
        Label_4 = tkinter.Label(Form_1,text="密码")
        Fun.Register(uiName,'Label_4',Label_4)
        Fun.SetControlPlace(uiName,'Label_4',20,50,80,23)
        Label_4.configure(bg = "#EFEFEF")
        Label_4.configure(fg = "SystemButtonText")
        Label_4.configure(relief = "flat")
        Entry_3= EXUIControl.CustomEntry(Form_1)
        Fun.Register(uiName,'Entry_3',Entry_3)
        Entry_3.SetBGColor("#FFFFFF")
        Entry_3.SetFGColor("#000000")
        Entry_3.SetTipFGColor("#888888")
        Entry_3.SetRelief("sunken")
        Fun.SetControlPlace(uiName,'Entry_3',120,24,160,23)
        Entry_5= EXUIControl.CustomEntry(Form_1)
        Fun.Register(uiName,'Entry_5',Entry_5)
        Entry_5.SetBGColor("#FFFFFF")
        Entry_5.SetFGColor("#000000")
        Entry_5.SetShowChar("*")
        Entry_5.SetTipFGColor("#888888")
        Entry_5.SetRelief("sunken")
        Fun.SetControlPlace(uiName,'Entry_5',120,54,160,23)
        Button_6 = tkinter.Button(Form_1,text="确定")
        Fun.Register(uiName,'Button_6',Button_6)
        Fun.SetControlPlace(uiName,'Button_6',146,103,60,23)
        Button_6.configure(bg = "#EFEFEF")
        Button_6.configure(command=lambda:Fun.CommandFunction_Adaptor(Project1_cmd.Button_6_onCommand,uiName,"Button_6"))
        Button_7 = tkinter.Button(Form_1,text="退出")
        Fun.Register(uiName,'Button_7',Button_7)
        Fun.SetControlPlace(uiName,'Button_7',220,103,60,23)
        Button_7.configure(bg = "#EFEFEF")
        Button_7.configure(command=lambda:Fun.CommandFunction_Adaptor(Project1_cmd.Button_7_onCommand,uiName,"Button_7"))
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        Fun.RunForm1_CallBack(uiName,"Load",Project1_cmd.Form_1_onLoad)
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
    MyDlg = Project1(root)
    root.mainloop()
