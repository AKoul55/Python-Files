myDict = {
    "fast": "he bowls quick",
    "hit": "he is a hardhitter",
    "marks":[4.5,8,5],
    "cricket":{'hit':'man'},
    1:2
}

print(list(myDict.keys())) #print the keys of the dict
print(list(myDict.values())) #print the values of the dict
print(myDict.items()) #print the (key, values foa ll contents of the dict)
updateDict ={
    "Ak": "koul",
    "India": "WC",

}
myDict.update(updateDict) #updates the dict by adding key and values
print(myDict)

print(myDict.get("hit")) # returns none as hit2 is not present/prints values associated with key
print(myDict)["hit2"] # throws an error as hit 2 not present