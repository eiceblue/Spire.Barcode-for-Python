from spire.barcode import *

# Function to write all bytes to a file
def WriteAllBytes(fname: str, data):
    with open(fname, "wb") as fp:
        fp.write(data)
    fp.close()


# Create an instance of BarcodeSettings
barcodeSettings = BarcodeSettings()

# Set the type of barcode to Codabar
barcodeSettings.Type = BarCodeType.DeutschePostIdentcode

# Set the data for the barcode
barcodeSettings.Data = "12345"

# Create an instance of BarCodeGenerator with the specified settings
barCodeGenerator = BarCodeGenerator(barcodeSettings)

# Generate the image for the barcode
barcodeimage = barCodeGenerator.GenerateImage()

# Write the PNG image to disk
WriteAllBytes("DeutschePostIdentcode.png", barcodeimage)
