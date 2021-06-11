import sys, os, subprocess

# Modified from Jon Macey's https://github.com/NCCA/Renderman
class ShaderLib:
    def __init__(self, ri, shaders_root_dir = './'):
        self.dir_path = shaders_root_dir + 'shaders/'
        self.compiled_dir_path = self.dir_path + 'compiled/'
        self.compiler = 'oslc'
        self.file_ext = '.osl'
        self.obj_ext  = '.oso'

        self.ri = ri

    def load_multiple(self, shaders):
        for shader in shaders:
            self.load(shader)

    def load(self, shader_name):
        ri = self.ri
        compiled_dir_path = self.compiled_dir_path

        ri.Option('searchpath', { 'string shader': compiled_dir_path })

        if self._is_compiled(shader_name) != True or self._is_changed(shader_name) > 0:
            print('compiling shader %s' %(shader_name))

            try:
                subprocess.check_call([
                    self.compiler,
                    '-o', compiled_dir_path + shader_name + self.obj_ext,
                          self.dir_path + shader_name + self.file_ext
                ])
            except subprocess.CalledProcessError:
                sys.exit('shader compilation failed')

    def use(self, file_name, name, params = None):
        ri = self.ri

        ri.Pattern(file_name, name, params or {})
        ri.Bxdf('PxrSurface', '') # material

####################
# PRIVATE METHODS
####################

    def _is_compiled(self, shader_name):
        return os.path.isfile(self.compiled_dir_path + shader_name + self.obj_ext)

    def _is_changed(self, shader_name):
        shader_path = self._get_shader_path(shader_name)
        obj_path = self._get_obj_path(shader_name)

        return self._get_mod_stat(shader_path) - self._get_mod_stat(obj_path)

    def _get_shader_path(self, shader_name):
        return self.dir_path + shader_name + self.file_ext

    def _get_obj_path(self, shader_name):
        return self.compiled_dir_path + shader_name + self.obj_ext

    def _get_mod_stat(self, file_path):
        return os.stat(file_path).st_mtime