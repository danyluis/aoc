# Advent of Code 2018
# https://adventofcode.com/2018/day/4
# Dany Farina (danyluis@gmail.com)

from datetime import *
from sys import *
from collections import *

# TODO : move awake to sleeping to simplify counts

def buildTimeline(events):
    eventQueue = deque(events)
    awake = True
    timeline = [-1] * 60
    timeline[0] = True
    for time, awake in events:
        timeline[time.minute] = awake
    for i in xrange(1, 60):
        if timeline[i] == -1:
            timeline[i] = timeline[i-1]
    return timeline

def sleepTime(tls):
    return sum([len(filter(lambda x: not x, tl)) for tl in tls])

def getSleepiest(gtls):
    sleepStats = defaultdict(list)
    maxt = -1
    guard = None
    for g in gtls.keys():
        st = sleepTime(gtls[g])
        sleepStats[st].append(g)
        if st > maxt:
            maxt = st
            guard = g
    return (guard, sleepStats)

def getSleepiestMinute(tls):
    def sleepCount(m):
        return sum([0 if tls[i][m] else 1 for i in xrange(len(tls))])
    mx = -1
    mxMin = 0
    for m in xrange(60):
        sc = sleepCount(m)
        if sc > mx:
            mx = sc
            mxMin = m
    return mxMin

events = []
for line in stdin.readlines():
    line = line[1:]
    dtstr, rest = line.split("]")
    dt = datetime.strptime(dtstr, '%Y-%m-%d %H:%M')
    rest = rest.replace("#", "").strip()
    events.append((dt, rest))
 
events.sort(key=lambda evt: evt[0])

guard = 0
for i, (dt, rest) in enumerate(events):
    if dt.hour == 23:
        dt += timedelta(hours=1)
        dt = datetime(dt.year, dt.month, dt.day, 0, 0, 0)

    parts = rest.split()

    if parts[0] == 'Guard':
        guard     = int(parts[1])
        events[i] = (dt, guard, True)

    elif parts[0] == 'falls':
        events[i] = (dt, guard, False)

    elif parts[0] == 'wakes':
        events[i] = (dt, guard, True)

tree = defaultdict(lambda: defaultdict(list))
for dt, guard, awake in events:
    day = date(dt.year, dt.month, dt.day)
    tree[guard][day].append((dt, awake))

timelines = defaultdict(list)
for guard in tree.keys():
    for date in tree[guard]:
        timelines[guard].append(buildTimeline(tree[guard][date]))

sleepiestGuard, stats  = getSleepiest(timelines)
sleepiestMinute = getSleepiestMinute(timelines[sleepiestGuard])

for k in sorted(stats.keys()):
    print "sleep {} => {}".format(k, " ".join([str(i) for i in stats[k]]))

print "sleepiestGuard={}, sleepiestMinute={}".format(sleepiestGuard, sleepiestMinute)
print sleepiestGuard * sleepiestMinute

