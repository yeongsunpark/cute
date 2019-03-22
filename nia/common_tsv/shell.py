import os
names = ['imbyeonghyeon', 'kimjeawoo', 'kimminji', 'kimteayoon', 'leeseojin', 'parksoyeong', 'songjuhyeong',
'wonjiyeon', 'wonkwangjea', 'yangmincheol', 'yoonhyeok', 'choojinkyeong', 'imsongee', 'kimhyeyoon',
'leejungsup', 'parkjinsun', 'songhyewon', 'yeomjisun', 'yoonseoyeong']

for name in names:
    print (name)
    a = os.popen('cat normal_finish-{}.tsv | wc -l'.format(name))
    b = os.popen('head -1 normal_finish-%s.tsv' % name)
    print (b.read())

