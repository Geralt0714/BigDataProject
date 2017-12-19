import sys
current_key = None
current_count = 0.0
key = None
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    if len(line)==0:
        continue
    # parse the input we got from mapper.py
    key, count = line.strip().split(',')


    # this IF-switch only works because Hadoop sorts map output
    # by key (here: key) before it is passed to the reducer
    if current_key ==None:
        current_key = key
    if current_key == key:
        current_count += float(count)
    else:
        print ('%s,%s' % (current_key, current_count))
        current_count = float(count)
        current_key = key

# do not forget to output the last key if needed!
if current_key == key:
    print ('%s,%s' % (current_key, current_count))
