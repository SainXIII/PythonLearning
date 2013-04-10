#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect("/tmp/example")

c = conn.cursor()

c.execute('''create table stocks
            (data text, trans text, symbol text,
             qty real, price real)''')

c.execute('''insert into stocks
             values ("2006-10-05", "BUY", "RHAT", 100, 35.14)''')

conn.commit()

c.close()
