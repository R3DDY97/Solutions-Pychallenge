#!/usr/bin/env python3

import webbrowser

def soln1():
    url1 = "http://www.pythonchallenge.com/pc/def/0.html"
    url2 = url1.replace("0",str(2**38))
    webbrowser.open(url2)

if __name__ == "__main__":
    soln1()
