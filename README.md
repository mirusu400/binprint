# binprint
Simple package to pretty print binary data in python

# Installation
```
pip install binprint
```

# Usage


### Hex dump from raw text
```python
import binprint

b = binprint.BinPrint("Hello world")
b.print()
```

### Hex dump from file
```python
import binprint

with open("./tests/testing.png", "rb") as f:
    b = binprint.BinPrint(f.read())
    b.print()
```





