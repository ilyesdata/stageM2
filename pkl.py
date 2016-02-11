import pickle  # Importing module, you need to do it only once
a = [1,2,3]  # Creating two lists
b = [3,4,5]
file = open("H:/output.txt", 'wb')
pickle.dump(a, file)  # Saving lists to file
pickle.dump(b, file)

# Importing module, you need to do it only once
file = open("H:/M2 recherche/Stage/lyesdata.pkl", 'rb')
a = pickle.load(file) # Read first record into a
b = pickle.load(file) # Read second record into b
print(a)
print(b)
# And so on until the end of the file