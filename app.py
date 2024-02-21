import PyPDF2
from googletrans import Translator
import os


path = './flutterengineering-book.pdf'

locale = 'ko'

output = f'./flutterengineering-book-{locale}/'

# make directory 

if not os.path.exists(output):
    os.makedirs(output)


# 텍스트 파일을 합치는 함수입니다
def text_combine(dir):
    # read all files in the directory
    files = os.listdir(dir)
    
    print(f"{len(files)} 개의 파일이 존재합니다.")
    result = ''
    # sort the files by name
    arr = sorted(files, key=lambda x: int(x.split('.')[0]))
    
    for file in arr:
        print(f"{file} 파일을 읽고 있습니다.")
        with open(dir + file, 'r') as f:
            text = f.read()
            f.close()
            result += text
    
    # write to file
    with open('./result.txt', 'w') as f:
        f.write(result)
        f.close()


def translate(text):
    translator = Translator()
    result = translator.translate(text, dest='ko')
    print(result.text)
    return result.text

def operation():
    with open(path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        print('파일을 열고 있습니다.')
        print('파일의 페이지 수는 : ', len(reader.pages), '입니다')
        size = len(reader.pages)

        for i in range(size):
            page = reader.pages[i]
            text = page.extract_text()
            # write to file
            directory = output + str(i) + '.txt'
            if os.path.exists(directory):
                print('파일이 존재합니다.')
            else:
                with open(directory, 'w') as f:
                    # translate the text
                    t_text = translate(text)

                    f.write(t_text)
                    print('파일을 쓰고 있습니다.')
                    f.close()
                   
          



# open the file




text_combine(output)