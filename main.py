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
        set_job(get_job_url(href))
        scrap_page(href)
    else:
        pass


def get_job_url(page):
    request = get(page)
    soup = BeautifulSoup(request.text, "html.parser")
    job_list = soup.find_all("a", class_="ts-offer-card__title-link")
    for job in job_list:
        return "https://www.aravihi.gov.pf" + job.get("href")


def set_job(url):
    request = get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    if soup is not None:
        title = is_valid(soup.find("p", id="fldjobdescription_jobtitle"))
        description = is_valid(soup.find("p", id="fldjobdescription_description1"))
        definitions = is_valid(soup.find("p", id="fldoffercustomblock2_longtext2")).split(";")
        #definition_list = definitions.split(';')
        education = is_valid(soup.find("p", id="fldapplicantcriteria_educationlevel"))
        specialisation = is_valid(soup.find("p", id="fldapplicantcriteria_freecriteria1"))
        skills = is_valid(soup.find("p", id="fldapplicantcriteria_longtext2")).split(";")
        experience = is_valid(soup.find("p", id="fldapplicantcriteria_freecriteria2"))
        end_date = is_valid(soup.find("p", id="fldoffercustomblock1_date1"))
        print(Job(title, description, definitions, education, specialisation, skills, experience, "", end_date))


def is_valid(el):
    if el is not None:
        return el.text


def scrap_jobs():
    for job_link in job_links:
        request = get(job_link)
        soup = BeautifulSoup(request.text, "html.parser")
        print(set_job(soup))


def main():
    scrap_page(start_url)
    #scrap_jobs()


if __name__ == "__main__":
    main()
