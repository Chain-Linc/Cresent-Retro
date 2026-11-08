# README: Aseprite Required!!! Make Sure to add aseprite install folder to your path
# Pillow also required: `pip install Pillow`

import json
import subprocess
from PIL import Image

ART_FOLDER = "Art/"
RENDERED_FOLDER = "Tools/Rendered/"

INDEX_TRANSPARENT = 0
INDEX_OFFSET = -1
INDEX_BACKGROUND = 0

def pixels2Bytearray(pixels, bitDepth):
    # bytearray = [0x00, 0x01, 0x02... ]
    pairsPerByte = 8 // bitDepth
    pixelsPaired = []
    
    # pair pixels
    for i in range(0, len(pixels), pairsPerByte):
        pixelsPaired.append([])
        for j in range(pairsPerByte):
            pixelsPaired[-1].append(pixels[i+j])

    bytes = []
    for pair in pixelsPaired:
        byte = 0
        for number in pair:
            byte = (result << number) | bitDepth
        bytes.append(byte)

    retBytearray = ""
    for byte in bytes:
        retBytearray += byte + ", "
    retBytearray.

    print(pixelsPaired)

    return retBytearray

def pillow2Bytearray(file):
    flatSequenceRaw = [i for i in file.get_flattened_data()]

    file2bit = []
    fileMask = []
    for pixel in flatSequenceRaw:
        if pixel == INDEX_TRANSPARENT:
            file2bit.append(0)
            fileMask.append(0)
        else:
            file2bit.append(pixel+INDEX_OFFSET)
            fileMask.append(1)


    return pixels2Bytearray(file2bit, 2), pixels2Bytearray(fileMask, 1)


print("Started converting")

with open("Tools/convertArtImport.json", "r") as list:
    fileList = json.load(list)

print("Convert list loaded")

saveFileList = []

for filepath in fileList:
    getFilePath = ART_FOLDER + filepath
    saveFilePath = RENDERED_FOLDER + filepath.removesuffix(".aseprite") + "1.png"
    result = subprocess.run(["aseprite", "-b", "--color-mode", "indexed", getFilePath, "--save-as", saveFilePath], capture_output=True, text=True)

    saveFileList.append(saveFilePath)
    print(getFilePath, "is aseprite processed and saved to:", saveFilePath)

print("All files aseprite processed")


for filePath in saveFileList:
    pillowFile = Image.open(filePath)
    pixels2bit, pixelsMask = pillow2Bytearray(pillowFile)
    print("2bit:", pixels2bit, "\n1bit:", pixelsMask)