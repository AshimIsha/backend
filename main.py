# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:19:32 2024

@author: M
"""
import json
from collections.abc import Awaitable,  Callable
from typing import Any
from urllib.parse import parse_qs
from utils import error, factorial_count, fibonaci_count, mean_count, answer

async def application(
    scope: dict[str, Any],
    recieve: Callable,
    send: Callable) -> None: 
    protocol = scope['type']
    method = scope['method']
    path = scope['path']
    
    if protocol == 'http':
        if method == 'GET':
            if path == '/factorial':
                
                await factorial(scope, send)
                
            if scope['path'].split('/')[1] == 'fibonacci':
                
                await fibonaci(scope, send)
                
            if path == '/mean':
                
                await mean(recieve, send)
    
    await error(404, "Not Found", send)
                
async def get_body(recieve) -> bytes:
    body = await recieve()
    return body.get('body')
                
async def factorial(
    scope: dict[str, Any],
    send: Callable) -> None:  
    
    try:
        num = int(parse_qs(scope['query_string'].decode())['n'][0])
    except Exception:
        await error(422, "Unprocessable Entity", send)
    
    if num < 0:
        await error(400, "Bad Request", send)
   
    result = factorial_count(num)

    res_body = {"result":result}
    await answer(res_body, send)
    
async def fibonaci(
    scope: dict[str, Any],
    send: Callable) -> None:  
    
    try:
        num = int(scope['path'].split('/')[2])
    except Exception:
        await error(422, "Unprocessable Entity", send)
    
    if num < 0:
        await error(400, "Bad Request", send)
   
    result = fibonaci_count(num)

    res_body = {"result":result}
    await answer(res_body, send) 
    
    
async def mean(
    recieve: Callable,
    send: Callable) -> None:  
    try:
        bytes_msg = await get_body(recieve)
        body = json.loads(bytes_msg)
        
        if not isinstance(body, list) or not body:
            return await error(400, "Bad Request", send)
        
        mean_answer = mean_count(body)
        
    except (IndexError, ValueError):
        await error(422, "Unprocessable Entity", send)
    

    res_body = {"result":mean_answer}
    await answer(res_body, send)   