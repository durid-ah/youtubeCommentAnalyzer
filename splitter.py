from sklearn.model_selection import train_test_split

YELP_REVIEW_TXT = 'yelp_reviews.txt'
YELP_TRAIN = 'yelp.split.train'
YELP_TEST = 'yelp.split.test'
TOTAL_LINES = 6685899

f = open(YELP_REVIEW_TXT)
x = f.readlines()
print("Files are read...")
f.close()


print("Closing file and splitting set...")
X_train, X_test = train_test_split(x, test_size=0.17, random_state=42)
print("Set split up")


print("Starting saving training set...")
wftr = open(YELP_TRAIN, 'w+')
count = 0
for item in X_train:
    print("Writing train %", count / (TOTAL_LINES * 0.83))
    wftr.write(item.replace('\n', '') + '\n')
    count += 1
wftr.close()


print("Starting saving test set...")
count = 0
wfte = open(YELP_TEST, 'w+')
for item in X_test:
    print(" Writing test %", count / (TOTAL_LINES * 0.17))
    wfte.write(item.replace('\n', '') + '\n')
    count += 1

wfte.close()
