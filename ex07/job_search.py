import sys
import requests
from bs4 import BeautifulSoup
import argparse

'''
this works purely through command line. calling ex07/job_search.py without any further filters will print the first 7 available job
however if you use --location Cluj-Napoca, --techlist React,MSExcel --company Bosch or any combination of said 3, you will get up to 7 available jobs, if available

--location, --techlist, --company are all optional

example
py ./job_search.py --location Cluj-Napoca --techlist JS,React 



'''

def scrape_data():
    is_scraping = True
    current_page = 1
    scraped_data = []

    while is_scraping:
        initial_len = len(scraped_data)
        response = requests.get(f"https://www.juniors.ro/jobs?page={current_page}")

        if(response.status_code != 200):
            print("error code")


        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("li", class_="job")

        for job in jobs:
            tech_list = [a.get_text(strip=True) for a in job.select("ul.job_tags > li > a")]
            header_text = job.find("div", class_="job_header_title").find("strong").text
            parts = [part.strip() for part in header_text.split("|")]

        
            if len(parts) >= 3 and parts[0].lower() == "remote":
                location = parts[1]
                post_date = parts[2]
            elif len(parts) == 2:
                location = parts[0]
                post_date = parts[1]
            else:
                location = parts[0] if parts else "N/A"
                post_date = parts[-1] if len(parts) > 1 else "N/A"

            details = {
                "Job title": job.find("div", class_="job_header_title").find("h3").text.strip(),
                "Company name": job.find("ul", class_="job_requirements").find("li").text.split(":")[1].strip(),
                "Location": location,
                "List of tech": tech_list,
                "Post date": post_date,
            }
            scraped_data.append(details)
            
        len_after = len(scraped_data)
        if initial_len == len_after:
            is_scraping = False

        current_page += 1
    return scraped_data

#filtering functions


def filter_location(location, jobs):
    return [job for job in jobs if job["Location"] == location]

def filter_company_name(company_name, jobs):
    return [job for job in jobs if job["Company name"] == company_name]

def filter_list_of_tech(list_of_tech, jobs):
    return [job for job in jobs if set(job["List of tech"]) & set(list_of_tech)]



if __name__ == "__main__":

    scraped_data = scrape_data()

    if len(sys.argv) == 1:
        for index, job in enumerate(scraped_data):
            print(job, "\n")
            if index == 6:
                print("These are the first 7 jobs!")
                quit()
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument("--location", type=str, required=False)
        parser.add_argument("--company", type=str, required=False)
        parser.add_argument("--techlist", type=str, required=False)

        args = parser.parse_args()

        final_list = scraped_data

        if args.location:
            final_list = filter_location(args.location, final_list)
        if args.company:
            final_list = filter_company_name(args.company, final_list)
        if args.techlist:
            tech_list = [tech.strip() for tech in args.techlist.split(',')]
            print(tech_list)
            final_list = filter_list_of_tech(tech_list, final_list)
        
        if final_list:
            for index, job in enumerate(final_list):
                print(job, "\n")
                if index == 6:
                    print(f"These are the first {index + 1} available jobs!")
                    break
        else:
            print("No jobs found matching the specified criteria.")
    