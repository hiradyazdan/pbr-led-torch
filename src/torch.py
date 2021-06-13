class Torch:
    def __init__(self, ri, rotate = None, translate = None, color = None):
        self.ri = ri
        self.theta_max_angle = 360

        self.rt_angle, \
        self.rt_x, \
        self.rt_y, \
        self.rt_z = rotate or [90, 1, 0 , 0]

        self.tr_x, \
        self.tr_y, \
        self.tr_z = translate or [-2, 2, -3.4]
        self.surface_color = color or [0.4, 0.4, 0.4]

    def draw(self):
        ri = self.ri

        ri.ArchiveRecord(ri.COMMENT, '---- Begin of Torch Group ----')
        self._draw_button_bumps()
        self._draw_button_pillow()
        self._draw_button_wall()
        self._draw_button_seat()

        self._draw_upper_ring()
        self._draw_main_body()
        self._draw_lower_body()
        ri.ArchiveRecord(ri.COMMENT, '---- End of Torch Group ----')

    ####################
    # PRIVATE METHODS
    ####################

    def _draw_button_bumps(self):
        ri = self.ri

        ri.AttributeBegin()
        ri.ArchiveRecord(ri.COMMENT, '-- Button Bumps --')
        ri.Attribute( 'identifier', { 'name': 'button-bumps' })

        ri.Attribute('displacementbound', {
            'sphere': [1],
            'coordinatesystem': ['object']
        })

        ri.Pattern('button_bumps', 'buttonTx', {
            'float frequency': [50],
            'float radius': [.4],
            'float fuzz': [0]
        })
        ri.Displace('PxrDisplace', 'domeDisp', {
            'float dispAmount': [.1],
            'reference float dispScalar': ['buttonTx:resultF']
        })
        ri.Bxdf('PxrDisney', 'dome', {
            'color baseColor': [0.1, 0.1, 0.1]
        })

        ri.TransformBegin()

        ri.Rotate(self.rt_angle, self.rt_x, self.rt_y, self.rt_z)
        ri.Translate(self.tr_x, self.tr_y, self.tr_z - .04)
        ri.Paraboloid(.72, 0, .3, self.theta_max_angle)

        ri.TransformEnd()

        ri.AttributeEnd()

    def _draw_button_pillow(self):
        ri = self.ri

        ri.AttributeBegin()
        ri.ArchiveRecord(ri.COMMENT, '-- Button Pillow --')
        ri.Attribute( 'identifier', { 'name': 'button-pillow' })

        ri.Bxdf('PxrDisney', 'bxdf_label', {
            'color baseColor': [0, 0, 0],
            'float metallic': [0]
        })

        ri.TransformBegin()

        ri.Rotate(self.rt_angle, self.rt_x, self.rt_y, self.rt_z)
        ri.Translate(self.tr_x, self.tr_y, self.tr_z - .05)
        ri.Paraboloid(.8, 0, .3, self.theta_max_angle)

        ri.TransformEnd()

        ri.AttributeEnd()

    def _draw_button_wall(self):
        ri = self.ri

        ri.AttributeBegin()
        ri.ArchiveRecord(ri.COMMENT, '-- Button Wall --')
        ri.Attribute( 'identifier', { 'name': 'button-wall' })

        ri.Bxdf('PxrDisney', 'bxdf_label', {
            'color baseColor': [0.1, 0.1, 0.1],
            "float metallic" : [0]
        })

        ri.TransformBegin()

        ri.Rotate(self.rt_angle, self.rt_x, self.rt_y, self.rt_z)
        ri.Translate(self.tr_x, self.tr_y, self.tr_z - .6) # z = -4.05
        ri.Cylinder(.8, .85, 1, self.theta_max_angle)

        ri.TransformEnd()

        ri.AttributeEnd()

    def _draw_button_seat(self):
        ri = self.ri

        ri.AttributeBegin()
        ri.ArchiveRecord(ri.COMMENT, '-- Button Seat --')
        ri.Attribute( 'identifier', { 'name': 'button-seat' })

        ri.Bxdf('PxrDisney', 'bxdf_label', {
            'color baseColor': self.surface_color,
            'float metallic': [0.5]
        })

        ri.TransformBegin()

        ri.Rotate(self.rt_angle, self.rt_x, self.rt_y, self.rt_z)
        ri.Translate(self.tr_x, self.tr_y, self.tr_z + .3)
        ri.Disk(0, 1, self.theta_max_angle)

        ri.TransformEnd()

        ri.AttributeEnd()

    def _draw_upper_ring_cap(self, translate_z):
        ri = self.ri

        ri.AttributeBegin()
        ri.ArchiveRecord(ri.COMMENT, '-- Upper Ring Ridge --')
        ri.Attribute( 'identifier', { 'name': 'upper-ring-ridge' })

        ri.Bxdf('PxrDisney', 'bxdf_label', {
            'color baseColor': self.surface_color,
            'float metallic': [1]
        })

        ri.TransformBegin()

        ri.Rotate(self.rt_angle, self.rt_x, self.rt_y, self.rt_z)
        ri.Translate(self.tr_x, self.tr_y, translate_z)
        ri.Disk(0, 1.03, self.theta_max_angle)

        ri.TransformEnd()

        ri.AttributeEnd()

    def _draw_upper_ring(self):
        ri = self.ri

        self._draw_upper_ring_cap(self.tr_z + .6)

        ri.AttributeBegin()
        ri.ArchiveRecord(ri.COMMENT, '-- Upper Ring --')
        ri.Attribute( 'identifier', { 'name': 'upper-ring' })

        ri.Attribute('displacementbound', {
            'sphere': [1],
            'coordinatesystem': ['object']
        })

        ri.Pattern('ring_displace', 'upperRingTx')
        ri.Displace('PxrDisplace', 'myDisp', {
            'float dispAmount': [.1],
            'reference float dispScalar': ['upperRingTx:resultF']
        })
        ri.Bxdf('PxrDisney', 'bxdf_label', {
            'color baseColor': self.surface_color,
            'float metallic': [.9]
        })

        ri.TransformBegin()

        ri.Rotate(self.rt_angle, self.rt_x, self.rt_y, self.rt_z)
        ri.Translate(self.tr_x, self.tr_y, self.tr_z - .3) # z = -3.7
        ri.Cylinder(1, .9, 2, self.theta_max_angle)

        ri.TransformEnd()

        ri.AttributeEnd()

    def _draw_main_body(self):
        ri = self.ri

        ri.AttributeBegin()
        ri.ArchiveRecord(ri.COMMENT, '-- Main Body --')
        ri.Attribute( 'identifier', { 'name': 'main-body' })

        # ri.Attribute('displacementbound', {
        #     'sphere': [1],
        #     'coordinatesystem': ['object']
        # })

        ri.Pattern('body_shaft', 'shaft', {
            # 'float repeatU': [10],
            # 'float repeatV': [3],
            # 'float radius': [0.2],
            'color surfaceColor': self.surface_color,
            # 'color diskColor': [1, 1, 1]
        })
        # ri.Displace('PxrDisplace', 'myDisp', {
        #     'float dispAmount': [12],
        #     'reference float dispScalar': ['diskTx:resultF']
        # })
        ri.Bxdf('PxrDisney', 'bxdf_label', {
            'reference color baseColor': ['shaft:outColor'],
            "float metallic" : [1]
        })

        ri.TransformBegin()

        ri.Rotate(self.rt_angle, self.rt_x, self.rt_y, self.rt_z)
        ri.Translate(self.tr_x, self.tr_y, self.tr_z - .6) # z = -4
        ri.Cylinder(1, .9, 6, self.theta_max_angle)

        ri.TransformEnd()

        ri.AttributeEnd()

    def _draw_lower_body(self):
        ri = self.ri

        self._draw_upper_ring_cap(self.tr_z + 4.9) # 1.5

        ri.AttributeBegin()
        ri.ArchiveRecord(ri.COMMENT, '-- Lower Body --')
        ri.Attribute( 'identifier', { 'name': 'lower-body' })

        ri.Attribute('displacementbound', {
            'sphere': [.5],
            'coordinatesystem': ['object']
        })

        ri.Pattern('ring_displace', 'lowerRingTx')
        # ri.Pattern('body_lower', 'torchBody', {
        #     'float repeatU': [10],
        #     'float repeatV': [3],
        #     'float fuzz': [0],
        #     'float radius': [0.2],
        #     'color surfaceColor': self.surface_color,
        #     'color diskColor': [1, 1, 1]
        # })
        ri.Displace('PxrDisplace', 'myDisp', {
            'float dispAmount': [.1],
            'reference float dispScalar': ['lowerRingTx:resultF']
        })
        ri.Bxdf('PxrDisney', 'bxdf_label', {
            'color baseColor': self.surface_color,#['torchBody:outColor'],
            'float metallic': [1]
        })

        ri.TransformBegin()

        ri.Rotate(self.rt_angle, self.rt_x, self.rt_y, self.rt_z)
        ri.Translate(self.tr_x, self.tr_y, self.tr_z + 3.9) # z = .5
        ri.Cylinder(1.01, 1, 3.4, self.theta_max_angle)

        ri.TransformEnd()

        ri.AttributeEnd()