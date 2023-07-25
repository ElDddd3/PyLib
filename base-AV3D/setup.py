from setuptools import setup, find_packages

VERSION = '2.1.0'
DESCRIPTION = 'Este paquete posee un conjuento de dos que se llaman "Area2D" y "Volumen3D"'
LONG_DESCRIPTION = ''

# Configurando
setup(
    name="AV3D",
    version=VERSION,
    author="El_Dddd",
    author_email="<eldddd67@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[

    ],  # añade cualquier paquete adicional que debe ser
    # instalado junto con tu paquete. Ej: 'caer'

    keywords=['python', 'Math', "Geometry", "Pylib"],
    classifiers=[
        "Development Status :: 2 - Beta",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ])
