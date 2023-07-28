import pwiki.gquery
import pwiki.wiki
import pwiki.ns
import pwiki.wparser
from mastodon import Mastodon

def get_random_page():
    wiki = pwiki.wiki.Wiki("en.wikipedia.org/")

    generator = pwiki.gquery.GQuery.random(wiki, ns=[pwiki.ns.NS(0)])
    page = generator.__next__()[0]

    return page

def convert_to_url(page):
    return "https://en.wikipedia.org/wiki/" + page.replace(" ", "_")

def post():
    mastodon = Mastodon(
        access_token='token.secret',
        api_base_url='https://botsin.space/'
    )
    page = "ERROR - DID NOT FIND ARTICLE"
    try:
        page = get_random_page()
    except:
        print("ERROR - WikiBot encountered error while finding article")

    message = "Today's wikipedia article is " + page + "\n\n" + convert_to_url(page)

    try:
        mastodon.status_post(message, language="en")
    except:
        print("ERROR - WikiBot encountered error while posting")

post()
