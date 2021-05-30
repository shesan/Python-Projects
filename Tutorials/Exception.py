# Exception

# Setup
actor = {"name": "John Cleese", "rank": "awesome"}

# Function to modify!!!


def get_last_name():
    last = ""
    try:
        last = actor["name"].split()
        return last[1]
    except:
        print("nope")

    return actor["name"].split()[1]


# Test code
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())
