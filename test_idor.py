from colorama import Fore
from sys import argv
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
w = Fore.WHITE
r = Fore.RED
c = Fore.CYAN
g = Fore.GREEN
y = Fore.YELLOW
def test_id(  name_f ):
        n = [5 , 1, 10 , 100]
        leng_old = []
        with open(name_f , 'r')as ff:
            for check in ff.readlines():
                check = check.rstrip()
                check_l = check.split('/')
                for check_ in check_l:
                    if check_.isnumeric():
                        req = requests.get(check ,verify=False )
                        if req.status_code in range(199,404):
                            print(f'{w}[{r}+{w}] {check} -> {str(req.status_code)} status_code')
                            leng_old.append(len(req.text))
                            for nn in n:
                                check_2 = int(check_) - nn
                                new_url = check.replace(check_ , str(check_2) , 1)
                                req2 = requests.get(new_url , verify=False )
                                if req2.status_code in range(199,404):
                                    print(f'{w}[{r}+{w}] {new_url} -> {str(req2.status_code)} status_code')
                                    for numb in leng_old:
                                        if abs((len(req2.text) - numb)) > 5:
                                            print (f'{w}[{r}+{w}] {g}Idor {y} -> {c} {check}')
                                            break
test_id( argv[1] )
