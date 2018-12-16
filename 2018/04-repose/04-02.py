# Advent of Code 2018
# https://adventofcode.com/2018/day/4
# Dany Farina (danyluis@gmail.com)

from datetime import *
from sys import *
from collections import *

# TODO : move awake to sleeping to simplify counts

def buildTimeline(events):
    timeline = [-1] * 60
    timeline[0] = True
    for time, awake in events:
        timeline[time.minute] = awake
    for i in xrange(1, 60):
        if timeline[i] == -1:
            timeline[i] = timeline[i-1]
    return timeline

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
        guard = int(parts[1])
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

maxSlept = -1
sleepiestMinute = None
sleepiestGuard = None
for minute in xrange(60):
    for guard in timelines.keys():
        slept = 0
        for guardAwake in timelines[guard]:
            slept += 0 if guardAwake[minute] else 1
        if slept > maxSlept:
            maxSlept = slept
            sleepiestGuard = guard
            sleepiestMinute = minute 

print "sleepiestGuard={}, sleepiestMinute={}".format(sleepiestGuard, sleepiestMinute)
print sleepiestGuard * sleepiestMinute

