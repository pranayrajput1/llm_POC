from src.analysis_functions.max_values import get_individual_max_values


def extract_operation(question):
        keywords = question.lower().split()
        if "highest" in keywords:
            return "highest"
        elif "lowest" in keywords:
            return "lowest"
        elif "increase percentage" in keywords:
            return "increase percentage"
        elif "average" in keywords:
            return "average"
        elif "lowest average" in keywords:
            return "lowest average"
        else:
            return None


def select_function_based_on_keyword(keywords_dictionary,operation):
    key = list(keywords_dictionary.keys())[0]
    parts = key.split('_')
    User = parts[0]
    platform = '_'.join(parts[1:])
    if operation == "highest":
        result = get_individual_max_values(keywords_dictionary)
        if result and len(result) > 0:
            number = result[0][0]
            return f"The highest {platform} of {User} are {number}"
        return "No data available"

    elif operation == "lowest":
        result = min_clicks()
        return f"The lowest "
    elif operation == "percentage_increase":
        return percentage_increase_clicks()
    else:
        return "Sorry, the specified operation is not supported."

