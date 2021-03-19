from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
app = FastAPI()

class Cookie(BaseModel):
    title: str
    price: float
    mass: float
    death_date: str

@app.get("/")
async def root():
    return {"message": "Hello Worlsdfsddfsd fszaf sadf szdf sdf f sd sd"}

@app.get("/cookie/{cookie_id}")
async def find_cookie(cookie_id):
    con = sqlite3.connect('example.sqlite')
    cur = con.cursor()
    cur.execute('SELECT * FROM cookie WHERE id = ?', (cookie_id,))
    cookie = cur.fetchone()
    con.commit()
    con.close()
    return {"title": cookie[0], "price": cookie[1], "mass": cookie[2], "death_date": cookie[3]}

@app.post("/cookie/")
async def create_item(item: Cookie):
    con = sqlite3.connect('example.sqlite')
    cur = con.cursor()
    cur.execute('INSERT INTO cookie (price, mass, title, death_date) VALUES (?,?,?,?)', (item.price, item.mass, item.title, item.death_date))
    con.commit()
    con.close()
    return item