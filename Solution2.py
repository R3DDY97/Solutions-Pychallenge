#!/usr/bin/env python3

import string
import webbrowser


test_data = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'qufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmuynnjw ml rfc spj"
url2 = "http://www.pythonchallenge.com/pc/def/map.html"

def replace_letter(text):
    azlist = string.ascii_lowercase
    new_data = ""
    for i in text:
        if i in azlist:
            pos = (azlist.index(i) + 2 +len(azlist))%len(azlist)
            new_data = new_data + azlist[pos]
        else:
            new_data = new_data + i
    print("Translated data is\n{}\n".format(new_data))
    return new_data

if __name__ == "__main__":
    replace_letter(test_data)
    url3_str = replace_letter("map")
    url3 = url2.replace("map", url3_str)
    print("Next url is\n\t{}\n".format(url3))
    webbrowser.open(url3)
