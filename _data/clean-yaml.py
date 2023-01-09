"""Run this `python clean-yaml.py` in the same directory as this script."""
import yaml

with open("./members.yml", "r") as stream:
    members = yaml.safe_load(stream)

members_sorted = {}

for key in ["group_members", "guest_members"]:
    members_sorted[key] = [
        {"name": member["name"], "website": member["website"], "image": member["image"]}
        for member in members[key]
    ]

members_sorted["alumni"] = [
    {"name": member["name"], "website": member["website"], "bio": member["bio"]}
    for member in members["alumni"]
]

for key in members_sorted.keys():
    members_sorted[key] = sorted(members_sorted[key], key=lambda d: d['name'])

with open("./members.yml", "w") as stream:
    yaml.safe_dump(
        members_sorted, stream, allow_unicode=True, indent=4, sort_keys=False
    )


with open("./projects.yml", "r") as stream:
    projects = yaml.safe_load(stream)

projects_sorted = {}

for key in ["current_projects", "previous_projects"]:
    projects_sorted[key] = [
        {"name": member["name"], "website": member["website"], "image": member["image"]}
        for member in projects[key]
    ]

for key in projects_sorted.keys():
    projects_sorted[key] = sorted(projects_sorted[key], key=lambda d: d['name'])

with open("./projects.yml", "w") as stream:
    yaml.safe_dump(
        projects_sorted, stream, allow_unicode=True, indent=4, sort_keys=False
    )
