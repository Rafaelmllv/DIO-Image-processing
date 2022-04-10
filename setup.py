from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-rafael",
    version="0.0.1",
    author="Rafael Vieira",
    author_email="rafaelmllv@gmail.com",
    description="Pacote desenvolvido pela professora Karina Kato, para processamento de imagens e demonstração da criação de um pacote python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeffersonk97/python-pacotes-processamento-imagens",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)