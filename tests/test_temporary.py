import nsecpy


def test_has_regions():
    assert isinstance(nsecpy.regions, dict) and len(nsecpy.regions)
