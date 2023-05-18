<script src="scripts/termynal/termynal.js" data-termynal-container="#termynal">

</script>
<img src="static/logo.svg">

# A quick way to start with machine and deep learning
[![python](https://img.shields.io/badge/-Python_3.10%7C3.11-blue?logo=python&logoColor=white)](https://www.python.org/downloads)

[![black](https://img.shields.io/badge/Code%20Style-Black-black.svg?labelColor=gray)](https://black.readthedocs.io/en/stable/)
[![isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/) 
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![pydocstyle](https://img.shields.io/badge/pydocstyle-enabled-AD4CD3)](http://www.pydocstyle.org/en/stable/)

[![license](https://img.shields.io/badge/License-MIT-green.svg?labelColor=gray)](https://github.com/opengeokube/ml-kit/blob/main/LICENSE)
</div>

## 🖋️ Authors
OpenGeokube Developers:
1. Jakub Walczak
1. Marco Macini
1. Mirko Stojiljkovic
1. Shahbaz Alvi

## 🎬 Quickstart

### Getting started

#### Installation
```bash
pip install mlkit
```

or

```bash
conda install ...
```

For contributing:
 
```text
git clone https://github.com/opengeokube/ml-kit
cd ml-kit
conda env create -f dev-env.yaml
pip install .
```

#### Preparing simple project
<div id="termynal" data-termynal>
    <span data-ty="input">mlflow init --name=my-new-project</span>
    <span data-ty>MLKit Creating a new skeleton for the project: << my-new-project >></span>
</div>


## 📜 Cite Us
```bibtex
@ONLINE{ml-kit,
  author = {Walczak, J., Mancini, M., Stojiljkovic, M., Alvi, S.},
  title = {{MLKit}: A quick way to start with machine and deep learning},
  year = 2023,
  url = {https://github.com/opengeokube/ml-kit},
  urldate = {<access date here>}
}
```