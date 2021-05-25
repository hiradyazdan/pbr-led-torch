#!/usr/bin/python

# from __future__ import

from prman import Ri
import shader_helpers
from cli import cli_args as args

def draw(ri):
    ""

def set_lighting(ri):
    ri.TransformBegin()
    ri.AttributeBegin()
    ri.Declare('domeLight' ,'string')

    ri.Translate(0,0,40)
    ri.Rotate(-90,1,0,0)
    ri.Rotate(100,0,0,1)

    ri.Light(
        'PxrDomeLight',
        'domeLight',
        {
            'string lightColorMap': [
                '../assets/textures/hdr_4k.tx'
            ]
        }
    )
    ri.AttributeEnd()
    ri.TransformEnd()

# Modified from Jon Macey's https://github.com/NCCA/Renderman
def set_integrator(args):
    integrator = { 'name': 'PxrPathTracer', 'params': {} }
    arg = args.default or args.vcm or args.direct or args.wire or args.normals or args.st or 0

    return {
        args.default : { 'name': 'PxrDefault',        'params': {} },
        args.vcm     : { 'name': 'PxrVCM',            'params': {} },
        args.direct  : { 'name': 'PxrDirectLighting', 'params': {} },
        args.wire    : { 'name': 'PxrVisualizer',     'params': { 'int wireframe': [1], 'string style': ['shaded'] } },
        args.normals : { 'name': 'PxrVisualizer',     'params': { 'int wireframe': [1], 'string style': ['normals'] } },
        args.st      : { 'name': 'PxrVisualizer',     'params': { 'int wireframe': [1], 'string style': ['st'] } }
    }.get(arg, integrator)

def setup_integrator(ri, args):
    integrator = set_integrator(args)

    ri.Hider('raytrace', { 'int incremental': [1] })
    ri.ShadingRate(args.shadingrate)
    ri.PixelVariance(args.pixelvar)
    ri.Integrator(integrator['name'], 'integrator', integrator['params'])

def setup_display_elements(ri, args):
    ri.Display(
        '../render/' + args.outname + '.exr',
        'it' if args.output == 'it' or args.output == 'rib' else 'openexr',
        'rgba'
    )
    ri.Format(args.width, args.height, 1)

def setup_world(ri, args):
    ri.Projection(ri.PERSPECTIVE, { ri.FOV: args.fov })

    ri.WorldBegin()
    ri.TransformBegin()

    set_lighting(ri)
    draw(ri)

    ri.TransformEnd()
    ri.WorldEnd()

def main(args):
    ri = Ri()
    ri.Option('rib', { 'string asciistyle': 'indented' })

    ri.Begin(args.rib or '__render')

    setup_display_elements(ri, args)
    setup_integrator(ri, args)
    setup_world(ri, args)

    ri.End()

if __name__ == '__main__':
    shader_helpers.loadShader('test')

    main(args())
