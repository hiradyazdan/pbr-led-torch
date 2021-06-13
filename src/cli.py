import argparse

# Modified from Jon Macey's https://github.com/NCCA/Renderman
def cli_args():
    parser = argparse.ArgumentParser(description='Modify Render Parameters for CandleHolder')

    parser.add_argument('--shadingrate', '-s',
                        nargs='?', const=0.1,             default=0.1,            type=float, help='shading rate default to 0.1')
    parser.add_argument('--pixelvar',    '-p',
                        nargs='?', const=0.01,            default=0.01,           type=float, help='pixel variance default 0.01')
    parser.add_argument('--fov',         '-fv',
                        nargs='?', const=50.0,            default=90.0,           type=float, help='projection fov default 50.0')
    parser.add_argument('--width',       '-wd',
                        nargs='?', const=1920,            default=1920,           type=int,   help='width of image default 1920')
    parser.add_argument('--height',      '-ht',
                        nargs='?', const=1080,            default=1080,           type=int,   help='height of image default 1080')
    parser.add_argument('--output',      '-o',
                        nargs='?', const='it',            default='it',           type=str,   help='output type default it')
    parser.add_argument('--outname',     '-on',
                        nargs='?', const='scene',         default='scene',        type=str,   help='output name default scene')
    parser.add_argument('--ribfile',     '-rb',
                        nargs='?', const='scene',         default='scene',        type=str,   help='rib file default scene.rib')

    parser.add_argument('--rib',     '-r', action='count', help='render to rib not framebuffer')
    parser.add_argument('--default', '-d', action='count', help='use PxrDefault')
    parser.add_argument('--vcm',     '-v', action='count', help='use PxrVCM')
    parser.add_argument('--direct',  '-t', action='count', help='use PxrDirect')
    parser.add_argument('--wire',    '-w', action='count', help='use PxrVisualizer with wireframe shaded')
    parser.add_argument('--normals', '-n', action='count', help='use PxrVisualizer with wireframe and Normals')
    parser.add_argument('--st',      '-u', action='count', help='use PxrVisualizer with wireframe and ST')

    return parser.parse_args()