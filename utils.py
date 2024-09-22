# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 16:12:18 2024

@author: M
"""

import json
import math

async def error(status, error, send):
    await send(
            {
                "type": 'http.response.start',
                "status": status,
                "headers": [
                        [b"content-type", b"text/plain"]                  
                ]
            }
        )
    await send(
            {
                "type": 'http.response.body',
                "body": json.dumps({"error": error}).encode('utf-8')
            }
        )
    
async def answer(res, send):
    await send(
            {
                "type": 'http.response.start',
                "status": 200,
                "headers": [
                        [b"content-type", b"text/plain"]                  
                ]
            }
        )
    await send(
            {
                "type": 'http.response.body',
                "body": json.dumps(res).encode('utf-8')
            }
        )
    
def factorial_count(n):
    return math.factorial(n)

def fibonaci_count(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y

    return x
    
def mean_count(n):
    a = 0
    for i in n:
        a += i
    
    return a / len(n)
    