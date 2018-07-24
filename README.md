# MongoDB sample


## Setup

```bash
brew install mongodb
```

## MongoDB

Launch MongoDB
```bash
mongod --dbpath data/ --logpath log/mongodb.log --fork
```

Stop MongoDB
```bash
mongo
> use admin
switched to db admin
> db.shutdownServer()
server should be down...
```

## Python client

```bash
virtualenv env
source env/bin/activate
pip install pymongo
python mongodb_sample.py
```
