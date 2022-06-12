# Strings

txt = "X-DSPAM-Confidence:    0.8475"
print(float(txt[txt.find(':')+1:].strip()))
