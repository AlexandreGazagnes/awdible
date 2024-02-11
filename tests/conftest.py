import numpy as np
import pandas as pd
import pytest

from sktransf.utils import get_titanic


@pytest.fixture
def X_y() -> tuple:
    """Load the data"""

    return get_titanic()


@pytest.fixture
def X() -> pd.DataFrame:
    """Load the data"""

    X, _ = X_y = get_titanic()

    return X


@pytest.fixture
def X_bool() -> pd.DataFrame:
    """Load the data"""

    X, _ = X_y = get_titanic()

    X["bool_col"] = np.random.choice(["a", "b"], size=X.shape[0])

    return X


@pytest.fixture
def X_unique() -> pd.DataFrame:
    """Load the data"""

    X, _ = X_y = get_titanic()

    X["unique_col"] = "hello"

    return X
