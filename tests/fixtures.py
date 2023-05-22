import os

import pytest
import toml
import torch

from mlkit.nn.confmodels import Conf


@pytest.fixture
def true_conf():
    yield Conf(
        root_dir=os.path.join(os.getcwd(), "tests", "resources"),
        **toml.load(os.path.join("tests", "resources", "test_file.toml")),
    )


@pytest.fixture
def base_conf_txt():
    return """
    [base]
    seed = 0
    experiment_name = "handwritten_digit_classification"

    [model]
    target = "./tests/dummy_module.py::B"
    input_dims = 1
    layers = 4
    dropout = 0.5
    output_dims = 10

    [training]
    epochs = 100
    epoch_schedulers = [
        {target = "torch.optim.lr_scheduler::CosineAnnealingLR", T_max = 100}
    ]

    [training.checkpoint]
    path = "chckpt"
    monitor = {"metric" = "Precision", "stage" = "val"}
    filename = "{epoch}_{val_fbeta_score:.2f}_convlstm"
    mode = "max"

    [training.optimizer]
    target = "torch.optim::Adam"
    lr = 0.0001
    weight_decay = 0.03

    [training.criterion]
    target = "torch.nn::NLLLoss"
    weight = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

    [validation]
    run_every_epoch = 1

    [dataset]
    target = "./tests/dummy_module.py::DummyDatasetModule"

    [dataset.trainval]
    root_dir = "./mnist"

    [dataset.train.loader]
    batch_size = 10
    shuffle = true
    num_workers = 4

    [dataset.validation.loader]
    batch_size = 10
    shuffle = false
    num_workers = 4
    """


@pytest.fixture
def dummy_optimizer():
    yield torch.optim.Adam([torch.nn.Parameter(torch.rand((100,)))], lr=0.1)