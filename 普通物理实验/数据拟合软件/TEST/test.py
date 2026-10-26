import wx 
  
#import the newly created GUI file 
import noname  
class CalcFrame(noname.MyFrame1): 
   def __init__(self,parent): 
      noname.MyFrame1.__init__(self,parent)  
		
   def FindSquare(self,event): 
      num = int(self.m_textCtrl1.GetValue()) 
      self.m_textCtrl2.SetValue (str(num*num)) 
        
app = wx.App(False) 
frame = CalcFrame(None) 
frame.Show(True) 
#start the applications 
app.MainLoop()