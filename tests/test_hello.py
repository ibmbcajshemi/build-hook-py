def test_hello( client ):
    ret = client.get( '/' )  
    assert ret.status_code == 200
    assert ret.mimetype == 'text/plain'
    assert b'jet' in ret.data
