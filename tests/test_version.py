import investopedia as iv


def test_investopedia_version():
    """Test that the version exists"""
    assert '__version__' in dir(iv)
