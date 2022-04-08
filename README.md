<h1>  🎲 Descomplicando a criação de pacotes de processamento de imagens em Python  </h1>
<p> Neste projeto você aprenderá a criar o seu primeiro pacote de processamento de imagens e disponibilizá-lo no repositório Pypi. Assim você pode reutilizá-lo e compartilhá-lo facilmente com outras pessoas. </p>
<br>

## Autora do Projeto: Karina Kato

### Aula: Descomplicando a criação de pacotes de processamento de imagens em Python

#### Tecnologia: Python

#### Data: 30/03/2022

## Image_Processing

The package "image_processing-test" is used to:

-   Processing:

    -   Histogram matching;
    -   Structural similarity;
    -   Resize image;

-   Utils:
    -   Read image;
    -   Save image;
    -   Plot image;
    -   Plot result;
    -   Plot Histogram;

---

## Installation

-   [x] Instalação das últimas versões de "setuptools" e "wheel"

```
py -m pip install --upgrade pip
py -m pip install --user setuptools wheel twine
```

-   [x] Tenha certeza que o diretório no terminal seja o mesmo do arquivo "setup.py"

```
py setup.py sdist bdist_wheel
```

-   [x] Após completar a instalação, verifique se as pastas abaixo foram adicionadas ao projeto:

    -   [x] build;
    -   [x] dist;
    -   [x] image_processing_test.egg-info.

-   [x] Basta subir os arquivos, usando o Twine, para o Test Pypi:

```
py -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

-   [x] Após rodar o comando acima no terminal, será pedido para inserir o usuário e senha. Feito isso, o projeto estará hospedado no Test Pypi.hospedá-lo no Pypi diretamente.
        Use the package manager [pip](https://pip.pypa.io/en/stable/) to install package_name

```bash
pip install python-pacotes-processamento-imagens
```

## Local Installation

-   [x] Instalação de dependências

```
pip install -r requirements.txt
```

-   [x] Instalção do Pacote

Use o gerenciador de pacotes `pip install -i https://test.pypi.org/simple/ image-processing-test `para instalar image_processing-test

```bash
pip install image-processing-test
```

---

