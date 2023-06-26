import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="LimpiezaDatos",
    version="0.1.0",
    description="Repositorio resumen del curso de Data Science",
    packages=setuptools.find_packages(),
    install_requires=requirements,
)