import csv

# Opens the Address File csv file and enters them into the addressList list with a for loop.
# Time Complexity: O(n)
# Space Complexity: O(n)
with open("Addresses File.csv") as addressesFile:
    reader = csv.reader(addressesFile, delimiter=",", quotechar='"')
    addressList = list(reader)

# Returns a unique number value for each address in the addressList list that corresponds to each address.
# For example, searching address_lookup("4001 South 700 East") returns 0 because it is the hub.
# Time Complexity: O(n)
# Space Complexity: O(n)
def address_lookup(searchAddress):
    """
    address_lookup:
    address_lookup takes an address and returns a unique numeric value.

    Args:
    searchAddress: this represents the address that will be passed into the function

    Returns:
    unique_address_value: this represents the unique value that is returned after the address is enumerated.

    Raises:
    Raises no exceptions.

    Time Complexity: time_adjuster uses one assignment operator, but iterates over the values in the addressList list. Its time complexity is O(n).

    Space Complexity: O(n).
    """
    unique_address_value = next((i for i, value in enumerate(addressList) if searchAddress in value), None)
    return(unique_address_value)

