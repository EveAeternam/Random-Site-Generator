# Random-Site-Generator
![Last Commit](https://img.shields.io/github/last-commit/EveAeternam/Random-Site-Generator?style=plastic)

Generates random URLs from lists of words and domains. These web URLs are almost guaranteed not to work, and will generate completely random links based on dictionaries. This is ideal to test browsers, caching, DNS, or any other network utility that needs large sets of random websites.

![Live Demo](https://img.shields.io/badge/Try%20the-Live%20demo!-ff69b4?style=for-the-badge&logo=github&link=http://www.google.com)

## Examples / Samples
Here are 10 samples each generated with the generator.
**Simple URL:**
```phone.nippy.barsy.net/
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
```competition.battle.hobbl.no/blank.asp
competition.friction.cultural.museum/index.html
caption.cagey.kunitachi.tokyo.jp/home.html
glistening.hit.hinohara.tokyo.jp/home.php
quartz.hoax.art.dz/home.php
number.listen.oi.kanagawa.jp/null.js
charming.string.telebit.app/null.
grind.efficacious.no.eu.org/blank.asp
cart.pumped.gov.sc/hippo.asp
shoes.jumbled.arts.museum/hippo
```

**Complex URL with Parameters**
```alleged.crowded.gy/index.html?development=2&weight=1&possible=3
material.actually.from-wv.com/hippo.?glamorous=true&caress=7&profuse=4&feet=0&impossible=8&nappy=false
sponge.person.notogawa.shiga.jp/hippo.js?sparkle=false&breath=4&ignore=true&catch=4&dispose=8&tearful=7&frighten=0&reach=9&hospital=9
skate.press.is-a-linux-user.org/file.php?draconian=4&grip=5&mind=true&steel=9
trains.parched.ly/download.asp?third=9&limping=false&dime=9&absent=0&birth=1&science=false&fish=true&stick=4&bite=2&sofa=8
scant.amusing.edu.et/hippo.php?nurse=7&class=5&regret=false&unhealthy=0
invite.female.Θúƒσôü/hippo.?eminent=8&undo=8&compare=true&sedate=5&confine=4&actually=4&saddle=4&chemical=4&level=3
hit.berserk.feedback/null.html?collapse=1&dash=0&feel=0&momentous=1&lift=3&vie=1
bawdy.permissible.my/file.js?righteous=3&impede=4&beast=4&staking=1&anger=4&direct=5
tacky.organization.plurinacional.bo/null.js?board=4&get=6&lacking=0&learned=4
```

# Downloads

#### Python
#### C# / .NET
#### PHP
#### JS
#### INO (Arduino)

# Manual
## How To Use
### Simple URL
```python
random_site()
random_site(subd)
```

### Complex URL
```python
random_site() + random_url(0)
random_site(subd) + random_url(0)
```
#### Arguments
**subd**: (*Boolean*) Generate subdomains (Default = True)
**args**: (*Integer*) How many arguments to generate (Default = 3)

#### Returns
**random_site()**: (*String*) Returns random URL
**random_url()**: (*String*) Returns random parameters (without URL)

## Dictionaries
### External Lists
By default each executable will come with the libraries in the same directory. However, should you wish to update it or use a custom list, the Random Site Generator relies on 2 external lists:
- **words.list**: *Contains a list of thousands of random words in plaintext. If running on Linux, it is recommended to append [/usr/share/dict/words] or [/usr/dict/words] to the file. The greater the list, the better the results.*
- **tld.list**: *Contains a list of all valid/approved/recognized Top Level Domains (TLDs) from [https://publicsuffix.org/list/public_suffix_list.dat]*
**Note:** The program ignores empty lines as well as comments started with the double-forward-slash "//".
### Internal Lists
The program also relies on 3 internal lists (hard-coded) that contain small arrays of less important data. These are mainly for URL generation with arguments and parameters in the link. The lists are a follows:
- **RAND_PAGES**: "index", "home", "account", "file", "download", "user", "hippo", "null", "blank", "query"
- **RAND_EXT**: "", "html", "xhtml", "php", "asp", "js"
 - **RAND_ARGS**: "true", "false", '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
### URL Structure
Any URL generated will have the following structure:
* Simple URL:
  * **(subdomain)**.**(domain)**.**(TLD)**/
* Complex URL:
  * **(subdomain)**.**(domain)**.**(TLD)**/(page).(extension)
* Complex URL with parameters:
  * **(subdomain)**.**(domain)**.**(TLD)**/(page).(extension)?*(argument)*=*(value)*&*(argument)*=*(value)*, etc...
