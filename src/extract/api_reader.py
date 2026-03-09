import pandas as pd
import requests as req

def read():
    url = "https://jsonplaceholder.typicode.com/posts"

    r = req.get(url)
    data =  r.json()
    df = pd.DataFrame(data)
    return (df)

