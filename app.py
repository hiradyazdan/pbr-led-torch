#!/usr/bin/python

from prman import Ri

from src.cli import cli_args as args
from src.renderer import Renderer

def main(args):
    ri = Ri()
    renderer = Renderer(ri, args)

    ri.Option('rib', { 'string asciistyle': 'indented' })
    ri.Begin(args.rib and renderer.asset_dir_path + args.ribfile + '.rib' or '__render')

    renderer.setup_scene_description()

    ri.End()

if __name__ == '__main__':
    main(args())
