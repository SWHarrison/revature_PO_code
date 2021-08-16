'''Write a function that divides a phrase into word buckets, with each
bucket containing n or fewer characters. Only include full words inside
each bucket.'''

def bucketize(words, num):

    buckets = []

    counter = num
    next_bucket = ""

    for word in words.split():
        if next_bucket == "":
            if len(word) <= counter:
                next_bucket += word
                counter -= len(word)
            else:
                pass
        else:
            if len(word) + 1 <= counter:
                next_bucket += " " + word
                counter -= (len(word) + 1)
            else:
                buckets.append(next_bucket)
                counter = num
                next_bucket = ""
                if len(word) <= counter:
                    next_bucket += word
                    counter -= len(word)

    if next_bucket != "":
        buckets.append(next_bucket)
    return buckets

print(bucketize("she sells sea shells by the sea", 10))

print(bucketize("the mouse jumped over the cheese",7))

print(bucketize("fairy dust coated the air", 20))

print(bucketize("a b c d e", 2))
