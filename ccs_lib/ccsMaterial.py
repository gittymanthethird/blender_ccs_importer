from .utils.PyBinaryReader.binary_reader import *

class ccsMaterial(BrStruct):
    def __init__(self):
        self.name = ''
        self.type = "Material"
        self.path = ''
        self.alpha = 1
        self.offsetX = 0
        self.offsetY = 0
        self.scaleX = 1
        self.scaleY = 1
        self.texture = None
    def __br_read__(self, br: BinaryReader, indexTable, version):
        self.index = br.read_uint32()
        self.name = indexTable.Names[self.index][0]
        self.path = indexTable.Names[self.index][1]

        self.textureIndex = br.read_uint32()
        self.alpha = br.read_float()
        if version > 0x130:
            self.offsetX = br.read_int16() / 4096
            self.offsetY = br.read_int16() / 4096
            self.scaleX = br.read_int16() / 4096
            self.scaleY = br.read_int16() / 4096
            values = br.read_int32(18)
        elif version == 0x130:
            self.offsetX = br.read_int16() / 4096
            self.offsetY = br.read_int16() / 4096
            self.scaleX = br.read_int16() / 4096
            self.scaleY = br.read_int16() / 4096
            values = br.read_int32(9)
        elif version < 0x130 and version > 0x120:
            self.offsetX = br.read_int16() / 4096
            self.offsetY = br.read_int16() / 4096
            self.scaleX = br.read_int16() / 4096
            self.scaleY = br.read_int16() / 4096
        else:
            self.offsetX = br.read_int16() / 4096
            self.offsetY = br.read_int16() / 4096


    def finalize(self, chunks):
        self.texture = chunks.get(self.textureIndex)
