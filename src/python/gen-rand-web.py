#!/usr/bin/env python3
"""Generate random (almost certainly non-existent) URLs from word and TLD lists."""

import argparse
import os
import random
import sys

RAND_ARGS = ["true", "false", '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
RAND_PAGES = ["index", "home", "account", "file", "download", "user", "hippo", "null", "blank", "query"]
RAND_EXT = ["", "html", "xhtml", "php", "asp", "js"]

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
LIB_FOLDER = os.path.normpath(os.path.join(THIS_FOLDER, '..', '..', 'lib'))


def find_list(name):
    """Look for a list next to the script first, then in the repo's lib/ folder."""
    for folder in (THIS_FOLDER, LIB_FOLDER):
        path = os.path.join(folder, name)
        if os.path.isfile(path):
            return path
    return os.path.join(LIB_FOLDER, name)


def load_list(fname):
    """Read a list file, skipping blank lines and // comments."""
    entries = []
    with open(fname, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("//"):
                entries.append(line)
    return entries


def load_tlds(fname):
    """Read the public suffix list, turning wildcard rules into plain suffixes."""
    tlds = []
    for line in load_list(fname):
        if line.startswith("!"):
            continue  # exception rules, not suffixes
        if line.startswith("*."):
            line = line[2:]
        tlds.append(line)
    return tlds


class Generator:
    def __init__(self, words, tlds, verbose=False):
        self.words = words
        self.tlds = tlds
        self.verbose = verbose

    def pick(self, entries, label):
        i = random.randrange(len(entries))
        if self.verbose:
            print("picked: '%s' from %s line %d" % (entries[i], label, i), file=sys.stderr)
        return entries[i]

    def random_site(self, subdomains=True):
        domain = self.pick(self.words, "words")
        tld = self.pick(self.tlds, "tld")
        subdomain = self.pick(self.words, "words") if subdomains else "www"
        return subdomain + '.' + domain + '.' + tld + '/'

    def random_url(self, arguments=3):
        page = random.choice(RAND_PAGES)
        ext = random.choice(RAND_EXT)
        url = page + ('.' + ext if ext else '')
        params = [self.pick(self.words, "words") + '=' + random.choice(RAND_ARGS)
                  for _ in range(arguments)]
        if params:
            url += '?' + '&'.join(params)
        return url

    def generate(self, subdomains=True, page=True, max_args=10):
        url = self.random_site(subdomains)
        if page:
            url += self.random_url(random.randint(0, max_args))
        return url


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Generate random URLs from lists of words and top-level domains.")
    parser.add_argument('-c', '--count', type=int, default=1,
                        help="number of URLs to generate (default: 1)")
    parser.add_argument('-s', '--subdomains', choices=['true', 'false'], default='true',
                        type=str.lower,
                        help="use a random word as the subdomain instead of 'www' (default: true)")
    parser.add_argument('-p', '--page', choices=['true', 'false'], default='true',
                        type=str.lower,
                        help="add a random page and query parameters (default: true)")
    parser.add_argument('-a', '--max-args', type=int, default=10,
                        help="maximum number of query parameters per URL (default: 10)")
    parser.add_argument('--words', default=find_list('words.list'),
                        help="path to the words list (default: lib/words.list)")
    parser.add_argument('--tlds', default=find_list('tld.list'),
                        help="path to the TLD list (default: lib/tld.list)")
    parser.add_argument('--seed', type=int, help="random seed, for repeatable output")
    parser.add_argument('-v', '--verbose', action='store_true',
                        help="print each pick to stderr")
    args = parser.parse_args(argv)
    if args.count < 0:
        parser.error("--count must be 0 or more")
    if args.max_args < 0:
        parser.error("--max-args must be 0 or more")
    return args


def main(argv=None):
    args = parse_args(argv)
    if args.seed is not None:
        random.seed(args.seed)
    gen = Generator(load_list(args.words), load_tlds(args.tlds), args.verbose)
    for _ in range(args.count):
        print(gen.generate(args.subdomains == 'true', args.page == 'true', args.max_args))


if __name__ == '__main__':
    main()
