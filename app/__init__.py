import shutil

SW = shutil.get_terminal_size().columns-1

BANNER_TEXT = "ECOMMERCE API"
BTW = len(BANNER_TEXT)//2

print("*"*SW)
print(" "*(SW//2-BTW), BANNER_TEXT)
print("*"*SW)