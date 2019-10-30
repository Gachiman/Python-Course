import re
import collections


if __name__ == "__main__":
    top_users = collections.Counter()
    top_platforms = collections.Counter()

    with open("access.log") as infile:
        for line in infile:
            ip = re.match(r'\d+\.\d+\.\d+\.\d+', line)
            platform = re.search(r'(Windows NT | Mac OS | FreeBSD)', line)
            top_users[ip.group()] += 1
            try:
                top_platforms[platform.group()] += 1
            except AttributeError:
                top_platforms["Bot"] += 1

    print(top_users.most_common(10))
    print(top_platforms.most_common())
