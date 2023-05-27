from playwright.sync_api import sync_playwright
from threading import Thread, Lock
from playwr import run
from signal import signal, SIGINT
from sys import exit



def main():
    countries = [
        ("de-AT", "austria"),
        # ("de-DE", "germany"),
        ("fr-FR", "france"),
        # ("bg-BG", "bulgaria"),
        ("hr-HR", "croatia"),
        ("cs-CZ", "czechrepublic"),
        ("da-DK", "denmark"),
        # ("et-EE", "estonia"),
        # ("fi-FI", "finland"),
        ("el-GR", "greece"),
        ("hu-HU", "hungary"),
        # ("ga-IE", "ireland"),
        ("it-IT", "italy"),
        # ("lv-LV", "latvia"),
        # ("lt-LT", "lithuania"),
        # ("lb-LU", "luxembourg"),
        # ("mt-MT", "malta"),

        
        ("nl-NL", "netherlands"),
        ("pl-PL", "poland"),


        ("pt-PT", "portugal"),
        # ("ro-RO", "romania"),
        # ("sk-SK", "slovakia"),
        # ("sl-SI", "slovenia"),
        ("es-ES", "spain"),
        ("sv-SE", "sweden")
    ]
    lock1 = Lock()
    lock2 = Lock()
    threads = []
    
    for countrysymbols, countryname in countries:
        threads.append(Thread(target=run, args=(countrysymbols, countryname, lock1, lock2)))

    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()