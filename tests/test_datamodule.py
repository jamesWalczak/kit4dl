from unittest.mock import MagicMock

import pytest

from kit4dl.dataset import Kit4DLAbstractDataModule


class TestDatamodule:
    class TestDataModule(Kit4DLAbstractDataModule):
        pass

    def test_setting_extra_arguments(self):
        conf = MagicMock()
        conf.arguments = {"abc": 1}
        datamodule = TestDatamodule.TestDataModule(conf)
        assert hasattr(datamodule, "abc")
        assert datamodule.abc == 1
