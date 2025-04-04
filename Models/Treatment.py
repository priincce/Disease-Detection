import re
import requests
import warnings
from bs4 import BeautifulSoup
from googlesearch import search

warnings.filterwarnings("ignore")

def diseaseDetail(term):
    diseases = [term]
    result = term + "\n"

    for dis in diseases:
        query = dis + ' wikipedia'

        for sr in search(query, tld="co.in", num_results=10, pause=0.5):
            if "wikipedia" in sr:
                try:
                    response = requests.get(sr, verify=False)
                    soup = BeautifulSoup(response.content, 'html5lib')

                    info_table = soup.find("table", {"class": "infobox"})
                    if info_table is not None:
                        filled = False
                        for row in info_table.find_all("tr"):
                            data = row.find("th", {"scope": "row"})
                            if data:
                                value = str(row.find("td"))

                                # Clean the HTML content
                                value = value.replace('.', '')
                                value = value.replace(';', ',')
                                value = value.replace('<b>', '<b> \n')
                                value = re.sub(r'<a.*?>', '', value)
                                value = re.sub(r'</a>', '', value)
                                value = re.sub(r'<[^<]+?>', ' ', value)
                                value = re.sub(r'\[.*?\]', '', value)
                                value = value.replace("&gt", ">")

                                # Append to result
                                result += data.get_text().strip() + " - " + value.strip() + "\n"
                                filled = True

                        if filled:
                            break
                except Exception as e:
                    result += f"Error fetching data from {sr}: {e}\n"
                    continue

    return result
