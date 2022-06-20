#!/usr/bin/env python
# coding: utf-8

# # Creating my own Block Chain 

# In[3]:


import hashlib

# to generate hash value we are using sha256 algorithm which can generate upto 256 bit hashvalue
# SHA-256 is a patented cryptographic hash function that outputs a value that is 256 bits long.

def hash_generator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()

## Block with 3 main parameters 
## 1.Data
## 2.Hash Value of Block
## 3.Hash value of Previous Block

class Block:
    def __init__(self,data,hash,prev_hash):
        self.data = data
        self.hash=hash
        self.prev_hash=prev_hash
        
class Blockchain:
    def __init__(self):
        ## hashLast means hash of Last Block
        hashLast =hash_generator('gen_last')
        ## hast Start means hash of that block
        hashStart = hash_generator('gen_hash')
        
        ## genesis is first block of block chain or we can say base of all block
        genesis=Block('gen_data',hashStart,hashLast)
        self.chain =[genesis]
        
    #method to add new block in BlockChain
    def add_block(self,data):
        prev_hash =self.chain[-1].hash
        hash =hash_generator(data+prev_hash)
        block = Block(data,hash,prev_hash)
        self.chain.append(block)
            


# In[4]:



block_chain = Blockchain()
block_chain.add_block('1')
block_chain.add_block('2')
block_chain.add_block('3')


# In[5]:


for block in block_chain.chain:
    print(block.__dict__)


# In[6]:


bc = Blockchain()
bc.add_block("Saurabh")
bc.add_block("Ankit")
bc.add_block("Raj")
bc.add_block("Aakash")
bc.add_block("Aarush")
bc.add_block("Vansham")
bc.add_block("Abhijeet")


# In[7]:


for block in bc.chain:
    print(block.__dict__)


# In[ ]:




