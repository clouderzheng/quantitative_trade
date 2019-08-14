import requests
from bs4 import BeautifulSoup
import traceback
def get_comment():
    try:
        tonghua_info_url = "http://stockpage.10jqka.com.cn/600887/"
        session = requests.Session()
        data = session.get(tonghua_info_url)

        doc = BeautifulSoup(data.text, 'html.parser')
        analyzes = doc.select(".analyze-txt-cont")

        result = {}
        for analyze in analyzes:
            time = analyze.select(".txt-aside")[0].text
            describe = analyze.select(".txt-main")[0].text
            result[time] = describe
        return result
    except Exception as e:
        traceback.print_exc()
        return "error"

result = get_comment()

print(result)


