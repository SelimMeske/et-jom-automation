from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time, re, docx
from parsers.sum_parser import sum_parser
from parsers.pros_cons_parser import pros_cons_parser
from tests.tests import tests
from selenium.webdriver.common.action_chains import ActionChains

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

### Extracted text in list
document_serialized = extract_text()

### Full text in one string
def get_full_text():
    for para in docx_file.paragraphs:
        current_paragraph = para.text
        full_text_list.append(current_paragraph)
    
    return '\n'.join(full_text_list)

### Get the main title text. Die besten xy - Unser Vergleich
def get_title_text():
    for para in docx_file.paragraphs:
        current_paragraph = para.text
        if 'Die best' in current_paragraph:
            return current_paragraph

### Get intro text
def get_intro_text():
    if (document_serialized[2] and len(document_serialized[1]) > 150):
        intro_text = document_serialized[1]
        return intro_text
    elif (document_serialized[3] and len(document_serialized[2]) > 150):
        intro_text = document_serialized[2]
        return intro_text

### Get the title and summaries for all 4 products
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
                    current_headline = document_serialized[index-3]
                    headlines.append(current_headline)
                    
                elif(document_serialized[index-4]):
                    current_headline = document_serialized[index-4]
                    headlines.append(current_headline)
                    
                elif(document_serialized[index-5]):
                    current_headline = document_serialized[index-5]
                    headlines.append(current_headline)
                else:
                    print("\033[1;31;93m Cant find headline... \033[0m")
            else:
                print("\033[1;31;93m Cant find summary... \033[0m")

    return { "summaries": summaries, "headlines": headlines}
            
### Get text for the main section... Warum Sie uns vartrauen konnen
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

### Get pros text
def get_pros_regex(full_text):
    all_pros_list = []

    pros_regex = r"^vorteile(.|\n)*?nachteile"

    all_pros = re.finditer(pros_regex, full_text, flags=re.DOTALL | re.MULTILINE | re.IGNORECASE)

    for match in all_pros:
        con = full_text[match.start():match.end()]
        all_pros_list.append(con)

    return all_pros_list

### Get cons text
def get_cons_regex(full_text):
    all_cons_list = []

    cons_regex = r"^nachteil(.*)"

    all_cons = re.findall(cons_regex, full_text, flags=re.DOTALL | re.MULTILINE | re.IGNORECASE)

    return all_cons

### Get the title input boxes for all 4 products
def add_product_titles(headlines_list):
    product_no = 1
    for headline in headlines_list:
        product_title_input_xpath = f'/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[3]/div[1]/div[1]/div/div[9]/div[2]/div/table/tbody/tr[{product_no}]/td[2]/div[1]/div[2]/div/input'
        product_title_input = webdriver.find_element_by_xpath(product_title_input_xpath)
        product_title_input.send_keys(headline)
        product_no += 1

### Get the pros input boxes for all 4 products
def add_product_pros(pros_list):
    product_no = 1
    for pro in pros_list:
        product_title_input_xpath = f'/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[3]/div[1]/div[1]/div/div[9]/div[2]/div/table/tbody/tr[{product_no}]/td[2]/div[5]/div[2]/textarea'
        product_title_input = webdriver.find_element_by_xpath(product_title_input_xpath)
        product_title_input.send_keys(pro)
        product_no += 1

### Get the pros input boxes for all 4 products
def add_product_cons(cons_list):
    product_no = 1
    for con in cons_list:
        product_title_input_xpath = f'/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[3]/div[1]/div[1]/div/div[9]/div[2]/div/table/tbody/tr[{product_no}]/td[2]/div[6]/div[2]/textarea'
        product_title_input = webdriver.find_element_by_xpath(product_title_input_xpath)
        product_title_input.send_keys(con)
        product_no += 1

### Get the summary input boxes for all 4 products
def add_product_sum(sum_list):
    product_no = 1
    for sum in sum_list:
        product_title_input_xpath = f'/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[3]/div[1]/div[1]/div/div[9]/div[2]/div/table/tbody/tr[{product_no}]/td[2]/div[2]/div[2]/div/input'
        product_title_input = webdriver.find_element_by_xpath(product_title_input_xpath)
        product_title_input.send_keys(sum)
        product_no += 1

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\mesic\\AppData\\Local\\Google\\Chrome\\User Data")

webdriver = webdriver.Chrome(executable_path='C:\\Users\\mesic\\OneDrive\\Documents\\chromedriver.exe', chrome_options=options)
webdriver.get('https://osp.expertentesten.de/wp-admin/post-new.php')

full_text = get_full_text()

title_text = get_title_text()
main_text = get_main_section()

headlines_and_summaries = get_all_product_headlines()

pros = get_pros_regex(full_text)
cons = get_cons_regex(full_text)

### Run tests!!!
tests(full_text)

# Title input
title = webdriver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[1]/div[1]/div[1]/input')
# Intro input
intro = webdriver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[3]/div[1]/div[1]/div/div[3]/div[2]/textarea')
# Main Text Input
main_text_area = webdriver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[3]/div[1]/div[1]/div/div[5]/div[2]/div/div[2]/textarea')
# Add Product Button
add_product_button = webdriver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[3]/div[1]/div[1]/div/div[9]/div[2]/div/div/a')
# Add Category Checkbox
add_category_checkbox = webdriver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[2]/div/div[2]/div/div/div[2]/ul/li[2]/label')

### Get intro text
intro_text = get_intro_text()

##
###
#### DOM Elements Actions
###
##

### Enter the intro text
intro.send_keys(intro_text)

### Add all products in DOM
for i in range(3):
    add_product_button.click()
    time.sleep(1)

### Move to element and click on it. This is to add the category.
actions = ActionChains(webdriver)
actions.move_to_element(add_category_checkbox).click().perform()

### Add main title
title.send_keys(title_text)

### Add main text
main_text_area.send_keys(main_text)

### Adding product headlines
add_product_titles(headlines_and_summaries['headlines'])

add_product_pros(pros)

add_product_cons(cons)

add_product_sum(headlines_and_summaries['summaries'])