# Dictionaries

filename = "./py-101/dataset/mbox-short.txt"
with open(filename) as f:
    send_dict = {}
    for line in f:
        if line.startswith("From "):
            send = line.split()[1]
            send_dict[send] = send_dict.get(send, 0) + 1
    msend = max(send_dict, key=send_dict.get)
    print(msend, send_dict[msend])
