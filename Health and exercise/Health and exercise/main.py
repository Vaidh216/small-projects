# client1 = open("ved.txt","a")
# client2 = open("Vikash.txt" , "a")
# client3 = open("Animesh.txt" , "a")

def getdate():
    import datetime
    return datetime.datetime.now()

print("Welcome to the health and exercise routine check program : ")

#Writing the data to the file
print("Do you want to write the data")
val = input("Enter your choice :(Yes/No) ")
#Checking to read or write
if val.lower() == "yes":

    # Data entry Client 1 Ved

    print("Do want want to enter the data of client1 ved")
    val = input("Enter you choice :(Yes/No)")
    #Checking if want which client

    if val.lower() == "yes":

        client1_diet = open("ved_diet.txt" , "a")
        client1_exer = open("ved_exe.txt" , "a")

        val = input("Do you want to enter diet data (Yes/No): ")
        if val.lower() == "yes":
            client1_diet.write(str(getdate()))
            while (True):
                val = input('Enter data :(No for ending) ')
                if(val.lower() == "no"):
                    break
                client1_diet.write(val)
                client1_diet.write("\n")

            client1_diet.write("\n\n")

        val = input("Do you want to enter exercise data (Yes/No): ")
        if val.lower() == "yes":
            client1_exer.write(str(getdate()))
            while (True):
                val = input('Enter data :(No for ending) ')
                if (val.lower() == "no"):
                    break
                client1_exer.write(val)
                client1_exer.write("\n")

            client1_exer.write("\n\n")

        print("Entry of data of client 1 ved ends :")
        client1_diet.close()
        client1_exer.close()

    # Data enrty Client 2 Vikash

    print("Do want want to enter the data of client2 vikash")
    val = input("Enter you choice :(Yes/No)")
    # Checking if want which client

    if val.lower() == "yes":

        client2_diet = open("vikash_diet.txt", "a")
        client2_exer = open("vikash_exe.txt", "a")

        val = input("Do you want to enter diet data (Yes/No): ")

        if val.lower() == "yes":
            client2_diet.write(str(getdate()))
            while (True):
                val = input('Enter data :(No for ending) ')
                if (val.lower() == "no"):
                    break
                client2_diet.write(val)
                client2_diet.write("\n")

            client2_diet.write("\n\n")

        val = input("Do you want to enter exercise data (Yes/No): ")
        if val.lower() == "yes":
            client2_exer.write(str(getdate()))
            while (True):
                val = input('Enter data :(No for ending) ')
                if (val.lower() == "no"):
                    break
                client2_exer.write(val)
                client2_exer.write("\n")
            client2_exer.write("\n\n")

        print("Entry of data of client 2 Vikash ends :")
        client2_diet.close()
        client2_exer.close()

    #Data entry for client Animesh

    print("Do want want to enter the data of client3 Animesh ")
    val = input("Enter you choice :(Yes/No)")
    # Checking if want which client
    if val.lower() == "yes":
        client3_diet = open("animesh_diet.txt", "a")
        client3_exer = open("animesh_exe.txt", "a")

        val = input("Do you want to enter diet data (Yes/No): ")
        if val.lower() == "yes":
            client3_diet.write(str(getdate()))
            while (True):
                val = input('Enter data :(No for ending) ')
                if (val.lower() == "no"):
                    break
                client3_diet.write(val)
                client3_diet.write("\n")
            client3_diet.write("\n\n")

        val = input("Do you want to enter exercise data (Yes/No): ")
        if val.lower() == "yes":
            client3_exer.write(str(getdate()))
            while (True):
                val = input('Enter data :(No for ending) ')
                if (val.lower() == "no"):
                    break
                client3_exer.write(val)
                client3_exer.write("\n")
            client3_exer.write("\n\n")

        print("Entry of data of client 3 Animesh ends :")
        client3_diet.close()
        client3_exer.close()

    print("Input operation completed")

# Now here are the function for the output operation

print("Do you want to read the data")
val = input("Enter your choice :(Yes/No) ")

if val.lower() == "yes":
    # Data reading Client 1 Ved

    print("Do want want to read the data of client1 ved")
    val = input("Enter you choice :(Yes/No)")
    #Checking if want which client

    if val.lower() == "yes":

        client1_diet = open("ved_diet.txt" , "r")
        client1_exer = open("ved_exe.txt" , "r")

        val = input("Do you want to read diet data (Yes/No): ")
        if val.lower() == "yes":
            print(client1_diet.read())

        val = input("Do you want to read exercise data (Yes/No): ")
        if val.lower() == "yes":
            print(client1_exer.read())

        print("Reading of data of client 1 ved ends :")
        client1_diet.close()
        client1_exer.close()

    # Data read for Client 2 Vikash

    print("Do want want to read the data of client2 vikash")
    val = input("Enter you choice :(Yes/No)")
    # Checking if want which client

    if val.lower() == "yes":

        client2_diet = open("vikash_diet.txt", "r")
        client2_exer = open("vikash_exe.txt", "r")

        val = input("Do you want to read diet data (Yes/No): ")

        if val.lower() == "yes":
            print(client2_diet.read())

        val = input("Do you want to read exercise data (Yes/No): ")
        if val.lower() == "yes":
            print(client2_exer.read())

        print("Reading of data of client 2 Vikash ends :")
        client2_diet.close()
        client2_exer.close()

    #Data reads for client3 Animesh

    print("Do want want to read the data of client 3 Animesh ")
    val = input("Enter you choice :(Yes/No)")
    # Checking if want which client
    if val.lower() == "yes":
        client3_diet = open("animesh_diet.txt", "r")
        client3_exer = open("animesh_exe.txt", "r")

        val = input("Do you want to read diet data (Yes/No): ")
        if val.lower() == "yes":
            print(client3_diet.read())

        val = input("Do you want to read exercise data (Yes/No): ")
        if val.lower() == "yes":
            print(client3_exer.read())

        print("Read of data of client 3 Animesh ends :")
        client3_diet.close()
        client3_exer.close()

    print("reading operation completed")

    print("The program ends For more uodates wait")
