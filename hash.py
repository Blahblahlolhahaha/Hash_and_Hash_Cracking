import hashlib
import pandas as pan

hash_list = [hashlib.md5,hashlib.sha1,hashlib.sha224,hashlib.sha256,hashlib.sha384,hashlib.sha512]
hash_files = ["md5.csv","sha1.csv","sha224.csv","sha256.csv","sha384.csv","sha512.csv"]
print("Welcome to the Hash Temple!\n")
while True:
    try:
        start = int(input("\nWhat would you like to do today?\n1)Hash something\n2)Crack a Hash!\n3)Exit\n>>>"))
        if not (start == 1 or start == 2 or start == 3):
            raise ValueError
        elif start == 3:
            break
        elif start == 1:
            while True:
                try:
                    hash_function = int(input("What hash alogorithm would you like to use?\n1)md5\n2)sha1\n3)sha224\n4)sha256\n5)sha384\n6)sha512\n7)Exit\n>>>"))
                    if hash_function < 1 or hash_function > 7:
                        raise ValueError
                    elif hash_function == 7:
                        break
                    plaintext = input("Input the string you want to hash (type 'file' if you want to read from a file) >>> ")
                    if plaintext == "'file'" :
                        try:
                            file_path = input("Input ABSOLUTE PATH of the file you want >>> ")
                            with open(file_path,"r") as all_of_them:
                                word_list = all_of_them.read().split("\n")
                            ciphertext = {x : hash_list[hash_function-1](x.encode()).hexdigest() for x in word_list}
                            print("Here are the results!")
                            for x,y in ciphertext.items():
                                print(f"{x} : {y}\n")
                            while True:
                                try:
                                    consent = input("Would you allow us to add the words to our database? Press y to accept, n to reject.\n>>> ")
                                    if consent.casefold() == "y":
                                        for x in word_list:
                                            if not "," in x:
                                                df = pan.read_csv("md5.csv",delimiter=",")
                                                found = False
                                                for z in df['text']:
                                                    if z == plaintext:
                                                        found = True
                                                        break
                                                if not found:
                                                    for y in range (hash_list.__len__()):
                                                        filee = open(hash_files[y],"a")
                                                        filee.write(f"{x},{hash_list[y](x.encode()).hexdigest()}\n")
                                                
                                        break
                                    elif consent.casefold() == "n":
                                        break
                                    else:
                                        raise NameError
                                except NameError as e:
                                    print(e)
                                    print("Enter y or n!")
                        except FileNotFoundError:
                            print("File is not found!")
                    else:
                        algo = hash_list[hash_function-1]
                        ciphertext = algo(plaintext.encode()).hexdigest()
                        print(f"The hash is {ciphertext}!")
                        df = pan.read_csv("md5.csv",delimiter=",")
                        found = False
                        for x in df['text']:
                            if x == plaintext:
                                found = True
                                break
                        if not found:
                            while True:
                                    try:
                                        consent = input("Would you mind if we add the words to our database? Press y to accept, n to reject.\n>>> ")
                                        if consent.casefold() == "y":
                                            for y in range (hash_list.__len__()):
                                                filee = open(hash_files[y],"a")
                                                filee.write(f"{plaintext},{hash_list[y](plaintext.encode()).hexdigest()}\n")
                                            break
                                        elif consent.casefold() == "n":
                                            break
                                        else:
                                            raise NameError
                                    except NameError:
                                        print("Enter y or n!")
                except ValueError:
                    print("Please enter a valid input!")
        elif start == 2:
            while True:
                try:
                    hash_function = int(input("What hash alogorithm would you like to use?\n1)md5\n2)sha1\n3)sha224\n4)sha256\n5)sha384\n6)sha512\n7)Exit\n>>>"))
                    if hash_function < 1 or hash_function > 7:
                        raise ValueError
                    else:
                        break
                except ValueError as e:
                    print(e)
                    print("Please enter a valid input!")
            hash_string = input("Input the hash you want to crack (type 'file' if you want to read from a file) >>> ")
            if hash_string == "'file'":
                file_path = input("Input ABSOLUTE PATH of the file you want >>> ")
                try:
                    with open(file_path,"r") as all_of_them:
                        word_list = all_of_them.read().split("\n")
                    for x in word_list:
                        df = pan.read_csv(hash_files[hash_function-1],delimiter=",")
                        results = []
                        for y in range (len(df["hash"])):
                            if df["hash"][y] == x:
                                results.append(df["text"][y])
                        if len(results) == 0:
                            print(f"Sorry your hash {x} is not found in our database!")
                        else:
                            print(f"\nHere are all the words matching the hash {x}!")
                            count = 1
                            for x in results:
                                print(f"{count}) {x}")
                                count += 1
                except FileNotFoundError:
                    print("Your file is not found!")
            else:
                df = pan.read_csv(hash_files[hash_function-1],delimiter=",")
                results = []
                for x in range (len(df["hash"])):
                    if df["hash"][x] == hash_string:
                        results.append(df["text"][x])
                if len(results) == 0:
                    print("Sorry your hash string is not found in our database!")
                else:
                    print("\nHere are all the words matching the hash!")
                    count = 1
                    for x in results:
                        print(f"{count}) {x}")
                        count += 1
    except ValueError:
        print("Please enter a valid input!")

