pkgs = ['pip',
		'geneticalgorithm',
        'pyswarms']

import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
        pip.main(['install', '--upgrade', package])
    else:
        pip._internal.main(['install', package])
        pip._internal.main(['install', '--upgrade', package])
     
for pkg in pkgs:
	install(pkg)