import investopedia


def test_download_pages():
    """Test download_pages"""
    result = investopedia.download_pages('https://www.investopedia.com/terms/i/irr.asp')
    target = 'Internal Rate of Return'
    assert target in result[0].find('h1').text
