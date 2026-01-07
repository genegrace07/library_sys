import pytest
from librarydb import Users,Operate

#Test available with  fixture
@pytest.fixture
def mock_db(mocker):
    mockdb = mocker.patch('librarydb.db')
    mockcursor = mockdb.cursor.return_value
    return mockdb,mockcursor
def test_available(mock_db):
    db,cursor = mock_db
    operate = Operate()
    cursor.fetchall.return_value = [{'title':'naruto','availability':'no'},{'title':'onepiece','availability':'yes'}]
    result = operate.available()

    db.ping.assert_called_once_with(reconnect=True)
    db.cursor.assert_called_once_with(dictionary=True,buffered=True)
    cursor.execute.assert_called_once_with('select * from books where status = "available"')
    # cursor.fetchall.assert_called_once()
    cursor.close.assert_called_once()

    assert result == [{'title':'naruto','availability':'yes'},{'title':'onepiece','availability':'yes'}]






#
# #Test view with parametirized
# @pytest.mark.parametrize('dbresult',[{'title':'the book2','author':'david2'}])
# def test_view(mocker,dbresult):
#   mock_db = mocker.patch('librarydb.db')
#   mock_cursor = mock_db.cursor.return_value
#
#   mock_cursor.fetchall.return_value = {'title':'the book1','author':'david1'}
#   operate = Operate()
#   result = operate.view()
#
#   mock_db.ping.assert_called_once_with(reconnect=True)
#   mock_db.cursor.assert_called_once_with(dictionary=True,buffered=True)
#   mock_cursor.execute.assert_called_once_with('select * from books')
#   mock_cursor.close.assert_called_once()
#
#   assert result == {'title':'the book2','author':'david2'}

# #TEST get_username with parameterized
# @pytest.mark.parametrize('username,expected',[('zoro',{'username':'zoro'})])
# def test_get_username(mocker,username,expected):
#   mock_db = mocker.patch('librarydb.db')
#   mock_cursor = mock_db.cursor.return_value
#
#   user = Users()
#   mock_cursor.fetchone.return_value  = expected
#   result = user.get_username(username)
#
#   mock_db.ping.assert_called_once_with(reconnect=True)
#   mock_db.cursor.assert_called_once_with(dictionary=True,buffered=True)
#   mock_cursor.execute.assert_called_once_with('select * from admins where username = %s',(username,))
#   mock_cursor.close.assert_called_once()
#
#   assert result == expected
#
# #TEST get_username
# def test_get_username(mocker):
#   mock_db = mocker.patch('librarydb.db')
#   mock_cursor = mock_db.cursor.return_value
#
#   user = Users()
#   mock_cursor.fetchone.return_value  = {'username':'luffy'}
#   result = user.get_username('luffy')
#
#   mock_db.ping.assert_called_once_with(reconnect=True)
#   mock_db.cursor.assert_called_once_with(dictionary=True,buffered=True)
#   mock_cursor.execute.assert_called_once_with('select * from admins where username = %s',('luffy',))
#   mock_cursor.close.assert_called_once()
#
#   assert result == {'username':'luffy'}

# #TEST SIGNUP
# def test_sign_up(mocker):
#   mock_db = mocker.patch('librarydb.db')
#   mock_cursor = mock_db.cursor.return_value
#
#   user = Users()
#   user.sign_up('luffy',1234)
#
#   mock_db.ping.assert_called_once_with(reconnect=True)
#   mock_db.cursor.assert_called_once_with(dictionary=True,buffered=True)
#   mock_cursor.execute.assert_called_once_with('insert into admins(username,passwd) values(%s,%s)',('luffy',1234))
#   mock_db.commit.assert_called_once()
#   mock_cursor.close.assert_called_once()
#
#   assert result is None
#

















