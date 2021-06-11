class CandleHolder:
    def __init__(self, ri):
        self.ri = ri

    def draw(self):
        ri = self.ri

        ri.ArchiveRecord(ri.COMMENT, '---- Begin of Candleholder Group ----')
        ri.AttributeBegin()
        ri.Attribute( 'identifier', { 'name': '' })

        ri.Attribute('displacementbound', {
            'sphere': [1],
            'coordinatesystem': ['object']
        })

        self._draw_stripes(100, 'outer-surface')
        # ri.Displace("PxrDisplace", "disp", {
        #     "float dispAmount": [0.03],
        #     "reference float dispScalar": ["diskTx:resultD"]
        # })

        theta_max_angle = 360

        # Outer Surface
        ri.ArchiveRecord(ri.COMMENT, '-- Outer Surface --')
        ri.TransformBegin()

        ri.Rotate(-90, 1, 0, 0)
        ri.Translate(0, -2, 0)

        ri.Scale(1, 1, 2.8)
        ri.Sphere(2, -1.4, 0.3, theta_max_angle)

        ri.TransformEnd()

        # Top Outer Ring
        ri.ArchiveRecord(ri.COMMENT, '-- Top Outer Ring --')
        ri.TransformBegin()

        ri.Rotate(90, 1, 0, 0)
        ri.Translate(0, 2, -1.53)
        # ri.Scale(1, 1, 1)
        ri.Paraboloid(2, .35, .7, theta_max_angle)
        # ri.Sphere(2, -1.4, 0.3, theta_max_angle)

        ri.TransformEnd()

        self._draw_stripes(20, 'inner-surface')

        # Inner Surface
        ri.ArchiveRecord(ri.COMMENT, '-- Inner Surface --')
        ri.TransformBegin()

        ri.Rotate(90, 1, 0, 0)
        ri.Translate(0, 2, -2.1)

        ri.Cylinder(1.34, 1, 2, theta_max_angle)

        # Top Inner Ring
        ri.ArchiveRecord(ri.COMMENT, '-- Top Inner Ring --')
        ri.Rotate(180, 1, 0, 0)
        ri.Translate(0, 0, -2.02)

        ri.Paraboloid(1.41, 1, 1.1, theta_max_angle)
        ri.TransformEnd()

        ri.AttributeEnd()
        ri.ArchiveRecord(ri.COMMENT, '---- End of Candleholder Group ----')

        ri.ArchiveRecord(ri.COMMENT, '---- Begin of Table Group ----')
        ri.AttributeBegin()
        ri.Attribute('identifier', { 'name': 'table-surface' })
        # shader

        ri.Pattern('table_shader', 'tableShader', {
            'string fileName': ['./assets/textures/table.tex']
        })
        ri.Bxdf('PxrDisney', 'woodTexture', {
            'reference color baseColor' : [ 'tableShader:outTexture' ],
            # 'int diffuseDoubleSided' : [1],
            # 'float reflectionGain' : [0.2]
        })

        DiscRadius2 = 6

        ri.TransformBegin()

        ri.Translate(0,-3.85,0)
        ri.Scale(DiscRadius2,DiscRadius2,DiscRadius2)
        ri.Rotate(-90,1,0,0)
        ri.Disk(0,1,360)

        ri.TransformEnd()

        ri.TransformBegin()

        # ri.Translate(0,-3.85,0)
        # ri.Rotate(-90,1,0,0)
        # ri.Cylinder (6, -1, 0, 360)

        ri.TransformEnd()
        ri.AttributeEnd()
        ri.ArchiveRecord(ri.COMMENT, '---- End of Table Group ----')

    def _draw_stripes(
        self,
        repeat_count, bxdf_label,
        surface_color = None, stripe_color = None
    ):
        ri = self.ri

        ri.Pattern("surface_body", "surfaceBody", {
            'int repeatCount': repeat_count,
            'color surfaceColor': surface_color or [1, 0.9, 0.1],
            'color stripeColor': stripe_color or [0.4, 0.9, 0.1],
        })
        # ri.Displace('PxrDisplace', 'myDisp', {
        #     'float dispAmount': [12],
        #     'reference float dispScalar': ['diskTx:resultF']
        # })
        ri.Bxdf('PxrDisney', bxdf_label, {
            'reference color baseColor': ['surfaceBody:outColor']
        })

    def _draw_round_surface(self, scale, sphere):
        ri = self.ri
        x_scale, y_scale, z_scale = scale
        radius, z_min, z_max, theta_max_angle = sphere

        ri.TransformBegin()

        ri.Rotate(-90, 1, 0, 0)
        ri.Translate(0, -2, 0)

        ri.Scale(x_scale, y_scale, z_scale)
        ri.Sphere(radius, z_min, z_max, theta_max_angle)

        ri.TransformEnd()

    def _draw_top_surface(self, theta_max_angle):
        ri = self.ri

        ri.TransformBegin()

        ri.Rotate(90, 1, 0, 0)
        ri.Translate(0, 10, 0)
        ri.Paraboloid(4, .7, .3, theta_max_angle)

        ri.TransformEnd()

    def _scale(self, x, y, z):
        ri = self.ri

        ri.Scale(x, y, z)