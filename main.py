import json

with open("following.json") as f:
    f_data = f.read()
following = json.loads(f_data)

following_list = []
relationships_following = following["relationships_following"]
for i in relationships_following:
    string_list_following = i["string_list_data"]

    for j in string_list_following:
        href_following = j["href"]
        following_list.append(href_following)

with open("followers.json") as e:
    e_data = e.read()
followers = json.loads(e_data)

followers_list = []
relationships_followers = followers["relationships_followers"]
for i in relationships_followers:
    string_list_followers = i["string_list_data"]

    for j in string_list_followers:
        href_followers = j["href"]
        followers_list.append(href_followers)

not_following_back = set(following_list) - set(followers_list)
for i in not_following_back:
    print(i, "does not follow you back.")

f.close()