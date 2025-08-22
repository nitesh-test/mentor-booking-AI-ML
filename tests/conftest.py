import pytest
from mentor_booking_ai_ml.datasets import generate_dataset


@pytest.fixture(scope="session")
def dataset_dir(tmp_path_factory):
    data_dir = tmp_path_factory.mktemp("data")
    generate_dataset(data_dir)
    return data_dir
