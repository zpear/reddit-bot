import pprint
import praw

user_agent = "Karma breakdown 1.0 by /u/Pearz"
r = praw.Reddit(user_agent=user_agent)

user_name = "Pearz"
user = r.get_redditor(user_name)

post_limit = 10
posts = user.get_submitted(limit=post_limit)

karma_by_subreddit = {}
for post in posts:
	subreddit = post.subreddit.display_name
	karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit, 0) + post.score)

pprint.pprint(karma_by_subreddit)
