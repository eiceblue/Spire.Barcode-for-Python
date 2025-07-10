from spire.barcode import *

# Function to append all lines of text to a file
def AppendAllText(fname: str, text: List[str]):
    # Open the file in write mode
    fp = open(fname, "w")

    # Iterate over each line of text
    for s in text:
        # Write the line to the file
        fp.write(s)

    # Close the file handle
    fp.close()

# Use BarcodeScanner class to scan a file and include checksum with the specified barcode type    
strCode = BarcodeScanner.ScanFileBarCodeTypeIncludeCheckSum("data/barcode1.png", BarCodeType.Code128, True)

# Append all scanned strings to a text file
AppendAllText("ScanFileBarCodeTypeIncludeCheckSum.txt", strCode)