def pros_cons_parser(string):
    string = string.replace('Vorteile:', '')
    string = string.replace('vorteile:', '')
    string = string.replace('Vorteil:', '')
    string = string.replace('vorteil:', '')
    
    string = string.replace('Nachteile:', '')
    string = string.replace('nachteile:', '')
    string = string.replace('Nachteil:', '')
    string = string.replace('nachteil:', '')

    return string