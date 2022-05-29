# Day 3 - Problem Description

## Difficulty: Easy/Medium

You are given a .csv file containing data from various user accounts of a website. In particular, for each user you get the username, the region from which they signed up, as well as the email and phone number they provided. The task is to write an algorithm that prints out the usernames of the fake accounts.

In order to help you determine the common elements of fake accounts, the _users.csv_ file (which can be found in the _Solution/data_ directory) contains various account examples, each of which is labeled either as "real" or "fake" in a column called "account label". Naturally, your algorithm should work on any similar set of data which does not include this column.

A few notes:

- All usernames in the .csv file can be assumed to be randomly generated and unique;
- All phone numbers can be assumed to consist of the regional prefix followed by 10 digits;
- All accounts can be assumed to be located in Europe. A list of valid regions in Europe, along with their corresponding regional prefix, can be found in the _Phone numbers.csv_ file (which is located in _Solution/data_ as well).
- While some data might be missing for some accounts, you may assume that each account entry will contain at least one of the user's email or the user's phone number.
