from __future__ import print_function
import sys, os, subprocess

# Modified from Jon Macey's https://github.com/NCCA/Renderman
def loadShader(shader) :
    shaders_dir_path = '../assets/shaders/'
    if os.path.isfile(shaders_dir_path + shader + '.oso') != True or \
            os.stat(shaders_dir_path + shader + '.osl').st_mtime - os.stat(shaders_dir_path + shader + '.oso').st_mtime > 0:
        print('compiling shader %s' %(shader))

        try:
            subprocess.check_call([
                'oslc',
                '-o', shaders_dir_path + shader + '.oso',
                      shaders_dir_path + shader + '.osl'
            ])
        except subprocess.CalledProcessError:
            sys.exit('shader compilation failed')