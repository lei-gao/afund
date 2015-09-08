#!/usr/bin/env python
# coding=gbk

import wx
import os.path

Interest = 2.00

FundID              = 0
FundBID             = 1
FixedInterest       = 2
FloatingInterest    = 3
FundName            = 4
FundPrice           = 5
FundBName           = 6
FundBPrice          = 7
FundValue           = 8
FundBValue          = 9

Funds = [ ['150177', '150178', '3.0', '1', '', '', '', '', '', ''], # ����֤ȯ���շּ�A
          ['150227', '150228', '5.5', '0', '', '', '', '', '', ''], # �������зּ�A # �����ͬ��Ч���й��������й����Ľ��ڻ��������һ���ڴ���׼����(˰��)+3% (April 18, 2.50)
          ['150198', '150199', '4.0', '1', '', '', '', '', '', ''], # ��̩��֤ʳƷ������ҵָ���ּ�A
          ['150171', '150172', '3.0', '1', '', '', '', '', '', ''], # ���������������֤ȯ��ҵָ���ּ�A
          ['150152', '150153', '3.5', '1', '', '', '', '', '', ''], # ������ҵ��ָ���ּ�A
          ['150186', '150187', '3.0', '1', '', '', '', '', '', ''], # ����������֤����ָ���ּ�A
          ['150200', '150201', '3.0', '1', '', '', '', '', '', ''], # ������֤ȫָ֤ȯ��˾ָ���ּ�A
          ['150181', '150182', '3.0', '1', '', '', '', '', '', ''], # ������֤����ָ���ּ�A
          ['150259', '150260', '3.0', '1', '', '', '', '', '', ''], # �׷�������ָ���ּ�A
          ['150223', '150224', '6.0', '0', '', '', '', '', '', ''], # ������֤ȫָ֤ȯ��˾ָ���ּ�A
          ['150265', '150266', '4.0', '1', '', '', '', '', '', ''], # ����һ��һ·�ּ�A
          ['150327', '150328', '4.0', '1', '', '', '', '', '', ''], # ������֤����Դָ���ּ�A
          ['150209', '150210', '3.0', '1', '', '', '', '', '', ''], # ������֤������ҵ�ĸ�ָ���ּ�A
          ['150184', '150185', '3.0', '1', '', '', '', '', '', ''], # ����������֤������ҵָ���ּ�A
          ['150064', '150065', '3.5', '1', '', '', '', '', '', ''], # ��ʢͬ��A
          ['150315', '150316', '3.0', '1', '', '', '', '', '', ''], # ������֤��ҵ4.0ָ���ּ�A
          ['502007', '502008', '3.0', '1', '', '', '', '', '', ''], # �׷������ĸ�ּ�A
          ['150027', '150028', '3.2', '1', '', '', '', '', '', ''], # �ų���֤500ָ��A
          ['150321', '150322', '5.0', '1', '', '', '', '', '', ''], # ������֤úָ̿���ּ�A
          ['150018', '150019', '3.0', '1', '', '', '', '', '', ''], # �����Ƚ�
          ['150030', '150031', '3.5', '1', '', '', '', '', '', ''], # ������֤��Ȩ90ָ������
          ['150190', '150191', '4.0', '1', '', '', '', '', '', ''], # �»���֤������ҵָ���ּ�A
          ['150034', '150035', '4.17950', '0', '', '', '', '', '', ''], # ̩���������A
          ['150194', '150195', '3.0', '1', '', '', '', '', '', ''], # ������֤�ƶ�������ָ���ּ�A
          ['150211', '150212', '3.5', '1', '', '', '', '', '', ''], # ������֤����Դ����ָ���ּ�A
        ]

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
    st4 = wx.StaticText(panel, label='Interest:')
    self.textinterest = wx.TextCtrl(panel)
    boxmain.Add((-1, 10))
    boxmain.Add(st1)
    boxmain.Add(self.textprice, flag=wx.TOP|wx.EXPAND, proportion=1)
    boxmain.Add((-1, 10))
    boxmain.Add(st2)
    boxmain.Add(self.textvalue, flag=wx.TOP|wx.EXPAND, proportion=1)
    boxmain.Add((-1, 10))
    boxmain.Add(btncalc)
    boxmain.Add((-1, 10))
    boxmain.Add(st3)
    boxmain.Add(self.textresult, flag=wx.TOP|wx.EXPAND, proportion=1)
    boxmain.Add((-1, 10))
    interestbox = wx.BoxSizer(wx.HORIZONTAL)
    interestbox.Add(st4)
    interestbox.Add(self.textinterest)
    boxmain.Add(interestbox, flag=wx.TOP)
    panel.SetSizer(boxmain)
    self.textinterest.SetValue('%f' % Interest)
  def CreateExteriorWindowComponents(self):
    self.CreateStatusBar()
    self.SetTitle()
  def SetTitle(self):
    super(MainWindow, self).SetTitle('A-Fund')
  def GetNumber(self, inputstring):
    outputstring = ''
    for index in range(0, len(inputstring) ):
      if ( (inputstring[index] >= '0' and inputstring[index] <= '9') or inputstring[index] == '.'):
        outputstring += inputstring[index]
    return outputstring
  def OnCalculate(self, event):
    # Price processing
    price = self.textprice.GetValue()
    # Split string into words
    prices = []
    word = ''
    for c in price:
      if (c == '\n' or c == ' ' or c == '\t' or c == '\r'):
        prices.append(word)
        word = ''
      else:
        word += c
    prices.append(word)
    # Find prices
    state = 0
    index = 0
    found = 0
    for w in prices:
      if (state == 0):
        for index in range(0, len(Funds)):
          if (w == Funds[index][0]):
            found = index
            state = 1
          elif (w == Funds[index][1]):
            found = index
            state = 3
      elif (state == 1): # FundName
        Funds[found][FundName] = w
        state = 2
      elif (state == 2): # FundPrice
        Funds[found][FundPrice] = self.GetNumber(w)
        state = 0
      elif (state == 3): # FundBName
        Funds[found][FundBName] = w
        state = 4
      elif (state == 4): # FundBPrice
        Funds[found][FundBPrice] = self.GetNumber(w)
        state = 0
    # Value processing
    value = self.textvalue.GetValue()
    # Split string into words
    values = []
    word = ''
    for c in value:
      if (c == '\n' or c == ' ' or c == '\t' or c == '\r'):
        values.append(word)
        word = ''
      else:
        word += c
    values.append(word)
    # Find values
    state = 0
    index = 0
    found = 0
    for w in values:
      if (state == 0):
        for index in range(0, len(Funds)):
          if (w == Funds[index][0]):
            found = index
            state = 1
          elif (w == Funds[index][1]):
            found = index
            state = 3
      elif (state == 1): # FundName
        if (Funds[found][FundName] != w):
          Funds[found][FundName] = 'ERROR'
        state = 2
      elif (state == 2): # FundValue
        Funds[found][FundValue] = self.GetNumber(w)
        state = 0
      elif (state == 3): # FundBName
        if (Funds[found][FundBName] != w):
          Funds[found][FundBName] = 'ERROR'
        state = 4
      elif (state == 4): # FundBValue
        Funds[found][FundBValue] = self.GetNumber(w)
        state = 0
    # Print results
    results = ''
    for index in range(0, len(Funds)):
      interest = 0.00
      theratio = 0.00
      results += '##########\n%s (%s) Price %s, Value %s\n%s(%s) B-Price %s, B-Value %s\n' % (
                  Funds[index][FundName], Funds[index][FundID],
                  Funds[index][FundPrice], Funds[index][FundValue],
                  Funds[index][FundBName], Funds[index][FundBID],
                  Funds[index][FundBPrice], Funds[index][FundBValue])
      # Calculate interest rate
      floatingInterest = 0
      if (Funds[index][FloatingInterest] == '1'):
        floatingInterest = 1
      fixedInterest = float(Funds[index][FixedInterest])
      interest = fixedInterest
      if (floatingInterest):
        interest = fixedInterest + Interest
      # Calculate future income
      if (1):
        thevalue = float(Funds[index][FundValue])
        thereturn = 1.00 + (0.01 * interest)
        theincome = thereturn - thevalue
        theprice = float(Funds[index][FundPrice])
        theratio = (theincome / theprice) * (thereturn - 1.00) / (thereturn - thevalue)
      results += 'Interest %s + (%s * %f) == %f\n@@@@@ Return %f @@@@@\n' % (
                  Funds[index][FixedInterest], Funds[index][FloatingInterest], Interest, interest,
                  theratio)
    self.textresult.SetValue(results)

app = wx.App()
frame = MainWindow()
frame.Show()
app.MainLoop()
