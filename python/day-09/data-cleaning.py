
raw_names = [
    "  Asha ",
    "RAM",
    "",
    "Mina",
    "  asha",
    "Ram ",
    "Sita",
    "   "
]

# Strip whitespace and ignore blank entries
clean_names = [
    name.strip().title()
    for name in raw_names
    if name.strip()
]

# Keep unique cleaned names while preserving their first occurrence
unique_names = list(dict.fromkeys(clean_names))

# Build a count of each cleaned name
name_counts = {
    name: clean_names.count(name)
    for name in set(clean_names)
}

print("Cleaned names:", clean_names)
print("Unique names:", unique_names)
print("Name counts:", name_counts)
