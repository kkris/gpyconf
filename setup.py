from distutils.core import setup

setup(
    name        = 'gpyconf',
    version     = '0.2beta',
    description = 'a modular Python configuration framework with support for multiple frontends and backends',
    author      = 'Kristoffer Kleine',
    author_email= 'kris.kleine@yahoo.de',
    url         = 'http://github.com/kkris/gpyconf',
    license     = '2-clause BSD | LGPL 2.1',
    packages    = ['gpyconf',
                   'gpyconf.frontends',
                        'gpyconf.frontends.gtk',
                   'gpyconf._internal',
                   'gpyconf.contrib',
                        'gpyconf.contrib.gtk',
                   'gpyconf.backends',
                        'gpyconf.backends._xml',
                   'gpyconf.fields'
                  ],
    package_data= {'gpyconf.frontends.gtk' : ['interface/*']}
)

