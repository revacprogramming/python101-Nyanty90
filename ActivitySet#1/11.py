# Tuples

filename = "./py-101/dataset/mbox-short.txt"
with open(filename) as f:
    hr_dict = {}
    for line in f:
        if line.startswith("From "):
            hr = line.split()[5].split(":")[0]
            hr_dict[hr] = hr_dict.get(hr, 0) + 1
    for k, v in sorted(hr_dict.items()):
        print(k, v)
