import ast
import re
import csv

# Following program is the python implementation of
# Rabin Karp Algorithm given in CLRS book

# d is the number of characters in the input alphabet
d = 256


# pat  -> pattern
# txt  -> text
# q    -> A prime number

def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    h = 1
    listNum = []

    # The value of h would be "pow(d, M-1)% q"
    for i in range(M - 1):
        h = (h * d) % q

        # Calculate the hash value of pattern and first window
    # of text
    for i in range(M):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

        # Slide the pattern over text one by one
    for i in range(N - M + 1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if p == t:
            # Check for characters one by one
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break

            j += 1
            # if p == t and pat[0...M-1] = txt[i, i + 1, ...i + M-1]
            if j == M:
                #                 print ("Pattern found at index " + str(i) )
                listNum.append(i)

        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q

            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t + q

    return listNum




test_file = open("news_feed/Tokyo.txt", "r")

text_in_file = test_file.read()

text_in_file = text_in_file.lower()
text_in_file =  text_in_file.replace("\n" , " \n ")


stop_word ="""a
about
above
after
again
against
all
am
an
and
any
are
aren't
as
at
be
because
been
before
being
below
between
both
but
by
can't
cannot
could
couldn't
did
didn't
do
does
doesn't
doing
don't
down
during
each
few
for
from
further
had
hadn't
has
hasn't
have
haven't
having
he
he'd
he'll
he's
her
here
here's
hers
herself
him
himself
his
how
how's
i
i'd
i'll
i'm
i've
if
in
into
is
isn't
it
it's
its
itself
let's
me
more
most
mustn't
my
myself
no
nor
not
of
off
on
once
only
or
other
ought
our
ours	ourselves
out
over
own
same
shan't
she
she'd
she'll
she's
should
shouldn't
so
some
such
than
that
that's
the
their
theirs
them
themselves
then
there
there's
these
they
they'd
they'll
they're
they've
this
those
through
to
too
under
until
up
very
was
wasn't
we
we'd
we'll
we're
we've
were
weren't
what
what's
when
when's
where
where's
which
while
who
who's
whom
why
why's
with
won't
would
wouldn't
you
you'd
you'll
you're
you've
your
yours
yourself
yourselves
"""

stop_words = stop_word.split()

print("\n********************************************\nSTOPWORD COUNTER\n********************************************")

dict ={}
for word in stop_words:
    print("Stopword : ", word, "  |  Length:", len(word))
    indexWord = search(word + " ", text_in_file, 977)

    if len(indexWord) != 0:
        i = 0
        for each in indexWord:
            i += 1
            print(each, text_in_file[each: each + len(word) + 1])

        dict[word] = i
        print("Stopword count :", i)

    print()

'''
Stopword Count
BeijingCSV.txt
BruneiCSV.txt
HanoiCSV.txt
JakartaCSV.txt
MelbourneCSV.txt
SingaporeCSV.txt
TaipeiCSV.txt
TokyoCSV.txt
'''

with open("TokyoCSV.csv", mode='w', newline='') as csv_file:
    fieldnames = ['Word', 'Frequency']
    w = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')
    w.writeheader()
    for word in stop_words:
        indexWord = search(word + " ", text_in_file, 977)

        if len(indexWord) != 0:
            i = 0
            for each in indexWord:
                i += 1
                print(each, text_in_file[each: each + len(word) + 1])

            dict[word] = i
        w.writerow({'Word' : word, 'Frequency' : i})

f = open("Tokyo.txt", "w")



print("\n********************************************\nDELETED STOPWORDS SAVE IN FILE\n********************************************")
for word in stop_words:
    text_in_file = re.sub(" " + word + " " , " ", text_in_file)
f.write(text_in_file)
f.close()








