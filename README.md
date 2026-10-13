# Random-Site-Generator
![Last Commit](https://img.shields.io/github/last-commit/EveAeternam/Random-Site-Generator?style=plastic)
![Python 3](https://img.shields.io/badge/python-3.8%2B-blue?style=plastic)

Generates random URLs from lists of words and domains. These web URLs are almost guaranteed not to work, and will generate completely random links based on dictionaries. This is ideal to test browsers, caching, DNS, or any other network utility that needs large sets of random websites.

## Examples / Samples
Here are 10 samples of each kind, generated with the script.

**Simple URL:**
```
phone.nippy.barsy.net/
part.stem.choyo.kumamoto.jp/
spot.inconclusive.cyon.site/
sway.plain.biz.gl/
prevent.obtainable.lidl/
bikes.motionless.warman/
donkey.obtain.uzhgorod.ua/
add.plead.development.run/
soggy.grouchy.apartments/
even.cemetery.kitakata.fukushima.jp/
```

**Complex URL with Page:**
```
competition.battle.hobbl.no/blank.asp
competition.friction.cultural.museum/index.html
caption.cagey.kunitachi.tokyo.jp/home.html
glistening.hit.hinohara.tokyo.jp/home.php
quartz.hoax.art.dz/home.php
number.listen.oi.kanagawa.jp/null.js
charming.string.telebit.app/null
grind.efficacious.no.eu.org/blank.asp
cart.pumped.gov.sc/hippo.asp
shoes.jumbled.arts.museum/hippo
```

**Complex URL with Parameters**
```
alleged.crowded.gy/index.html?development=2&weight=1&possible=3
material.actually.from-wv.com/hippo?glamorous=true&caress=7&profuse=4&feet=0&impossible=8&nappy=false
sponge.person.notogawa.shiga.jp/hippo.js?sparkle=false&breath=4&ignore=true&catch=4&dispose=8&tearful=7&frighten=0&reach=9&hospital=9
skate.press.is-a-linux-user.org/file.php?draconian=4&grip=5&mind=true&steel=9
trains.parched.ly/download.asp?third=9&limping=false&dime=9&absent=0&birth=1&science=false&fish=true&stick=4&bite=2&sofa=8
scant.amusing.edu.et/hippo.php?nurse=7&class=5&regret=false&unhealthy=0
invite.female.食品/hippo?eminent=8&undo=8&compare=true&sedate=5&confine=4&actually=4&saddle=4&chemical=4&level=3
hit.berserk.feedback/null.html?collapse=1&dash=0&feel=0&momentous=1&lift=3&vie=1
bawdy.permissible.my/file.js?righteous=3&impede=4&beast=4&staking=1&anger=4&direct=5
tacky.organization.plurinacional.bo/null.js?board=4&get=6&lacking=0&learned=4
```

## Usage
Requires Python 3.8 or later and nothing outside the standard library.

```
python3 src/python/gen-rand-web.py [options]
```

| Option | Default | What it does |
|---|---|---|
| `-c`, `--count N` | 1 | Number of URLs to generate |
| `-s`, `--subdomains true\|false` | true | Use a random word as the subdomain; `false` uses `www` |
| `-p`, `--page true\|false` | true | Add a random page, extension and query parameters; `false` gives a simple URL |
| `-a`, `--max-args N` | 10 | Maximum number of query parameters per URL |
| `--words PATH` | `lib/words.list` | Words list to use |
| `--tlds PATH` | `lib/tld.list` | TLD list to use |
| `--seed N` | none | Random seed, for repeatable output |
| `-v`, `--verbose` | off | Print each pick to stderr |
| `-h`, `--help` | | Show help |

**Examples:**
```
python3 src/python/gen-rand-web.py -c 10                    # 10 full URLs
python3 src/python/gen-rand-web.py -c 10 -p false           # 10 simple URLs
python3 src/python/gen-rand-web.py -c 5 -s false -a 3       # www. URLs with up to 3 parameters
python3 src/python/gen-rand-web.py -c 1000 > urls.txt       # a test set for a browser, cache or DNS tool
```

### Using it from Python
```python
import importlib.util
spec = importlib.util.spec_from_file_location("gen", "src/python/gen-rand-web.py")
gen = importlib.util.module_from_spec(spec); spec.loader.exec_module(gen)

g = gen.Generator(gen.load_list("lib/words.list"), gen.load_tlds("lib/tld.list"))
g.generate()                        # full URL with up to 10 parameters
g.generate(subdomains=False)        # www.(domain).(tld)/...
g.generate(page=False)              # simple URL
g.random_site()                     # (subdomain).(domain).(tld)/
g.random_url(arguments=3)           # (page).(ext)?a=1&b=2&c=3
```

## Dictionaries
### External lists
Both lists live in `lib/`. The script looks next to itself first and then in `lib/`, so you can copy the script and lists into one folder, or point at your own lists with `--words` and `--tlds`.
- **words.list**: thousands of random words in plain text, one per line. On Linux you can append `/usr/share/dict/words` for more variety; the bigger the list, the better the results.
- **tld.list**: the [Public Suffix List](https://publicsuffix.org/list/public_suffix_list.dat). Wildcard rules (`*.ck`) are used as their base suffix and exception rules (`!www.ck`) are skipped.

Both lists ignore empty lines and comments starting with `//`.

### Internal lists
Three small hard-coded lists fill in pages and parameters:
- **RAND_PAGES**: "index", "home", "account", "file", "download", "user", "hippo", "null", "blank", "query"
- **RAND_EXT**: "" (no extension), "html", "xhtml", "php", "asp", "js"
- **RAND_ARGS**: "true", "false", '0' to '9'

### URL structure
* Simple URL:
  * **(subdomain)**.**(domain)**.**(TLD)**/
* Complex URL:
  * **(subdomain)**.**(domain)**.**(TLD)**/(page).(extension)
* Complex URL with parameters:
  * **(subdomain)**.**(domain)**.**(TLD)**/(page).(extension)?*(argument)*=*(value)*&*(argument)*=*(value)*, etc.

## License
[MIT](LICENSE)
