import os
#統計對話內容出現的文字、貼圖、圖片


#修改function read_file,只單純讀取檔案
def read_file(filename):
    chat = []
    with open (filename,'r',encoding = 'utf-8-sig') as f:
        for line in f:
            content = line.strip()
            chat.append(content)
        return (chat)

#增加內容切割function
def content(chat):
    lines =[]
    for line in chat:
        s = line.split(' ')
        #清單的切割
        time = s[0]
        name = s[1]
        if name == 'Viki' or name == 'Allen':
            content =s[2:]
        lines.append([time,name,content])
    return (lines)

#增加文字統計function
def content_text(chat):
    a_t_count = 0
    v_t_count = 0
    for line in chat:
        s = line.split(' ')
        #清單的切割
        time = s[0]
        name = s[1]
        if name == 'Viki':
            #排除非文字部分
            if '貼圖' in s[2] or '圖片' in s[2]:
                continue
            else:
                for m in s[2:]:
                    v_t_count += len(m)
        
        elif name == 'Allen':
            if '貼圖' in s[2] or '圖片' in s[2]:
                continue
            else:
                for m in s[2:]:
                    a_t_count += len(m)
    print ('Allen 在對話內容中總共輸入了:', a_t_count, '字')
    print ('Viki 在對話內容中總共輸入了:', v_t_count, '字')

#增加貼圖統計function
def content_sticker(chat):
    a_s_count = 0
    v_s_count = 0
    for line in chat:
        s = line.split(' ')
        if s[1] == 'Viki':
            if s[2] == '貼圖':
                v_s_count += 1
        
        elif s[1] == 'Allen':
            if s[2] == '貼圖':
                a_s_count += 1
    print ('Allen 在對話內容中總共輸入了:', a_s_count, '次貼圖')
    print ('Viki 在對話內容中總共輸入了:', v_s_count, '次貼圖')

#增加圖片統計function
def content_image(chat):
    a_i_count = 0
    v_i_count = 0
    for line in chat:
        s = line.split(' ')
        #清單的切割
        if s[1] == 'Viki':
            if s[2] == '圖片':
                v_i_count += 1
        
        elif s[1] == 'Allen':
            if s[2] == '圖片':
                a_i_count += 1
    print ('Allen 在對話內容中總共輸入了:', a_i_count, '次圖片')
    print ('Viki 在對話內容中總共輸入了:', v_i_count, '次圖片')

#+filename 參數
#寫入檔案時只記錄名字和內容
def write_file(filename,chat):
    with open (filename,'w',encoding = 'utf-8') as f:
        for c in chat:
            s = c.split(' ')
            #將對話LIST消除變成純文字
            #for n in s[2:]:
            #    print (n)
            f.write (s[1] + ':' + str(s[2:]) + '\n')


def main():
    filename = input("please enter the filename:")
    if os.path.isfile(filename):
        print ('readfile success')
        chat = read_file(filename)
        content_text(chat)
        content_sticker(chat)
        content_image(chat)
        content(chat)
        write_file('Line_output.txt',chat)
    else:
        print ('readfile fail...')


main()

