import string

text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

shifted_letters = string.ascii_lowercase[2:] + string.ascii_lowercase[:2]
translations = string.maketrans(string.ascii_lowercase, shifted_letters)

print string.translate(text, translations)
