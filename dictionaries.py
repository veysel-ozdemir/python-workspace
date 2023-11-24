band = {
    "vocals": "Plant",
    "guitar": "Page",
}
band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# --------------- access items ---------------

print(band["vocals"])
print(band.get("guitar"))

print(band.keys())  # list all keys
print(band.values())  # list all values
print(band.items())  # list of key/value pairs as tuples
# verify a key exists
print("guitar" in band)
print("triangle" in band)

# --------------- operation on values or items ---------------
# change values
band["vocals"] = "Converdale"
band.update(
    {
        "bass": "JPJ",
    }
)
print(band)

# remove items
print(band.pop("bass"))  # returns the value of the specified key, and removes it
print(band)

band["drums"] = "Bonham"
print(band)
print(band.popitem())  # returns the last item as tuple, and removes it
print(band)

# delete and clear

band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# --------------- copy and reference ---------------

# band2 = band  # creates a reference

band2 = band.copy()
band2["drums"] = "Dave"
print(band)
print(band2)

band3 = dict(band)
print(band3)

# --------------- nested dictionaries ---------------

member1 = {
    "name": "Plant",
    "instrument": "vocals",
}

member2 = {
    "name": "Page",
    "instrument": "guitar",
}

band = {
    "member1": member1,
    "member2": member2,
}

print(band)
print(band["member1"]["name"])
