def sum_parser(string):
    string = string.replace('Summary:', '')
    string = string.replace('Summary :', '')
    string = string.replace('SUMMARY:', '')
    string = string.replace('SUMMARY :', '')
    string = string.replace('Summary', '')
    string = string.replace('summary:', '')
    string = string.replace('summary :', '')
    string = string.replace('summary', '')
    
    string = string.replace('Subheadline:', '')
    string = string.replace('Subheadline :', '')
    string = string.replace('SUBHEADLINE:', '')
    string = string.replace('SUBHEADLINE :', '')
    string = string.replace('Subheadline', '')
    string = string.replace('subheadline:', '')
    string = string.replace('subheadline :', '')
    string = string.replace('subheadline', '')


    return string.strip()