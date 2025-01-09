import requests
import xml.etree.ElementTree as ET
import csv
import argparse

# Fetch data from PubMed
def fetch_pubmed_data(query, max_results=10):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("esearchresult", {}).get("idlist", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching PubMed data: {e}")
        return None

# Fetch paper details using PubMed IDs
def fetch_paper_details(pubmed_ids):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "xml"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching paper details: {e}")
        return None

# Parse XML data to extract paper details
def parse_paper_details(xml_data):
    root = ET.fromstring(xml_data)
    papers = []

    for article in root.findall(".//PubmedArticle"):
        paper = {}
        paper["PubMedID"] = article.findtext(".//PMID")
        paper["Title"] = article.findtext(".//ArticleTitle")
        
        pub_date = article.find(".//PubDate")
        if pub_date is not None:
            year = pub_date.findtext("Year", "")
            month = pub_date.findtext("Month", "")
            day = pub_date.findtext("Day", "")
            paper["Publication Date"] = f"{year}-{month}-{day}" if year else "Unknown"
        else:
            paper["Publication Date"] = "Unknown"
        
        # Extract authors and affiliations
        authors = []
        non_academic_authors = []
        company_affiliations = []
        emails = []

        for author in article.findall(".//Author"):
            lastname = author.findtext("LastName", "")
            firstname = author.findtext("ForeName", "")
            fullname = f"{firstname} {lastname}".strip()
            authors.append(fullname)
            
            affiliation = author.find(".//AffiliationInfo/Affiliation")
            if affiliation is not None:
                affiliation_text = affiliation.text
                if "@" in affiliation_text:
                    emails.append(affiliation_text.split()[-1])  # Extract email
                if any(keyword in affiliation_text.lower() for keyword in ["company", "pharma", "biotech"]):
                    non_academic_authors.append(fullname)
                    company_affiliations.append(affiliation_text)
        
        paper["Authors"] = ", ".join(authors)
        paper["Non-academic Authors"] = ", ".join(non_academic_authors)
        paper["Company Affiliations"] = "; ".join(company_affiliations)
        
        # Only store the main author's email (first author email)
        paper["Email"] = emails[0] if emails else "Not Available"
        
        papers.append(paper)

    return papers



# Save results to a CSV file
def save_to_csv(parsed_data, filename):
    if not parsed_data:
        print("No data to save.")
        return
    
    # Set only the relevant keys for the CSV (Email column)
    keys = ["PubMedID", "Title", "Publication Date", "Authors", "Non-academic Authors", "Company Affiliations", "Email"]
    
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(parsed_data)
    print(f"Data saved to {filename}")


# Main function for command-line interface
def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers based on a query.")
    parser.add_argument("query", type=str, help="Search query for PubMed.")
    parser.add_argument("-f", "--file", type=str, default="results.csv", help="Output CSV filename.")
    parser.add_argument("-n", "--number", type=int, default=10, help="Number of results to fetch.")
    args = parser.parse_args()

    print(f"Fetching papers for query: {args.query}")
    pubmed_ids = fetch_pubmed_data(args.query, max_results=args.number)
    if pubmed_ids:
        print(f"Found {len(pubmed_ids)} papers.")
        xml_data = fetch_paper_details(pubmed_ids)
        if xml_data:
            parsed_data = parse_paper_details(xml_data)
            save_to_csv(parsed_data, args.file)
        else:
            print("Failed to fetch paper details.")
    else:
        print("No papers found for the query.")

if __name__ == "__main__":
    main()
