#!/usr/bin/python

from __future__ import print_function

from src.shader_lib import ShaderLib
from src.candle_holder import CandleHolder

class Renderer:
    def __init__(self, ri, args):
        self.ri = ri
        self.args = args

        self.integrator = { 'name': 'PxrPathTracer', 'params': {} }

        self.asset_dir_path = './assets/'
        self.texture_dir_path = self.asset_dir_path + 'textures/'
        self.render_dir_path = './render/'
        self.shaderLib = ShaderLib(ri, self.asset_dir_path)

    def setup_scene_description(self):
        ri = self.ri
        args = self.args

        ri.ArchiveRecord(ri.COMMENT, 'VERSION 0.0.1')
        ri.ArchiveRecord(ri.COMMENT, 'DESCRIPTION "Rendering A Candleholder"')

        self.shaderLib.load_multiple([
            'surface_body',
            # 'top_outer_ring',
            # 'top_inner_ring',
            # 'inner_surface',
            # 'inner_bottom',
            'table_shader'
        ])

        ri.Option('searchpath', { 'string texture': self.texture_dir_path })

        self._setup_display_elements()
        self._setup_integrator()

        print('shading rate {} \npixel variance {} \nusing {} {}'.format(
            args.shadingrate,
            args.pixelvar,
            self.integrator['name'],
            self.integrator['params'] or ''
        ))

        self._set_camera()
        self._setup_world()

    ####################
    # PRIVATE METHODS
    ####################

    def _setup_display_elements(self):
        ri = self.ri
        args = self.args

        ri.Display(
            self.render_dir_path + args.outname + '.exr',
            'it' if args.output == 'it' or args.output == 'rib' else 'openexr',
            'rgba'
        )
        ri.Format(args.width, args.height, 1) # 1920 x 1080

    def _setup_integrator(self):
        ri = self.ri
        args = self.args
        self.integrator = self._set_integrator()

        ri.Hider('raytrace', {
            'int incremental': [1],
            # 'string pixelfiltermode' : 'importance',
            # TODO: Should I need to reduce noise by setting sampling to 720?
            # 'int maxsamples': 720,
            # 'int minsamples': 720
        })
        ri.ShadingRate(args.shadingrate) # 0.1
        ri.PixelVariance(args.pixelvar) # Low pixel variance (0.01)
        ri.Integrator(self.integrator['name'], 'integrator', self.integrator['params']) # PxrPathTracer

    # Modified from Jon Macey's https://github.com/NCCA/Renderman
    def _set_integrator(self):
        args = self.args
        arg = args.default or args.vcm or args.direct or args.wire or args.normals or args.st or 0

        return {
            args.default : { 'name': 'PxrDefault',        'params': {} },
            args.vcm     : { 'name': 'PxrVCM',            'params': {} },
            args.direct  : { 'name': 'PxrDirectLighting', 'params': {} },
            args.wire    : { 'name': 'PxrVisualizer',     'params': { 'int wireframe': [1], 'string style': ['shaded'] } },
            args.normals : { 'name': 'PxrVisualizer',     'params': { 'int wireframe': [1], 'string style': ['normals'] } },
            args.st      : { 'name': 'PxrVisualizer',     'params': { 'int wireframe': [1], 'string style': ['st'] } }
        }.get(arg, self.integrator)

    """
    Camera
    
    """
    def _set_camera(self, focal_length = 1, focal_distance = 14, translate = None, rotate = None):
        ri = self.ri
        args = self.args

        tr = translate or [0, -1.5, focal_distance - 1]
        rt = rotate or [-20, 1, 0, 0]

        ri.Projection(ri.PERSPECTIVE, { ri.FOV: args.fov }) # FOV: 50
        ri.DepthOfField(focal_length * 2, focal_length, focal_distance)

        ri.Translate(tr[0], tr[1], tr[2])
        ri.Rotate(rt[0], rt[1], rt[2], rt[3])

    def _setup_world(self):
        ri = self.ri

        ri.WorldBegin()
        ri.TransformBegin()

        # HDRI Sourced from:
        # - https://hdrihaven.com/hdri/?c=urban&h=comfy_cafe
        # - https://hdrihaven.com/hdri/?c=night&h=fireplace
        self._set_environment_map('comfy_cafe_4k.tx')
        self._draw_scene()

        ri.TransformEnd()
        ri.WorldEnd()

    """
    Environment Map Light
    This method specifies the scene's environment lighting 
    and the portion of the environment to be visible to the scene
    
    """
    def _set_environment_map(self, env_map_file):
        ri = self.ri

        ri.ArchiveRecord(ri.COMMENT, '---- Begin of Lighting Group ----')
        ri.TransformBegin()
        # ri.Declare('domeLight' ,'string')

        ri.Rotate(-90, 1, 0, 0)
        ri.Rotate(110, 0, 0, 1)

        ri.Light('PxrDomeLight', 'domeLight', {
            'string lightColorMap': [env_map_file],
            'float exposure': [0],
            # 'float intensity' : [1.0],
        })
        ri.TransformEnd()
        ri.ArchiveRecord(ri.COMMENT, '---- End of Lighting Group ----')

    """
    Modelling & Shading
    
    """
    def _draw_scene(self):
        ri = self.ri
        candleHolder = CandleHolder(ri)

        candleHolder.draw()

        # self.shaderLib.use('test')