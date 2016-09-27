import couchdb
couch = couchdb.Server()
db = couch.create('test')
couch.delete('test')