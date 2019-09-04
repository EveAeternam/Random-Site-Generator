import os, sys, random

### SETUP ARGUMENTS
args = str(sys.argv)

if ("-v" in args or "--verbose" in args):
    verbose = True
else:
    verbose = False

if "-c" in args:
    count = args[args.index("-c")+1]
else:
    count = 1

if "-s" in args:
    if (args[args.index("-s")+1] == "True" or args[args.index("-s")+1] == "False"):
        subd = subd = args[args.index("-s")+1]
else:
    subd = True

if ("-h" in args or "--help" in args):
    print("Help text here (TODO)")
    count = 0
###

RAND_ARGS = ["true", "false", '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
RAND_PAGES = ["index", "home", "account", "file", "download", "user", "hippo", "null", "blank", "query"]
RAND_EXT = ["", "html", "xhtml", "php"]

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
path_words = os.path.join(THIS_FOLDER, 'words.list')
path_tlds = os.path.join(THIS_FOLDER, 'tld.list')

def file_len(fname):
    count = 0
    for line in open(fname).xreadlines(  ):
        count += 1
    return count

def random_line(fname):
    line = ""
    while (line == "" or line == "\n" or line.startswith("//")):
        randint = random.randrange(0,file_len(fname))
        lines = open(fname).readlines()
        line = lines[randint].rstrip()
        if (verbose): print("picked: '" + line + "' from line " + str(randint))
    return line

def random_site(subdomains = True):
    site = ""
    domain = random_line(path_words)
    tld = random_line(path_tlds)
    if (subdomains): subdomain = random_line(path_words)
    else: subdomain = "www"
    site = subdomain + '.' + domain + '.' + tld + '/'
    return site

def random_url(arguments = 3):
    page = RAND_PAGES[random.randrange(0,len(RAND_PAGES))]
    ext = RAND_EXT[random.randrange(0,len(RAND_EXT))]
    c = 0
    argument = ""
    while (c < arguments):
        if (c == 0 ):
            argument += "?"
        else:
            argument += "&"
        argument += random_line(path_words)
        argument += "="
        argument += RAND_ARGS[random.randrange(0,len(RAND_ARGS))]
        c += 1
    url = page + '.' + ext + argument
    return url


i = 0
while (i < count):
    print (random_site(subd) + random_url(random.randint(0,10)))
    i += 1
