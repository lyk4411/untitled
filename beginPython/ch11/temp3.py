import wx

def hello(event):
    print("hello world.")
app = wx.App()
win = wx.Frame(None,title = "hello,python", size=(410,335))
button = wx.Button(win,label="Hello")
button.Bind(wx.EVT_BUTTON,hello)
win.Show()
app.MainLoop()