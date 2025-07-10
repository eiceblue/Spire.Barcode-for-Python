from spire.barcode import *


# Function to write all text to a file
def WriteAllText(fpath: str, content: str):
    # Open the file in write mode with UTF-8 encoding
    with open(fpath, 'w', encoding='utf-8') as fp:
        # Write the content to the file
        fp.write(content)

# Use BarcodeScanner class to scan a file and include checksum
strCode = BarcodeScanner.ScanOneFileWithIncludeCheckSum("data/barcode1.png",True)

# Write the scanned string to a text file
WriteAllText("ScanOneFileWithIncludeCheckSum.txt",strCode)