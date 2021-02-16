import os

# os.chdir(r'C:\Users\aclass\Desktop\startcamp\make_dummy\dummy') #해당폴더를 연것과 동일
# filenames = os.listdir('.')  # dot의 의미 : 현재폴더 안에 있는 모든 파일들을 리스트를 list로 다 받겠다

# for filename in filenames:  #리스트에 담긴 네임들을 하나하나 보면서
#     #os.rename(filename,f'SAMSUNG_{filename}') 원래 파일 네임을 SAMSUNG_를 붙여서 바꾸겠다
#     os.rename(filename, filename.replace('SAMSUNG','SSAFY')) #원래 파일 네임에서 SAMSUNG을 SSAFY로 바꾸겠다.

    
os.chdir(r'C:\Users\multicampus\Desktop\image\frame\four')

filenames = os.listdir('.')
for i in range(0, len(filenames)):
    os.rename(filenames[i], str(i)+'.jpg')