
data = []
f = open('answer.txt', encoding="utf8")
for line in f:
    d = {}
    d['qId'] = line[line.index('qId:')+len('qId:'):line.index('aid:')-1]
    d['aid'] = line[line.index('aid:')+len('aid:'):line.index('content:')-1]
    d['content'] = line[line.index('content:')+len('content:'):line.index('time:')-1]
    d['uId'] = line[line.index('uId:')+len('uId:'):line.index('#up:')-1]
    d['#up'] = line[line.index('#up:')+len('#up:'):line.index('#down:')-1]
    d['#down'] = line[line.index('#down:')+len('#down:'):]
    data.append(d)

x = []
for i in range(len(data)):
    d = len(data[i]['content'])
    x.append(d)
y = []
for i in range(len(data)):
    d = int(data[i]['#up'])
    y.append(d)
