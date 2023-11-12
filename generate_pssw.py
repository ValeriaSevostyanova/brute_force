from tqdm import tqdm

import random
import string

import zipfile
import os

def zip_file(file_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(file_path)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for _ in range(length):
        password += random.choice(characters)
    return password

num_passwords = int(input('number of passwords: ')) # number of passwords
password_length = int(input('password length: ')) # password length
progress_bar = tqdm(total=num_passwords, unit='passwords')

with open('passwords.txt', 'w') as file:
    passwords = []
    for _ in range(num_passwords):
        file.write(generate_password(password_length) + '\n')
        progress_bar.update(1)
    file.close()

progress_bar.close()
zip_file('passwords.txt', 'passwords_zip.ext')
print('passwords are generated and saved in the passwords_zip.ext file')
os.remove('passwords.txt')
    
    
