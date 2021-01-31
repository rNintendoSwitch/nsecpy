import nsecpy


def test_has_regions():
    assert isinstance(nsecpy.regions, list) and len(nsecpy.regions)
