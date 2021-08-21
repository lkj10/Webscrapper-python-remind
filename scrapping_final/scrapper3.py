import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def extract_jobs(url):
    jobs = []
    print("Scrapping remoteok...")
    request = requests.get(url, headers=headers)
    soup = BeautifulSoup(request.text, "html.parser")
    results = soup.find_all("td", {"class" : "company position company_and_position"})
    for result in results:
      try :
          job_id = result.find("a")["href"]
          title = result.find("h2", {"itemprop" : "title"}).text
          company = result.find("h3", {"itemprop" : "name"}).text
          jobs.append({
              'title' : title,
              'company' : company,
              'location' : "remote",
              'apply_link' : f"https://remoteok.io/{job_id}"
          })
      except:
        pass
    return jobs


def get_jobs_ro(word):
    url = f"https://remoteok.io/remote-{word}-jobs"
    jobs = extract_jobs(url)
    return jobs

