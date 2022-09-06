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
  lines = text.split("\n")
  for line in lines:
    if line.startswith("Keywords:"):
      keywords.append(line)
      #TODO: Keywords may be split over multiple lines, make sure to include all keywords not just the sentence where it started
  return keywords

# Extracts keywords and links from a TACAS paper
def extract_from_tacas_paper(pages):
  keywords = []
  links = []
  keywords = extract_keywords_from_tacas_page(pages[0])
  for page in pages:
    links += extract_links_from_pdf_page(page)
  return keywords, links


for doc in os.listdir("Proceedings/"):
  if "TACAS" in doc:
    reader = PdfReader("Proceedings/"+doc)
    
    # Identifies paper titles in outline of a PDF document
    # Note: this works for TACAS papers, did not try with other papers yet
    paper_titles = []
    for dest in reader.outline:
      for key in dest:
        if not isinstance(key, list):
          paper_titles.append(key['/Title'])
    
    
    #TODO: Automatically extract paper 'boundaries'
    paper_pages = [[23,44], [45, 65], [66,83], [84, 103], [105, 124]]
    
    for i in range(len(paper_pages)):
      print(paper_titles[i])
      keywords, links = extract_from_tacas_paper(reader.pages[paper_pages[i][0]:paper_pages[i][1]])
      print(keywords)
      print(links)
      print("\n")
