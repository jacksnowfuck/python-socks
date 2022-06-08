#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import pproxy
import configparser
import win32timezone

loop = asyncio.get_event_loop()

file = 'config.ini'
con = configparser.ConfigParser()
con.read(file, encoding='utf-8')
local_listen = con.get('local','local_listen')
remote_conn = con.get('remote','remote_conn')

async def ssh_handle():
    server = pproxy.Server(local_listen)
    remote = pproxy.Connection(remote_conn)
    args = dict(rserver=[remote],
                verbose=print)

    await server.start_server(args)
    print("server started in socks5://127.0.0.1:8081")
    await asyncio.sleep(1)
    return "done"

try:
    loop.run_until_complete(ssh_handle())
    loop.run_forever()
except Exception as e:
    print(e)