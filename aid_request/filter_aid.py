import csv
from datetime import datetime

input_files = [
    # 'sample.txt'
    '2017_08_26_stream.txt.csv',
    '2017_08_27_stream.txt.csv',
    '2017_08_28_stream.txt.csv',
    '2017_08_29_stream.txt.csv',
    '2017_08_30_stream.txt.csv',
]


def is_aid_request(tweet):
    if "help" in tweet or "need" in tweet or "demand" in tweet or " aid" in tweet or "urg" in tweet:
        return True

    return False

for input_f in input_files:

    with open(input_f) as f:
        reader = csv.reader(f, delimiter='|', quotechar='"')
        next(reader)
        with open("aid_" + input_f, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["tweet_id", "datetime", "city", "state", "country", "gps", "polygon", "tweet"])

            for row in reader:

                tweet = row[7]
                tweet = tweet.encode()
                udata = tweet.decode("utf-8", "ignore")
                tweet = udata.encode("ascii", "ignore")
                tweet = tweet.decode("ascii", "ignore")
                if is_aid_request(tweet=tweet):
                    writer.writerow(row)
