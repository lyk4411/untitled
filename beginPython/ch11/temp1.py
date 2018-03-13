import wx                               #导入wx包
app = wx.App()                          #创建应用程序对象
win = wx.Frame(None,title = 'Simple Editor',size=(410,335))  #创建窗体
bkg = wx.Panel(win)

loadButton = wx.Button(bkg, label = 'Open')
saveButton = wx.Button(bkg, label = 'Save')
filename = wx.TextCtrl(bkg)
context = wx.TextCtrl(bkg,style = wx.TE_MULTILINE | wx.HSCROLL)

hbox = wx.BoxSizer()
hbox.Add(filename,proportion = 1,flag=wx.EXPAND)
hbox.Add(loadButton,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(saveButton,proportion=0,flag=wx.LEFT,border=5)

vbox=wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND | wx.ALL,border=5)
vbox.Add(context,proportion=1,
         flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT,border=5)
bkg.SetSizer(vbox)
# loadButton = wx.Button(win, label = 'Open',
#                        pos=(225,5),size=(80,25))  #创建Button
# saveButton = wx.Button(win, label = 'Save',
#                        pos=(315, 5), size=(80, 25))  #创建Button
# filename = wx.TextCtrl(win,pos = (5,5),size = (210,25))
# content = wx.TextCtrl(win,pos = (5,35),size = (390,260),
#                       style=wx.TE_MULTILINE | wx.HSCROLL)
win.Show()                              #显示窗体
app.MainLoop()                          #运行程序