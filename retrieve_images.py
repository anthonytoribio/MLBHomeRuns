#retrieve_iamges.py
#Creator: Anthony Toribio and Robert Toribio
#Date: 10/30/2021

from apiclient.discovery import build

_API_KEY = "APIKeyHidden"
_CX = "CXHidden"  #search_engine_id
_QUERY = "Justin Turner"

_SERVICE = build("customsearch","v1", developerKey=_API_KEY)


def getImage_url(query:str) -> str:
    res = _SERVICE.cse().list(
        q = query,
        cx = _CX,
        searchType = "image",
        num = 1,
        fileType="jpg",
        safe = "off"
        ).execute()

    return res["items"][0]["link"]
        
def debugger_test():
    res = _SERVICE.cse().list(
        q = _QUERY,
        cx = _CX,
        searchType = "image",
        num = 1,
        fileType="jpg",
        safe = "off"
        ).execute()

    print(res["items"][0]["link"])
    for item in res['items']:
        print("==========================================================")
        print(item["title"])
        print(item["link"])

if __name__=="__main__":
    debugger_test()
