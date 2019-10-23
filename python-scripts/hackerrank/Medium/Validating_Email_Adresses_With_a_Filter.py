import re


def fun(s):
    return re.search(r"^[a-zA-Z][\w-]*@[0-9a-zA-Z]+\.[a-zA-Z]{1,3}$", s)


def filter_mail(mails):
    return list(filter(fun, mails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())
    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
