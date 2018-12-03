import pickle

def store_data():
    # Initilizing data to be stored in Database
    abul = {'key': 'abul', 'name': 'abul mama', 'age': 21, 'pay': 4000000}
    habul = {'key': 'habul', 'name': 'habul mama', 'age': 25, 'pay': 4000}
    tabul = {'key': 'tabul', 'name': 'tabul mama', 'age': 28, 'pay': 48900000}

    # Database
    db = {}
    db['abuldb'] = abul
    db['habuldb'] = habul
    db['tabuldb'] = tabul

    # It is important to append in binary mode

    dbfile = open('final.csv', 'ab')

    pickle.dump(db, dbfile)
    dbfile.close()

def load_data():
    dbfile = open('final.csv', 'rb')
    db = pickle.load(dbfile)
    for keys in db:
        print(keys, '=>', db[keys])
    dbfile.close()

if __name__ == '__main__':
    store_data()
    load_data()
