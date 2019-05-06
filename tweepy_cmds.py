import tweepy

CONSUMER_KEY = 'XXXXXX'
CONSUMER_SECRET = 'XXXXXX'
ACCESS_KEY = 'XXX-XXX'
ACCESS_SECRET = 'XXXXXX'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def get_trending_tag(woeid: int) -> str:
    """Return the most popular hashtag in <woeid> (Yahoo! Where On Earth ID), 1
    is global, USA is 23424977

    Requirement: There exists at least one trending hashtag

    >>> get_trending_tag(1)
    """
    data = api.trends_place(woeid)  # get trending topics

    trends = data[0]['trends']

    # find most popular hashtag (instead of most popular trend)
    index = 0
    while index < len(trends) and trends[index]['name'][0] != '#':
        index += 1

    return trends[index]


def get_trending(woeid: int) -> str:
    data = api.trends_place(woeid)  # get trending topics
    trends = data[0]['trends']
    return trends[0]


def get_list_of_tweets(query: str, count: int, pages: int) -> list:
    """Return a list of tweets that are not retweets and are found by <query>.
    The length of the returned list is <count>*<pages>

    count <= 100
    """
    n_words = 0
    pages = tweepy.Cursor(api.search, q=(query+'-filter:retweets'),
                          count=count, tweet_mode='extended', lang='en').pages(pages)

    tweets = []  # list of tweets
    for page in pages:
        for tweet in page:
            text = tweet.full_text
            tweets.append(text)
            n_words += 1 + text.count(' ')

    print("Tweets found:", len(tweets))
    print("Words found:", n_words)
    return tweets


def post_tweet(s: str) -> None:
    """Post a tweet <s>
    """
    api.update_status(s)
