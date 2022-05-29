# Problem 3 - Problem Solution

# The difficulty of this problem is partly dependent on the level of detail one wants to go into when checking for
# the common elements between fake accounts. Opening the "users.csv" file we see the following data:

#   username  |   region      |   email                   |   phone number    |   account label
# ------------+---------------+---------------------------+-------------------+------------------
#   mistefa   |   Malta       |   mi23@gmail.com          |   3569870000000   |   real
#   fausta    |   Lithuania   |   fausta@outlook.com      |   3705840000000   |   real
#   dipti     |   Spain       |   dipti2000@hotmail.com   |   347682000000    |   real
#   nikandros |   Spain       |   nik.56@yahoo.com        |   342795000000    |   real
#   merle     |   Greece      |   mrlonb@icloud.com       |   306912000000    |   real
#   amador    |   Greece      |   amadorsmith@email.com   |   618527000000    |   fake
#   pandora   |   Albania     |   None                    |   3555741289688   |   real
#   lucette   |   Sweden      |   tte45@none.ocm          |   865249000000    |   fake
#   levent    |   Albania     |   vent3@name.uu           |   3555790000000   |   fake
#   ziyad     |   Monaco      |   ziziad@gmail.com        |   3775250000000   |   real
#   eldon     |   Monaco      |   paulpaul@hotmail.com    |   865249000000    |   fake
#   xena      |   Norway      |   xenamail@hotmail.kjn    |   None            |   fake
#   paul      |   Hungary     |   name@random.coem        |   367458000000    |   fake

# After cross-referencing with "Phone numbers.csv" we observe the following:
#   1) Fake accounts may have an invalid regional prefix in their phone number;
#   2) Fake accounts may have an invalid domain suffix in their email;
#   3) Missing data does not seem to affect the account label.

# It's clear that the solution requires two parts:
#   a) a routine which checks whether the account's phone number (if one is provided) starts with the correct
#      regional prefix;
#   b) a routine which checks whether the account's email (if one is provided) ends with a valid domain suffix.

# Regarding (a), one can simply load the data from the "Phone numbers.csv" file using e.g. pandas, and then perform
# the necessary checks. Regarding (b), one can probably simply check whether the email ends with a .com suffix.
# However, to be extra safe we also found each country's domain suffix (the data can be found in the "domains.json"
# file, located in the "Solution/data" directory), and wrote a function which checks whether the email ends with
# .com or with the corresponding country domain suffix.

# --------------------------------------------------------------------------------------------------------------------

import sys
import pandas as pd


def get_data(path):
    # Input: the path to the user data that is to be checked.
    # Output: the user data in a pandas dataframe, and the regional phone number prefices
    # along with the the regional domain suffices in a second pandas dataframe.
    users_data = pd.read_csv(path)
    users_data.fillna(value=0, inplace=True)
    phone_codes = pd.read_csv("./data/Phone numbers.csv")
    domains = pd.read_json("./data/domains.json")
    joined_data = pd.merge(phone_codes, domains, how="left")

    return users_data, joined_data


def phone_check(users_data, joined_data, i, region):
    # Check whether a phone number has the correct regional prefix.
    raw_phone = users_data["phone number"].iloc[i]
    if raw_phone != 0:
        phone_number = str(int(raw_phone))
        user_prefix = phone_number[:-10]
        prefix = str(
            list(joined_data.loc[joined_data["Country"] == region, "Prefix"])[0]
        )

        return user_prefix == prefix

    return True


def domain_check(users_data, joined_data, i, region):
    # Check whether an email address ends with .com or with the correct regional prefix.
    raw_domain = users_data["email"].iloc[i]
    if raw_domain != 0:
        ind = raw_domain.rfind(".")
        user_domain = raw_domain[ind:]
        domain = str(list(joined_data.loc[joined_data["Country"] == region, "tlds"])[0])

        return user_domain == domain or user_domain == ".com"

    return True


def check(users_data, joined_data):
    # Return a list of the fake accounts based on the phone number and email checks.
    fake_accounts = []
    for i in range(len(users_data)):
        region = users_data["region"].iloc[i]
        user = users_data["username"].iloc[i]
        check_1 = phone_check(users_data, joined_data, i, region)
        check_2 = domain_check(users_data, joined_data, i, region)
        if not check_1 or not check_2:
            fake_accounts.append(user)

    return fake_accounts


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python day3.py path/to/data.csv")
    path = sys.argv[1]
    users_data, joined_data = get_data(path)
    fake_accounts = check(users_data, joined_data)
    print()
    print("Fake accounts:")
    print("\n".join(fake_accounts))
    print()


if __name__ == "__main__":
    main()
