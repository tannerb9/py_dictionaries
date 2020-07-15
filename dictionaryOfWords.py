word_definitions = dict()

word_definitions["bellicose"] = "inclined or eager to fight; agressively hostile; belligerent; pugnacious"
word_definitions["bailiwick"] = "a person's area of skill, knowledge, authority, or work"
word_definitions["vox populi"] = "the voice of the people; popular opinion"
word_definitions["repudiate"] = "to reject with disapproval or condemnation"

def_list = []

for word in word_definitions.values():
    def_list.append(word)

print(def_list[:2])

for (key, value) in word_definitions.items():
    print(f"{key}: {value}")
