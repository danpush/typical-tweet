from tweepy_cmds import get_trending_tag, get_list_of_tweets, post_tweet, get_trending
from create_sentence import create_sentence, choose_random_word
import time

def tweets_to_dictionaries(tweets: list) -> tuple:
    """Given a list of tweets, return a tuple of:
    first words: dictionary where key is a word and the value is the amount of
                times that word has appeared
    follower words: dictionary where key is a word and the values are
                dictionaries where the keys are the possible words following
                any given word with the value the number of times they have
                appeared (a key of None means the sentence ends)

    >>> tweets = ['hello #world', 'our #world']
    >>> first_words, follower_words = tweets_to_dictionaries(tweets)
    >>> first_words
    {'hello': 1, 'our': 1}
    >>> follower_words
    {'hello': {'#world': 1}, '#world': {None: 2}, 'our': {'#world': 1}}
    """
    first_words = {}  # Dictionary where key is word and value is number of times it was used
    follower_words = {}  # Dictionary where key is word, and value is dictionary where key is word and value is number of times it was used
    for tweet in tweets:
        words = tweet.split()
        if words[0] not in first_words:
            first_words[words[0]] = 1
        else:
            first_words[words[0]] += 1

        for i in range(len(words) - 1):

            if words[i] not in follower_words:
                follower_words[words[i]] = {words[i + 1]: 1}
            else:  # words[i] is in next_word
                if words[i + 1] not in follower_words[words[i]]:
                    follower_words[words[i]][words[i + 1]] = 1
                else:
                    follower_words[words[i]][words[i + 1]] += 1

        # last word:
        if words[-1] not in follower_words:
            follower_words[words[-1]] = {None: 1}
        elif None not in follower_words[words[-1]]:
            follower_words[words[-1]][None] = 1
        else:
            follower_words[words[-1]][None] += 1

    return first_words, follower_words,


def reformat_tweets(tweets: list) -> list:
    """Return a list of tweets identical to <tweets> except all lowercase,
    without links and with some other minor adjustments.

    >>> tweets = ['Today is i monday #day', 'Earth #day is (tmrw &amp always)']
    >>> reformat_tweets(tweets)
    ['today is I monday #day', 'earth #day is tmrw and always']
    """
    new_tweets = []
    for tweet in tweets:
        words = tweet.lower().split(' ')
        sentence = ''
        for word in words:
            if '@' not in word and 'https://' not in word:

                if '"' in word:
                    word = word.replace('"', '')
                if '(' in word:
                    word = word.replace('(', '')
                if ')' in word:
                    word = word.replace(')', '')
                if '&amp' in word:
                    word = word.replace('&amp', 'and')
                if word == 'i':
                    word == 'I'

                sentence += word + ' '
        new_tweets.append(sentence[:-1])
    return new_tweets


def main():
    trending_tag = get_trending(23424977)  # US is 23424977, WW is 1
    hashtag = trending_tag['name']
    query = trending_tag['query']

    print("Trending tag: " + hashtag)
    # hashtag = '#myfirstTweet'
    # query = 'myfirstTweet'

    tweets = get_list_of_tweets(query, 100, 15)
    tweets = reformat_tweets(tweets)

    first_words, follower_words = tweets_to_dictionaries(tweets)

    print("Unique words:", len(follower_words))

    condition = False
    while not condition:
        sentence = create_sentence(first_words, follower_words)
        if hashtag.lower() not in sentence:
            sentence += ' ' + hashtag
        condition = (len(sentence) <= 280)
    print(sentence)
    post_tweet(sentence)

    # Following line is included if you want this to run every hour.
    # time.sleep(60*60)


if __name__ == '__main__':
    main()
    import doctest
    # doctest.testmod()
    # tweet("tweepy api test")
