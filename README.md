# Typical Tweet
This is a Twitter bot that gets the most trending topic, and makes a tweet about it based on others tweets it's read. Currently running on Google's VM Compute Engine f1-micro, but should work on a Raspberry Pi. Loosely based on the Hidden Markov Model.

Often live at: https://twitter.com/PossiblyAndroid

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
Need tweepy module and Twitter Developer app (Consumer API keys and Access token & access token secret).

You can install tweepy with pip (or pip3), note that this is written for python 3.

```
$ pip3 install tweepy
```

You will need a Twitter App with Keys/Secrets. You can make an App at https://developer.twitter.com/en/apply-for-access
You need just the CONSUMER_KEY and CONSUMER_SECRET to get create tweets, but if you want to post them as well you will need the ACCESS_KEY and ACCESS_SECRET.

### Running locally
Clone this repository onto your computer or download the contents as a zip file. Go into tweepy_cmds.py and replace CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, and ACCESS_SECRET with your own Keys/Secrets. If you aren't intending on posting any tweets, feel free to leave ACCESS_KEY and ACCESS_SECRET as is, but comment out line 9.

```python
CONSUMER_KEY = 'XXXXXX'
CONSUMER_SECRET = 'XXXXXX'
ACCESS_KEY = 'XXX-XXX'
ACCESS_SECRET = 'XXXXXX'
```

```python
# auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
```

If you are not planning on posting tweets, make sure to comment out line 108 in main.py (in the main() function)
```python
# post_tweet(sentence)
```

If you want to run this just once, make sure in main.py you're calling the main() function,
```python
if __name__ == '__main__':
    main()
    # run_every(60 * 60 * 4)
```
If you want this to run on an interval, then make sure you're calling the run_every(t) function, where t is time in milliseconds. The following runs every 4 hours
```python
if __name__ == '__main__':
    # main()
    run_every(60 * 60 * 4)
```

### Deployment
You can run this on a Raspberry Pi, any VM, or on your computer with nohup.
```
$ nohup python3 main.py &
```

## License
This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details
