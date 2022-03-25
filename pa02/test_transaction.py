'''
test_transaction runs unit and integration tests on the transaction module
'''
from cgitb import small
import pytest
from transaction import Transaction, to_transaction_dict

@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')

@pytest.fixture
def empty_db(dbfile):
    ''' create an empty database '''
    db = Transaction(dbfile)
    yield db

@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    cat0 = {'item #':'1','amount':'400','category':'loan','date':'2022-01-10','description':'loan for car'}
    cat1 = {'item #':'2','amount':'500','category':'bank','date':'2023-02-20','description':'loan for bank'}
    cat2 = {'item #':'3','amount':'600','category':'money','date':'2024-03-30','description':'loan for money'}
    id1=empty_db.add_transaction(cat0)
    id2=empty_db.add_transaction(cat1)
    id3=empty_db.add_transaction(cat2)
    yield empty_db
    empty_db.delete_transaction(id3)
    empty_db.delete_transaction(id2)
    empty_db.delete_transaction(id1)

@pytest.fixture
def med_db(small_db):
    ''' create a database with 10 more elements than small_db'''
    rowids=[]
    # add 10 categories
    for i in range(10):
        s = str(i)
        cat ={'name':'name'+s,
               'desc':'description '+s,
                }
        rowid = small_db.add_transaction(cat)
        rowids.append(rowid)

    yield small_db

    # remove those 10 categories
    for j in range(10):
        small_db.delete_transaction(rowids[j])



@pytest.mark.delete
def jimkellys_tests(med_db):
    ''' add a category to db, delete it, and see that the size changes'''
    # first we get the initial table
    cats0 = med_db.select_all()

    # then we add this category to the table and get the new list of rows
    cat0 = {'item #':'1',
            'amount':'400',
            'category':'loan',
            'date':'2022-01-30',
            'description':'loan for car'     
            }
    rowid = med_db.add_transaction(cat0)
    cats1 = med_db.select_all()

    # now we delete the category and again get the new list of rows
    med_db.delete_transaction(rowid)
    cats2 = med_db.select_all()

    assert len(cats0)==len(cats2)
    assert len(cats2) == len(cats1)-1
    


@pytest.mark.nazari
def nazaris_tests():
    
    return

@pytest.mark.gabby
def gabbys_tests():
    return

@pytest.mark.tiffany
def tiffanys_tests():
    return