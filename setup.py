import setuptools

def parse_requirements(filename):
	lines = (line.strip() for line in open(filename))
	return [line for line in lines if line and not line.startswith("#")]

setuptools.setup(
    name="LimpiezaDatos",
    version="0.1.0",
    description="Paquete con las funciones y clases de limpieza de datos y modelos del curso",
    packages=setuptools.find_packages(),
    install_requires=parse_requirements('requirements.txt'),
)
