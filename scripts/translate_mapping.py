import os
if os.path.exists("log/result.txt"):
  os.remove("log/result.txt")

src = []
tgt = []
count = 1
src_count = 0
tgt_count = 0
with open('log/input.txt') as f:
    text = f.read()

string = text.split('"')[1::2]
for i in string:
    word = i.split(';')

    for i in word:
        temp = i.split('=')
        src.append(temp[-1])
        temp_tgt = temp[0].split(' ')
        tgt.append((temp_tgt[-1]))
    src.pop()
    tgt.pop()
    src_count = src_count + len(src)
    tgt_count = tgt_count + len(tgt)
    with open('log/result.txt', 'a') as fp:
        fp.write(str(count))
        fp.write("\n")
        fp.write("source_cols_count:")
        fp.write(str(src_count))
        fp.write("\n")
        fp.write("source_cols: ")
        for item in src:
            if src.index(item) == len(src)-1:
                fp.write("%s" % item)
            else:
                fp.write("%s, " % item)
        fp.write("\n")
        fp.write("target_cols_count:")
        fp.write(str(tgt_count))
        fp.write("\n")
        fp.write("target_cols: ")
        for item in tgt:
            if tgt.index(item) == len(tgt)-1:
                fp.write("%s" % item)
            else:
                fp.write("%s, " % item)
        fp.write("\n")
        fp.write("\n")
    src.clear()
    tgt.clear()
    src_count = 0
    tgt_count = 0
    count=count+1