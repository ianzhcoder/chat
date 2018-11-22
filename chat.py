import os

def read_file(filename):
    chat = []
    with open (filename,'r',encoding = 'utf-8-sig') as f:
        for line in f:
            content = line.strip()
            if content == 'Allen' or content == 'Tom':
                name = content 
                continue
            else:
                chat.append([name,content])
        return (chat)

def write_file(chat):
    with open ('output.txt','w',encoding = 'utf-8') as f:
        for c in chat:
            f.write (c[0] + ':' + c[1] + '\n')


def main():
    filename = input("please enter the filename:")
    if os.path.isfile(filename):
        print ('readfile success')
        chat = read_file(filename)
        write_file(chat)
    else:
        print ('readfile fail...')


main()

