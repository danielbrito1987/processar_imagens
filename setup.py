from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="processar_imagens",
    version="0.0.1",
    author="Daniel Brito",
    author_email="damasceno1871@gmail.com",
    description="Pacote para processamento de imegens",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/danielbrito1987/processar_imagens",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)