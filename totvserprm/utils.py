import time
import random
import string

def number_doc():
    num_doc = str(time.time()).replace('.','')[-7:]
    num_doc = num_doc[4:] + random.choice(string.letters) + num_doc[:4]
    num_doc = random.choice(string.letters) + num_doc
    num_doc = num_doc + random.choice(string.letters)
    return num_doc
