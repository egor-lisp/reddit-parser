from reddit_parser import Reddit_parser


reddit = Reddit_parser()

info = reddit.retrieve_url('https://www.reddit.com/r/pics/comments/rgyuh5/after_30_years_of_mortgage_payments_i_paid_it_off/')
print(info)

