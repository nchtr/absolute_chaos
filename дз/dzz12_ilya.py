import re
#1
def email(email_address):
    ch = re.findall(r"([^@&]+)@([\w_-][\w_\.-]*\.[\w_-]{2,})$", email_address)
    if not ch:
        raise ValueError(f"wrong email: {email_address}")
    return dict(zip(["username", "domain"], ch[0]))
print(email(input()))

#2
a=input().split()
print(a)
chars = "aeiou"
res = [x for x in a if re.match(f"^[{chars}]", x)]
print(str(res))


#3
text=input()
print(re.split('; |, |\*|\n',text))
