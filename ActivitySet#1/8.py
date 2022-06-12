# Files

with open((filename := "py-101/dataset/mbox-short.txt")) as f:
    cnt, ttl = 0, 0
    for l in f:
        if l.startswith("X-DSPAM-Confidence:"):
            cnt += 1
            ttl += float(l.split()[1])
    print(ttl/cnt)
