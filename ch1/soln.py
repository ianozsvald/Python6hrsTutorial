"""Challenge 1 of PythonChallenge: http://www.pythonchallenge.com/pc/def/map.html"""

#text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
text = """http://www.pythonchallenge.com/pc/def/map.html"""

new_text = ""

for c in text:
    new_char = c
    if c != " ":
        if c.isalpha():
            new_ordinal = ord(c) + 2
            if new_ordinal > 122:
                new_ordinal = new_ordinal - 26
            new_char = chr(new_ordinal)
    new_text += new_char
print new_text
