from fastapi import FastAPI
import uvicorn
import requests
from bs4 import BeautifulSoup
app = FastAPI()


@app.get("/home")
def hello(name=None):
    if name is not None:
        return f"Hello {name}"
    else:
        return "Hello stranger"

@app.get("/youtube")
def youtube(link=None):
    if link is not None:
        try:
            r = requests.get(link)
            s = BeautifulSoup(r.text, "html.parser")
            title = s.find("title").text.replace("\n", "").replace("- YouTube", "").strip()
            creator = str(s.find("link", itemprop="name"))
            info = {
                "title": title,
                "creator": creator.replace("itemprop=\"name\"/>", "").replace("<link content=", "").replace("\"", "").strip(),

            }
        except Exception as e:
            print(e)
            return "Error finding that video"
        return info
    else:
        return "You didn't provide a link"



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)