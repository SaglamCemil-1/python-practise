#arama yapma değiştirme regular expressions
# bir satırda birşeyi atayıp if ile kontrol edilecekse
# sadece = kullanılamaz := kullanılmalıdır
import re
"""
email = input("E mail: ").strip().lower()

if re.search(r"^[^@]+@[^@]+\.edu$^",email):
    diff = r"^.+@.+\.edu$"
    better_1 = (r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.edu$^",email)
    better_2 = (r"^\w+@\w+\.edu$^",email)
    better_3 = (r"^\w+@\w+\.(com|edu)$^",email)

    ### re.search(pattern,string,flags = 0)

    #^ -> başlasın 
    #. -> herhangi bir karakter
    #+ -> .nın bir veya daha fazla olması
    # yani xxxx @ yyyyy 
    #@ -> bu olsun arada
    #\.edu->.dan escape .edu ile bitsin
    # [a-zA-Z0-9] | ^ -> olmasın 
    # \w -> alphanumeric
    # (x|y)$ x yada y ile bitsin
    # (\w|\s) -> alphanumeric + whitespace
    print("valid")
"""
user_name = input("user name: ").strip()

if re.search(r"^[a-zA-Z]+ ?, ?[a-zA-Z]+$",user_name,re.IGNORECASE):
    surname,name = user_name.split(",")
    surname = surname.strip()
    name = name.strip()
    print(f"hello {name} 1 {surname}")
else:
    print(f"hello {user_name}")

url = input("URL: ").strip()

#username = url.replace("https://twitter.com/","")
#          url.removeprefix(https://twitter.com/)

#re.sub(pattern,repl,string,count=,flags=)
username = re.sub(r"^(https?//)?(www\.)?twitter\.com/", "" ,url)
print(f"{username} - is user")
"""
matches = re.search(r"^(https?//)?(www\.)?twitter\.com/(.+)$",url,re.IGNORECASE)
"""
if matches := re.search(r"^(https?//)?(www\.)?twitter\.com/(.+)$",url,re.IGNORECASE):
    #r"?:https ve ?:www kullanılsa group 1 olur 
    print(f"there was",matches.group(3))
