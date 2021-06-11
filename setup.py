from setuptools import setup

classifiers = [
                  'Intended Audience :: Graphics Programmers',
                  'License :: OSI Approved :: MIT License',
                  'Operating System :: POSIX'
              ] + [
                  ('Programming Language :: Python :: %s' % x)
                  for x in '2.7'.split()
              ]

test_requirements = [
    'prman'
]

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='candleholder',
    version='0.0.1',
    description='A candleholder renderer with Renderman',
    long_description=long_description,
    url='',
    author='Hirad Yazdanpanah',
    author_email='s5320619@bournemouth.ac.uk',
    license='MIT',
    platforms=["windows"],
    packages=['candleholder'],
    entry_points={
        'console_scripts': [
            'amphc=amplifyhealthcheck.cli:init_cli'
        ]
    },
    classifiers=classifiers,
    keywords="nginx amplify nginx-amplify nginx-configuration health-check metrics",
    install_requires=[
        'prman'
    ],
    setup_requires=['pytest-runner'],
    tests_require=test_requirements,
    extras_require={
        'test': test_requirements,
    },
    python_requires='==2.7.*',
    zip_safe=False
)