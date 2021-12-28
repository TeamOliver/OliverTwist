from pymongo import MongoClient
from TeamOliver import MONGODB_URL
    
client = MongoClient(MONGODB_URL)
db = client['CHATS']

user_col = db['USERS']
chat_col = db['CHATS']
b_users = db['BANNED_USERS']
b_chats = db['BANNED_CHATS']

def in_users(id):
    data = {'_id': id}
    return user_col.find(data)
          
def add_user(id, name):
    data = {'_id': id, 'name': name}
    return user_col.insert_one(data)
        
def del_user(id):
    data = {'_id': id}
    return user_col.delete_one(data)

def ban_user(id, name, reason):
    user_col.delete_one({'_id': id})
    data = {'_id': id, 'name': name, 'reason': reason}
    return b_users.insert_one(data)

def unban_user(id, name):
    user_col.insert_one({'_id': id, 'name': name}) 
    data = {'_id': id}                             
    return b_users.delete_one(data)                

def get_users():
    count = user_col.count_documents({})
    list = user_col.find()
    return count, list
#----------------------------------------------------------------------------------
def in_chats(id):
    data = {'_id': id}
    return chat_col.find(data)
          
def add_chats(id, title):
    data = {'_id': id, 'title': title}
    return chat_col.insert_one(data)
        
def del_chats(id):
    data = {'_id': id}
    return chat_col.delete_one(data)

def ban_chats(id, reason):
    chat_col.delete_one({'_id': id})
    data = {'_id': id, 'reason': reason}
    return b_users.insert_one(data)

def unban_chats(id):
    data = {'_id': id}
    return b_users.delete_one(data)

def get_chats():
    count = chat_col.count_documents({})
    list = chat_col.find()
    return count, list
