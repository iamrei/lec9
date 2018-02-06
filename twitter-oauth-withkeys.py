
from requests_oauthlib import OAuth1Session
import secrets
import json

client_key = secrets.api_key
client_secret = secrets.api_secret

resource_owner_key = secrets.ACCESS_KEY
resource_owner_secret = secrets.ACCESS_SECRET

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food', 'count': 10} #finding 'food' + only 10 tweets
r = oauth.get(protected_url, params=params)
# print (r.text)
r2 = json.loads(r.text)
results = r2["statuses"]
# print(results)

## writing the search results to a json file 
# search_fname = "tweet_search_result.json"
# search_diction = results
# search_str = json.dumps(search_diction)
# cache_f = open(search_fname,"w")
# cache_f.write(search_str)
# cache_f.close()

tweets_lst = []
for status_dic in results:
    tweets_lst.append(status_dic)
# print(tweets_lst)

for tweet in tweets_lst:
	print(tweet['user']['name'] + ': \n' + tweet['text'] + '\n')


