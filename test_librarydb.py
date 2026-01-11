import pytest
from librarydb import Users,Operate,Actions

#test update to available
@pytest.fixture
def mockdb(mocker):
    mock_db = mocker.patch('librarydb.db')
    mock_cursor = mock_db.cursor.return_value
    return mock_db, mock_cursor
def test_update_to_available(mockdb):
    db,cursor = mockdb
    actions = Actions()
    actions.update_to_available(20)

    db.ping.assert_called_once_with(reconnect=True)
    db.cursor.assert_called_once_with(dictionary=True,buffered=True)
    cursor.execute.assert_called_once_with('update books set status = "available" where book_id = %s',(20,))
    db.commit.assert_called_once()
    cursor.close.assert_called_once()
    db.close.assert_called_once()

# def update_to_available(self, book_id):
#     db.ping(reconnect=True)
#     cursor = db.cursor(dictionary=True, buffered=True)
#     querry = 'update books set status = "available" where book_id = %s'
#     result = cursor.execute(querry, (book_id,))
#     db.commit()
#     cursor.close()
#     db.close()
#     return result

# #test delete function
# @pytest.fixture
# def mockdb(mocker):
#     mock_db = mocker.patch('librarydb.db')
#     mock_cursor = mock_db.cursor.return_value
#     return mock_db, mock_cursor
# def test_delete(mockdb):
#     db, cursor = mockdb
#     actions = Actions()
#
#     result = actions.delete(10)
#
#     db.ping.assert_called_once_with(reconnect=True)
#     db.cursor.assert_called_once_with(dictionary=True,buffered=True)
#     cursor.execute.assert_called_once_with('delete from books where book_id = %s',(10,))
#     db.commit.assert_called_once()
#     cursor.close.assert_called_once()
#     db.close.assert_called_once()

# # test add books function
# @pytest.fixture
# def dbmock(mocker):
#     mock_db = mocker.patch('librarydb.db')
#     mock_cursor = mock_db.cursor.return_value
#     return mock_db,mock_cursor
# @pytest.mark.parametrize('title,author',[('onepiece','luffy'),
#                                          ('naruto','saske'),
#                                          ('dragonball','goku')])
#
# def test_add_books(dbmock,title,author):
#     db, cursor = dbmock
#     operate = Operate()
#     result = operate.add_books(title, author)
#
#     db.ping.assert_called_once_with(reconnect=True)
#     db.cursor.assert_called_once_with(dictionary=True,buffered=True)
#     cursor.execute.assert_called_once_with('insert into books (title,author) values (%s,%s)',(title,author,))
#     db.commit.assert_called_once()
#     cursor.close.assert_called_once()
#
#     assert result

# #test borrow function
# @pytest.fixture
# def dbmock(mocker):
#     mock_db = mocker.patch('librarydb.db')
#     mock_cursor = mock_db.cursor.return_value
#     return mock_db,mock_cursor
# def test_borrowed(dbmock):
#     db,cursor = dbmock
#     cursor.fetchall.return_value = [{'title':'onepiece','author':'luffy','status':'borrowed'},
#                                     {'title':'naruto','author':'saske','status':'borrowed'},
#                                     {'title':'dragonball','author':'goku','status':'borrowed'}]
#     operate = Operate()
#     result = operate.borrowed()
#
#     db.ping.assert_called_once_with(reconnect=True)
#     db.cursor.assert_called_once_with(dictionary=True,buffered=True)
#     cursor.execute.assert_called_once_with('select * from books where status = "borrowed"')
#     cursor.close()
#
#     assert result == [{'title':'onepiece','author':'luffy','status':'borrowed'},
#                       {'title':'naruto','author':'saske','status':'borrowed'},
#                       {'title':'dragonball','author':'goku','status':'borrowed'}]

# #Test available with  fixture
# @pytest.fixture
# def mock_db(mocker):
#     mockdb = mocker.patch('librarydb.db')
#     mockcursor = mockdb.cursor.return_value
#     return mockdb,mockcursor
# def test_available(mock_db):
#     db,cursor = mock_db
#     operate = Operate()
#     cursor.fetchall.return_value = [{'title':'naruto','availability':'no'},{'title':'onepiece','availability':'yes'}]
#     result = operate.available()
#
#     db.ping.assert_called_once_with(reconnect=True)
#     db.cursor.assert_called_once_with(dictionary=True,buffered=True)
#     cursor.execute.assert_called_once_with('select * from books where status = "available"')
#     # cursor.fetchall.assert_called_once()
#     cursor.close.assert_called_once()
#
#     assert result == [{'title':'naruto','availability':'no'},{'title':'onepiece','availability':'yes'}]
# #
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

















