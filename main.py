#!/usr/bin/env python

import wx
import os.path


class MainWindow(wx.Frame):
  def __init__(self):
    super(MainWindow, self).__init__(None, size=(800,600))
    self.CreateInteriorWindowComponents()
    self.CreateExteriorWindowComponents()
    self.Centre()
  def CreateInteriorWindowComponents(self):
    panel = wx.Panel(self)
    boxmain = wx.BoxSizer(wx.VERTICAL)
    st1 = wx.StaticText(panel, label='Prices:')
    self.textprice = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
    st2 = wx.StaticText(panel, label='Values:')
    self.textvalue = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
    btncalc = wx.Button(panel, label='Calculate')
    btncalc.Bind(wx.EVT_BUTTON, self.OnCalculate)
    st3 = wx.StaticText(panel, label='Results:')
    self.textresult = wx.TextCtrl(panel, style=wx.TE_MULTILINE|wx.TE_READONLY)
    boxmain.Add((-1, 10))
    boxmain.Add(st1)
    boxmain.Add(self.textprice, flag=wx.TOP|wx.EXPAND, proportion=1);
    boxmain.Add((-1, 10))
    boxmain.Add(st2)
    boxmain.Add(self.textvalue, flag=wx.TOP|wx.EXPAND, proportion=1);
    boxmain.Add((-1, 10))
    boxmain.Add(btncalc)
    boxmain.Add((-1, 10))
    boxmain.Add(st3)
    boxmain.Add(self.textresult, flag=wx.TOP|wx.EXPAND, proportion=1);
    panel.SetSizer(boxmain)
  def CreateExteriorWindowComponents(self):
    self.CreateStatusBar()
    self.SetTitle()
  def SetTitle(self):
    super(MainWindow, self).SetTitle('A-Fund')
  def OnCalculate(self, event):
    self.textresult.SetValue('%s:%s' % (self.textprice.GetValue(), self.textvalue.GetValue() ) )

app = wx.App()
frame = MainWindow()
frame.Show()
app.MainLoop()
