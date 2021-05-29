from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time, re, docx
from parsers.sum_parser import sum_parser

docx_file = docx.Document('C:\\Users\\mesic\\Downloads\\new.docx')

# Main section text
main_section = []

# Full text list
full_text_list = []


### Extract the text in list
def extract_text():
    extracted = []

    for i in docx_file.paragraphs:
        extracted.append(i.text)
    
    return extracted

document_serialized = extract_text()

def get_full_text():
    for para in docx_file.paragraphs:
        current_paragraph = para.text
        full_text_list.append(current_paragraph)
    
    return '\n'.join(full_text_list)

def get_title_text():
    for para in docx_file.paragraphs:
        current_paragraph = para.text
        if 'Die best' in current_paragraph:
            return current_paragraph

def get_all_product_headlines():

    summaries = []
    headlines = []

    for para in docx_file.paragraphs:
        current_paragraph = para.text
        
        if 'Summary' in current_paragraph:
            index = document_serialized.index(current_paragraph)

            ### Search for summary text and headline
            if (document_serialized[index-1]):
                current_summary = document_serialized[index-1]
                summaries.append(current_summary)
                
                if (document_serialized[index-2]):
                    current_headline = document_serialized[index-2]
                    headlines.append(current_headline)
                    
                elif(document_serialized[index-3]):
                    current_headline = document_serialized[index-3]
                    headlines.append(current_headline)
                    
                elif(document_serialized[index-4]):
                    current_headline = document_serialized[index-4]
                    headlines.append(current_headline)
                    
                else:
                    print("\033[1;31;93m Cant find headline... \033[0m")
            elif (document_serialized[index-2]):
                current_summary = document_serialized[index-2]
                summaries.append(current_summary)
                
                if (document_serialized[index-3]):
                    current_headline = document_serialized[index-2]
                    headlines.append(current_headline)
                    
                elif(document_serialized[index-4]):
                    current_headline = document_serialized[index-3]
                    headlines.append(current_headline)
                    
                elif(document_serialized[index-5]):
                    current_headline = document_serialized[index-4]
                    headlines.append(current_headline)
                else:
                    print("\033[1;31;93m Cant find headline... \033[0m")
            else:
                print("\033[1;31;93m Cant find summary... \033[0m")

    return { "summaries": summaries, "headlines": headlines}
            

def get_main_section():
    # Flag to start writing to main section
    main_start_flag = False

    for para in docx_file.paragraphs:
        current_paragraph = para.text
        if current_paragraph == 'Warum Sie uns vertrauen können':
            main_start_flag = True
        
        if main_start_flag == True:
            main_section.append(current_paragraph)
    
    return '\n'.join(main_section)

def get_product_titles(full_text_list):
    product_no = 1
    for para in full_text_list:
        product_title_input_xpath = f'/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[3]/div[1]/div[1]/div/div[9]/div[2]/div/table/tbody/tr[{product_no}]/td[2]/div[1]/div[2]/div/input'
        summary_found = re.search('summary', para, flags=re.IGNORECASE)
        if summary_found:
            product_title_input = webdriver.find_element_by_xpath(product_title_input_xpath)
            print(full_text_list.index(summary_found.group(0)))
            product_title_input.send_keys('test')
            product_no += 1

# options = webdriver.ChromeOptions()
# options.add_argument("user-data-dir=C:\\Users\\mesic\\AppData\\Local\\Google\\Chrome\\User Data")

# webdriver = webdriver.Chrome(executable_path='C:\\Users\\mesic\\OneDrive\\Documents\\chromedriver.exe', chrome_options=options)
# webdriver.get('https://osp.expertentesten.de/wp-admin/post-new.php')

full_text = get_full_text()

title_text = get_title_text()
main_text = get_main_section()

headlines_and_summaries = get_all_product_headlines()

for i in headlines_and_summaries['summaries']:
    a = sum_parser(i)
    print(a)

# Test if all products have summary, pros and cons
summary = re.findall("Summary", full_text, flags=re.IGNORECASE)
pros = re.findall(r'^Vorteile', full_text, flags=re.IGNORECASE)
cons = re.findall(r'^Nachteile', full_text, flags=re.IGNORECASE)

cons_backup = re.findall(r'^Nachteil', full_text, re.MULTILINE | re.IGNORECASE)
pros_backup = re.findall(r'^Vorteil', full_text, re.MULTILINE | re.IGNORECASE)

if len(summary) == 4:
    print("Summary Test -\033[1;32;40m Passed \033[0m")
else:
    print("Summary Test -\033[1;31;93m Failed \033[0m")

if len(pros) == 4:
    print("Pros Test    -\033[1;32;40m Passed \033[0m")
else:
    if len(cons) < 4:
        if len(pros_backup) == 4:
            print("Pros Test    -\033[1;32;40m Passed \033[0m")
        else:
            print("Pros Test    -\033[1;31;93m Failed \033[0m")
    else:
        print("Pros Test    -\033[1;31;93m Failed \033[0m")

if len(cons) == 4:
    print("Cons Test    -\033[1;32;40m Passed \033[0m")
else:
    if len(cons) < 4:
        if len(cons_backup) == 4:
            print("Cons Test    -\033[1;32;40m Passed \033[0m")
        else:
            print("Cons Test    -\033[1;31;93m Failed \033[0m")
    else:
        print("Cons Test    -\033[1;31;93m Failed \033[0m")

time.sleep(1)

# Title input
# title = webdriver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[1]/div[1]/div[1]/input')
# Intro input
# intro = webdriver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[3]/div[1]/div[1]/div/div[3]/div[2]/textarea')
# Main Text Input
# main_text_area = webdriver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[3]/div[1]/div[1]/div/div[5]/div[2]/div/div[2]/textarea')
# Add Product Button
# add_product_button = webdriver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[3]/div[1]/div[1]/div/div[9]/div[2]/div/div/a')
# Add Category Checkbox
# add_category_checkbox = webdriver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[2]/div/div[2]/div/div/div[2]/ul/li[2]/label/input')

# for i in range(3):
    # add_category_checkbox.click()

# add_product_button.click()

# title.send_keys(title_text)
# main_text_area.send_keys(main_text)

time.sleep(2)

# get_product_titles(full_text_list)
