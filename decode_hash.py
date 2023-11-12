import hashlib
from tqdm import tqdm

import zipfile

def unzip_file(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_path)
        
input_hashed = "0e385589729688144363378792916561"
unzip_file('passwords_zip.ext', 'passwords.txt')
psw_f = open('passwords.txt/passwords.txt', 'r')
progress_bar = tqdm(total=int(input('number of passwords in passwords_zip.ext: ')), unit='passwords')


flag = 1
for w in psw_f:
    word = w.encode('utf-8')
    hash_w = hashlib.md5(word.strip())
    dig = hash_w.hexdigest()

    dig = dig.encode('utf-8')
    super_hs_w = hashlib.md5(dig.strip())
    sup_dig = super_hs_w.hexdigest()

    progress_bar.update(1)

    if sup_dig == input_hashed:
        flag = 0
        print(w)
        break

if flag:
    progress_bar.close()
    print('password not found')

psw_f.close()
