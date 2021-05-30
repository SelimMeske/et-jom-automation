import re, time

def tests(full_text):
    ### Test if all products have summary, pros and cons
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