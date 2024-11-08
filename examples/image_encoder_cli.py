# encode_icon.py
from base64 import b64encode
import sys
import pyperclip

# filename = sys.argv[1]
filename = "address_book_32.png"
with open(filename, "rb") as f:
    pyperclip.copy(b64encode(f.read()).decode("ascii"))
    print("Copied to clipboard.")
