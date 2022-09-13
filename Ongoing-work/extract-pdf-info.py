# Script to automatically extract information from proceeding pdfs.
# It tries to extract the following information
# 1. Paper titles
# 2. All links per paper
# 3. Keywords per paper


from PyPDF2 import PdfReader
import os


# Extracts links from a PDF page by looking for "http" in sentences
def extract_links_from_pdf_page(page):
  links = []
  text = page.extract_text()
  lines = text.split("\n")
  for line in lines:
    if "http" in line:
      links.append(line)
      #TODO: Link may be split over multiple lines, make sure to include the complete link not just the sentence where it started
  return links

# Extracts keywords from a PDF page by looking for a sentence starting with "Keywords:" (as used in the TACAS template)
def extract_keywords_from_tacas_page(page):
  keywords = []
  text = page.extract_text()
  if "Keywords:" in text:
    text_after_keywords = text.split("Keywords:")[1]
    words = text_after_keywords.split("1")[0].split("·") # Take all text until section 1 starts then split on the separator
    keywords.extend(words)
    keywords = [w.strip() for w in keywords]
  return keywords

# Extracts keywords and links from a TACAS paper
def extract_from_tacas_paper(pages):
  keywords = []
  links = []
  keywords = extract_keywords_from_tacas_page(pages[0])
  for page in pages:
    links += extract_links_from_pdf_page(page)
  return keywords, links


# Detects boundaries (i.e. first and last page) of all papers in a proceedings pdf
# Beginnings are detected by looking for "Abstract" and part of the copyright statement
# Endings are detected by looking for the "Open Access" statement which is placed at the end of each paper
# Returns 
def detect_paper_boundaries(reader, paper_titles):
  beginnings = []
  ends = []
  for i in range(0, len(reader.pages)):
    text = reader.pages[i].extract_text()
    # seems to work fine without 2022 except that it identifies a few more "beginnings" because of long lists of references
    if "Abstract" in text and ("The Author(s) 2022" in text or "not under copyright protection" in text): # Take this as beginning of paper, "1 Introduction" is not reliable because it misses a lot of the SV-COMP papers + 4 others
      beginnings.append(i)
    if "Open Access" in text: # Identify end of papers
      ends.append(i)
  # Disregard first element in ends, which refers to the "Open Access" statement in the beginning of the proceedings that is not associated with any specific paper
  return zip(beginnings, ends[1:])
  


for doc in os.listdir("Proceedings/"):
  reader = PdfReader("Proceedings/"+doc)
  # Identifies paper titles in outline of a PDF document
  # Note: this works for TACAS papers, did not try with other papers yet
  paper_titles = []
  for dest in reader.outline:
    for key in dest:
      if not isinstance(key, list):
        paper_titles.append(key['/Title'])
  
  paper_pages = detect_paper_boundaries(reader, paper_titles)
  
  for begin,end in paper_pages:
    keywords, links = extract_from_tacas_paper(reader.pages[begin:end+1])
    print(keywords)
    print(links)
    print("\n")