import hashlib

md5 = open("md5.csv","a")
sha1 = open("sha1.csv","a")
sha224 = open("sha224.csv","a")
sha256 = open("sha256.csv","a")
sha384 = open("sha384.csv","a")
sha512 = open("sha512.csv","a")
dictionary = open("words.txt","r")
all_words = dictionary.read().split("\n")
for x in all_words:
    if not "," in x:
        md5.write(f"{x},{hashlib.md5(x.encode()).hexdigest()}\n")
        sha1.write(f"{x},{hashlib.sha1(x.encode()).hexdigest()}\n")
        sha224.write(f"{x},{hashlib.sha224(x.encode()).hexdigest()}\n")
        sha256.write(f"{x},{hashlib.sha256(x.encode()).hexdigest()}\n")
        sha384.write(f"{x},{hashlib.sha384(x.encode()).hexdigest()}\n")
        sha512.write(f"{x},{hashlib.sha512(x.encode()).hexdigest()}\n")
md5.close()
sha1.close()
sha224.close()
sha256.close()
sha384.close()
sha512.close()
