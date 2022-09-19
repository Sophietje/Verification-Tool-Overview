# Script to automatically extract information from proceeding pdfs.
# It tries to extract the following information
# 1. Paper titles
# 2. All links per paper
# 3. Keywords per paper


from PyPDF2 import PdfReader
import os
import re
md_template = """
#### Name:


#### Application domain/field:


#### Type of tool (e.g. model checker, test generator):


#### Expected input thing:


#### Expected input format:


#### Expected output:


#### Internals (tools used, frameworks, techniques, paradigms, ...):


#### Comments:


#### URIs (github, websites, etc.):


#### Last commit date:


#### Last publication date:


#### List of related papers:
{}

#### Related tools (tools mentioned or compared to in the paper):


#### Meta
{}
"""

#TODO: recognize artifact badges

# Generate a markdown file for all papers found with corresponding titles, keywords and links
def dump_to_markdown(paper_title, doi, conf, year, keywords):
  name = ''.join(e for e in paper_title if e.isalnum())
  filename = "generated/"+name+".md"
  with open(filename, 'w', encoding='utf-8') as file:
    paper_link = doi + " (" + conf + " "+ year + ")"
    keywords = "".join([":: "+k.replace("-\n", "")+"\n" for k in keywords])
    p = md_template.format(paper_link, keywords)
    file.write(p)



# Extracts links from a PDF page by looking for "http" in sentences
def extract_links_from_pdf(pages):
  links = []
  doi = ""
  artifact = []
  for page in pages:
    text = page.extract_text()
    lines = text.split("\n")
    for line in lines:
      # Add line if it contains a link, but not if it is a link in the copyright statement (that refers to the paper itself)
      if "http" in line:
        # If it's a copyright statement then extract the DOI
        if "artifact" in line.lower() or "code" in line.lower() or "supplement" in line.lower():
          artifact.append(line)
        elif "The Author(s) 2022" in line or "not under copyright protection" in line:
          if doi == "":
            doi = "http" + "".join(line.split("http")[1:])
        # If we didn't find a copyright statement, assume first link is the paper DOI
        elif doi == "" and "doi" in line:
            line = line.replace(" ", "")
            m = re.search("http.*\_[0-9][0-9]", line)
            doi = m.group() if m else line
        # Otherwise add the link the list of links (unless it's a useless CC link)
        elif not "creativecommons.org" in line:
          links.append(line)
        #TODO: Link may be split over multiple lines, make sure to include the complete link not just the sentence where it started
  return doi, artifact, links

# Extracts keywords from a PDF page by looking for a sentence starting with "Keywords:" (as used in the TACAS template)
def extract_keywords_from_pdf(page):
  keywords = []
  text = page.extract_text()
  if "Keywords:" in text:
    text_after_keywords = text.split("Keywords:")[1]
    words = text_after_keywords.split("1")[0].split("·") # Take all text until section 1 starts, then split on the separator
    keywords.extend(words)
    keywords = [w.strip() for w in keywords]
  return keywords

# Extracts keywords and links from a paper (PDF format)
def extract_keywords_and_links_from_pdf(pages):
  keywords = []
  links = []
  keywords = extract_keywords_from_pdf(pages[0])
  doi, artifact, links = extract_links_from_pdf(pages)
  return keywords, doi, artifact, links


# Detects boundaries (i.e. first and last page) of all papers in a proceedings pdf
# Beginnings are detected by looking for "Abstract" and part of the copyright statement
# Endings are detected by looking for the "Open Access" statement which is placed at the end of each paper
# Returns 
def detect_paper_boundaries(reader, paper_titles):
  beginnings, bibs, ends = [], [], []
  for i in range(0, len(reader.pages)):
    text = reader.pages[i].extract_text()
    # seems to work fine without 2022 except that it identifies a few more "beginnings" because of long lists of references
    if "Abstract" in text and ("The Author(s) 2022" in text or "not under copyright protection" in text): # Take this as beginning of paper, "1 Introduction" is not reliable because it misses a lot of the SV-COMP papers + 4 others
      beginnings.append(i)
    if "Open Access" in text: # Identify end of papers
      ends.append(i)
    if "References\n" in text: # Identify beginning of bibliography
      bibs.append(i)
  # Disregard first element in ends, which refers to the "Open Access" statement in the beginning of the proceedings that is not associated with any specific paper
  return list(zip(beginnings, bibs, ends[1:]))
  


for doc in os.listdir("Proceedings/"):
  reader = PdfReader("Proceedings/"+doc)
  # Identifies paper titles in outline of a PDF document
  paper_titles = []
  for dest in reader.outline:
    if "TACAS" in doc:
      for key in dest:
        if not isinstance(key, list):
          paper_titles.append(key['/Title'])
    elif "CAV" in doc:
      if not isinstance(dest, list) and dest['/Count'] != 0:
        paper_titles.append(dest['/Title'])
  # Detect boundaries (first and last page) of papers, used for grouping other metadata
  paper_pages = detect_paper_boundaries(reader, paper_titles)
  i = 0
  while (i < len(paper_titles)):
    begin, bib, end = paper_pages[i]
    keywords, doi, artifact, links = extract_keywords_and_links_from_pdf(reader.pages[begin:end+1])
    conf = "TACAS" if "TACAS" in doc else "CAV"
    dump_to_markdown(paper_titles[i], doi, conf, "2022", keywords)
    i += 1