from Job import Job
from bs4 import BeautifulSoup
from requests import get

start_url = "https://www.aravihi.gov.pf/offre-de-emploi/liste-offres.aspx"
job_links = []


def scrap_page(url):
    request = get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    next_page = soup.find("a", id="ctl00_ctl00_corpsRoot_corps_PaginationLower_linkSuivPage")
    if next_page is not None:
        href = next_page.get("href")
        scrap_page(href)
        get_job_url(href)
    else:
        pass


def get_job_url(page):
    request = get(page)
    soup = BeautifulSoup(request.text, "html.parser")
    job_list = soup.find_all("a", class_="ts-offer-card__title-link")
    for job in job_list:
        job_links.append("https://www.aravihi.gov.pf" + job.get("href"))


def set_job(soup):
    description_list = []
    job = Job
    if soup is not None:
        title = soup.find("p", id="fldjobdescription_jobtitle")
        if title is not None:
            title = title.text
            job.title = title
        descriptions = soup.find("p", id="fldoffercustomblock2_longtext2")
        if descriptions is not None:
            descriptions = descriptions.text
            description_list = descriptions.split(';')
        return Job(title, description_list, "", "", "")


def scrap_jobs():
    for job_link in job_links:
        request = get(job_link)
        soup = BeautifulSoup(request.text, "html.parser")
        print(set_job(soup))


def main():
    scrap_page(start_url)
    scrap_jobs()


if __name__ == "__main__":
    main()
