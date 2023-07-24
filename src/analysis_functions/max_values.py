def get_individual_max_values(data_entries):
    keys_list = list(data_entries.keys())

    max_values = []
    for item in keys_list:
        print(item)
        max_values.append(max(data_entries[item]))
    return max_values


def get_max_between_multiple(data_entries):
    items = data_entries.values
    max_value = items.max()
    return max_value
