import os 
#清單以及字串切割

def read_file(filename):
    lines =[]
    with open (filename,'r',encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
        return lines

def context(line):
    for n in line:
        #將傳進來的值利用空格做切割
        s = n.split(' ')
        #取出清單第一個位置中的前5個字
        time = s[0][:5]
        #取出清單第一個位置中第五個數字開始到最後的字串
        name = s[0][5:]
        print (name, s[1], '-----', time)


def main():
    filename = input("please enter the filename:")
    if os.path.isfile(filename):
        print ('readfile success')
        chat = read_file(filename)
        print (chat)
        context(chat)

    else:
        print ('readfile fail...')

main()