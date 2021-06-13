class Table:
    def __init__(self, ri):
        self.ri = ri

    def draw(self):
        ri = self.ri

        ri.ArchiveRecord(ri.COMMENT, '---- Begin of Table Group ----')
        ri.AttributeBegin()
        ri.Attribute('identifier', { 'name': 'table-surface' })

        ri.Pattern('table_shader', 'tableShader', {
            'color inColor': [1, 1, 1],
            'string fileName': ['./assets/textures/wood.tx']
        })
        ri.Bxdf('PxrDisney', 'woodTexture', {
            'reference color baseColor' : [ 'tableShader:outTexture' ],
            # 'int diffuseDoubleSided' : [1],
            # 'float reflectionGain' : [0.2]
        })

        ri.TransformBegin()

        ri.Translate(0,-3.9,2)
        ri.Scale(15, 15, 15)
        ri.Rotate(-90,1,0,0)
        ri.Disk(0, 1, 360)

        ri.TransformEnd()
        ri.AttributeEnd()
        ri.ArchiveRecord(ri.COMMENT, '---- End of Table Group ----')