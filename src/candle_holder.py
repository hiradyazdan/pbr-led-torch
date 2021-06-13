class CandleHolder:
    def __init__(self, ri):
        self.ri = ri

    def draw(self):
        ri = self.ri

        ri.ArchiveRecord(ri.COMMENT, '---- Begin of Candleholder Group ----')
        ri.AttributeBegin()

        self._draw_stripes(100, 'outer-surface')

        theta_max_angle = 360

        # Outer Surface
        ri.ArchiveRecord(ri.COMMENT, '-- Outer Surface --')
        ri.TransformBegin()

        ri.Rotate(-90, 1, 0, 0)
        ri.Translate(0, -2, -.67)

        ri.Scale(1, 1, 2.3)
        ri.Sphere(2, -1.4, 0.3, theta_max_angle)

        ri.TransformEnd()

        # Top Outer Ring
        ri.ArchiveRecord(ri.COMMENT, '-- Top Outer Ring --')
        ri.TransformBegin()

        ri.Rotate(90, 1, 0, 0)
        ri.Translate(0, 2, -.71)
        # ri.Scale(1, 1, 1)
        ri.Paraboloid(2, .35, .7, theta_max_angle)
        # ri.Sphere(2, -1.4, 0.3, theta_max_angle)

        ri.TransformEnd()

        self._draw_stripes(60, 'inner-surface')

        # Inner Surface
        ri.ArchiveRecord(ri.COMMENT, '-- Inner Surface --')
        ri.TransformBegin()

        ri.Rotate(90, 1, 0, 0)
        ri.Translate(0, 2, -1.3)

        ri.Cylinder(1.34, 1, 3, theta_max_angle)

        # Top Inner Ring
        ri.ArchiveRecord(ri.COMMENT, '-- Top Inner Ring --')
        ri.Rotate(180, 1, 0, 0)
        ri.Translate(0, 0, -2.02)

        ri.Paraboloid(1.41, 1, 1.1, theta_max_angle)
        ri.TransformEnd()

        ri.AttributeEnd()
        ri.ArchiveRecord(ri.COMMENT, '---- End of Candleholder Group ----')

    def _draw_stripes(
        self,
        repeat_count, bxdf_label,
        surface_color = None, stripe_color = None
    ):
        ri = self.ri

        ri.Attribute( 'identifier', { 'name': '' })

        ri.Attribute('displacementbound', {
            'sphere': [1],
            'coordinatesystem': ['object']
        })

        ri.Pattern('surface_body', 'surfaceBody', {
            'int stripeCount': repeat_count,
            'color surfaceColor': surface_color or [.2, 0.02, 0],
            'color stripeColor': stripe_color or [.2, 0, 0]
        })
        # ri.Displace('PxrDisplace', 'myDisp', {
        #     'float dispAmount': [12],
        #     'reference float dispScalar': ['diskTx:resultF']
        # })
        ri.Bxdf('PxrDisney', bxdf_label, {
            'reference color baseColor': ['surfaceBody:outColor']
        })

        # ri.Attribute('trace', {
        #     'constant int maxspeculardepth': [6]
        # })
        # ri.Attribute('visibility', {
        #     'constant int transmission': [1],
        #     'constant int indirect': [1]
        # })
        # ri.Bxdf('PxrLMGlass', 'glass', {
        #     'color reflectionColor': [0.4891, 0.7303, 0.7759],
        #     'color refractionColor': [0.9, 0.9, 0.9],
        #     'int shadows': [1]
        # })

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