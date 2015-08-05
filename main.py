#!/usr/bin/env python
import wx

import sgmllib

class MyParser(sgmllib.SGMLParser):
  "A simple parser class."
  def parse(self, s):
    "Parse the given string 's'."
    self.feed(s)
    self.close()
  def __init__(self, verbose=0):
    "Initialise an object, passing 'verbose' to the superclass."
    sgmllib.SGMLParser.__init__(self, verbose)
    self.hyperlinks = []
    self.title = ''
  def start_a(self, attributes):
    "Process a hyperlink and its 'attributes'."
    for name, value in attributes:
      if name == "href":
        self.hyperlinks.append(value)
    
  def get_hyperlinks(self):
    "Return the list of hyperlinks."
    return self.hyperlinks
  def get_title(self):
    "Return the title of the A-fund."
    return self.title

import urllib, sgmllib

# Get something to work with.
f = urllib.urlopen("http://finance.sina.com.cn/fund/quotes/150186/bc.shtml")
s = f.read()

# Try and process the page.
# The class should have been defined first, remember.
myparser = MyParser()
myparser.parse(s)

# Get the hyperlinks.
print myparser.get_hyperlinks()

app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = wx.Frame(None, wx.ID_ANY, "Hello World") # A Frame is a top-level window.
frame.Show(True)     # Show the frame.
app.MainLoop()


