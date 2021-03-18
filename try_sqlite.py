import sqlite3
con = sqlite3.connect('example.sqlite')

cur = con.cursor()

symbol = input()
cur.execute(f"SELECT * FROM stocks WHERE symbol = ?", (symbol,))
print(cur.fetchall())



# Do this instead
# t = ('RHAT',)
# cur.execute('SELECT * FROM stocks WHERE symbol=?', t)
# print(cur.fetchone())

# Larger example that inserts many records at a time
purchases = [
             ('2006-03-28', 'BUY', 'RHAT\' OR 1 --', 1000, 45.00)
            ]
cur.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()