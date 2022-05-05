
import sys
import unittest
from os import path
print(path.dirname(path.dirname(path.abspath(__file__))))
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

# from src.binprint import BinPrint
from binprint import BinPrint

class TestBinPrint(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def test_ascii(self):
        b = BinPrint(b'Hello World')
        b.print()

    def test_utf8(self):
        b = BinPrint('안녕하세요 가나다라마바사아차카타파하', encode='utf-8', width=8)
        b.print()
    
    def test_utf16(self):
        b = BinPrint('안녕하세요 가나다라마바사아차카타파하', encode='utf-16')
        b.print()

    def test_bindata(self):
        with open("./testimg.png", "rb") as f:
            b = BinPrint(f.read())
            b.print()

if __name__ == '__main__':
    unittest.main()