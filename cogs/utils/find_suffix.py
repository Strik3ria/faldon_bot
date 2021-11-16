from cogs.utils.suffixes import suffixes


def find_suffix(suffix_name):
    suffix_name = (
        suffix_name.replace("Of ", "")
        .replace("The ", "")
        .replace("the ", "")
        .lower()
    )
    for suffix in suffixes.keys():
        if suffix_name in suffix:
            return suffix

    return "Not found"
