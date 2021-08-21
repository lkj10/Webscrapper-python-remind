import requests
from bs4 import BeautifulSoup


def extract_jobs(url):
    jobs = []
    print("Scrapping weworkremotely...")
    result = requests.get(f"{url}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("section", {"class" : "jobs"})
    for result in results:
      job =result.find("ul")
      features = job.find_all("li")
      for i in range(len(features)-1):
        job_id = features[i].find("a")["href"]
        title = features[i].find("span", {"class" : "title"}).text
        company = features[i].find("span", {"class" : "company"}).text
        location = features[i].find("span", {"class" : "region company"}).text
        jobs.append({
          'title' : title,
          'company' : company,
          'location' : location,
          'apply_link' : f"https://weworkremotely.com/{job_id}"
      })
    return jobs


def get_jobs_wwr(word):
    url = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={word}"
    jobs = extract_jobs(url)
    return jobs