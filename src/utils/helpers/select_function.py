def extract_operation(question):
        keywords = question.lower().split()
        if "highest" in keywords:
            return "highest"
        elif "lowest" in keywords:
            return "lowest"
        elif "increase percentage" in keywords:
            return "increase percentage"
        else:
            return None


def select_function_based_on_keyword(keywords_dictionary,operation):

    if operation == "highest":
        return max_clicks()
    elif operation == "lowest":
        return min_clicks()
    elif operation == "percentage_increase":
        return percentage_increase_clicks()
    else:
        return "Sorry, the specified operation is not supported."

