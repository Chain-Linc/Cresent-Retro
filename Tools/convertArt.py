# README: Make Sure to install py_aseprite
# pip install git+https://github.com/Eiyeron/py_aseprite

import json
from aseprite import AsepriteFile

ART_FOLDER = "Art/"
INDEX_TRANSPARENT = 0
INDEX_OFFSET = -1
INDEX_BACKGROUND = 0

def pixels2Bytearray(pixels, bitDepth):
    # bytearray = [0x00, 0x01, 0x02... ]
    retBytearray = ""

    pairsPerByte = 8 // bitDepth

    pixelsPaired = []
    
    # pair pixels
    for i in range(0, pixels // pairsPerByte, pairsPerByte):
        pixelsPaired.append([])
        for j in range(pairsPerByte):
            pixelsPaired[-1].append(j)

    print(pixelsPaired)

    return retBytearray

def aseprite2Bytearray(file):
    flatSequenceRaw = []
    for frame in file.frames:
        for chunk in frame.chunks:
            # 0x2005 = chunk type for a Cel
            if chunk.chunk_type == 0x2005:
                rawPixelIndices = chunk.data['data']
                flatSequenceRaw.extend(list(rawPixelIndices))

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

with open("Tools/convertArtImport.json", "r") as list:
    fileList = json.load(list)

for filepath in fileList:
    with open(ART_FOLDER + filepath, 'rb') as f:
        asepriteData = AsepriteFile(f.read())
        pixels2bit, pixelsMask = aseprite2Bytearray(asepriteData)

        