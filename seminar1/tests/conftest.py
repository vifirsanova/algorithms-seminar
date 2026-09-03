import pytest


@pytest.fixture
def sample_events():
    """Стандартный набор мероприятий для тестов"""
    return [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]


@pytest.fixture
def sample_items():
    """Стандартный набор предметов для рюкзака"""
    return [(60, 10), (100, 20), (120, 30)]
