#!/usr/bin/env python3
from hashcash import *
from hashlib import sha1 as sha


'''1. Set challenge and difficulty params'''
challenge = b'Denmark'
difficulty = 23

'''2. Mint'''
token = make_token(challenge, difficulty)

'''3. Verify '''
verify_token(challenge, token)
