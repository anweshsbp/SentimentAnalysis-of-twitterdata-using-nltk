from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


#consumer key, consumer secret, access token, access secret.
ckey="tUgkNrAfz45yvABii9yKofJQE"
csecret="ptNgnz78tgayfluvWrCySLwnBdhHYQatJMopocWRZh1Vnre0P0"

atoken="1219626370684407809-IUGNv7j9uPRzrxYkIthFqLBrdGo8mo"
asecret="k9LRJPskpSKTcFynq2AGOWwwLdDGe4Ma3GfqJAefCiF7L"

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["BJP"])
tweet = all_data["text"]
