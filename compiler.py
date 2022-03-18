from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
ext_modules = [
    Extension("main_app", ["main_app.py"]),
    Extension("sub", ["sub.py"]),
    Extension("fahmy", ["fahmy.py"]),
]
setup(name='Cython App',
      cmdclass={'build_ext': build_ext},
      ext_modules=cythonize(ext_modules),
      compiler_directives={'language_level': 3},
      zip_safe=False
      )

