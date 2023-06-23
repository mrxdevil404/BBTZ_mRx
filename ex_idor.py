from re import search
from colorama import Fore
from sys import argv
w = Fore.WHITE
r = Fore.RED
c = Fore.CYAN
g = Fore.GREEN
def ch_id( name_f ):
        emails = []
        f_s = open("results_midor.txt" , 'a')
        with open(name_f , 'r')as f:
            for check in f.readlines():
                check = check.rstrip()
                check_l = check.split('/')
                for check_ in check_l:
                    if check_.isnumeric() and ( ".js" not in check or ".css" not in check ):
                        print (f"{w}[{r}+{w}] {c} {check_} {g} -> {r} {check}")
                        f_s.write(check + '\n')
                    match_ = search(r'=\b\d+\b',check)
                    if match_ and check not in emails:
                        print (f"{w}[{r}+{w}] {c} {match_.group(0)} {g} -> {r} {check}")
                        f_s.write(check + '\n')
                        emails.append(check)
                    else:
                        match = search(r'[\w.+-]+@[\w-]+\.[\w.-]+', check)
                        if match and check not in emails:
                            print (f"{w}[{r}+{w}] {c} {match.group(0)} {g} -> {r} {check}")
                            f_s.write(check + '\n')
                            emails.append(check)
        f_s.close()
ch_id(argv[1])
