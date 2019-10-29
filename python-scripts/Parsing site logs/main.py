import re
import collections


if __name__ == "__main__":
    recs = []
    top_users = collections.Counter()
    top_platforms = collections.Counter()

    record = collections.namedtuple('record', "ip date request url answer_code base_url system_information")
    with open("access.log") as infile:
        for line in infile:
            p = re.search(r'(\d+\.\d+\.\d+\.\d+).+\[(.+)] "([A-Z]+) ([^"]*)" (\d+) \d+ "([^"]*)" "([^"]+)"', line)
            recs.append(record(p.group(1), p.group(2), p.group(3), p.group(4), p.group(5), p.group(6), p.group(7)))

    for item in recs:
        top_users[item.ip] += 1
        top_platforms[item.system_information] += 1
    print(top_users.most_common(10))
    print(top_platforms.most_common(5))
