import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

from src.analysis_engine.min_max_avg_percent_increase_decrease import get_max_value, get_min_value, get_average, \
    highest_percent_decrease, highest_percent_increase, standard_deviation, calculate_iqr, find_outliers_iqr, \
    calculate_median, calculate_covariance, calculate_correlation
from src.utils.constants import campaign_data, dataframe_columns, intervals
from src.utils.helpers.input_helpers import get_log

logging = get_log()


def build_question(operation, column):
    """
    building question from the operation and column name
    @param operation
    @param column
    @return question
    """
    platform, metric = column.split("_")

    questions = []

    questions.append(f"What is the {operation} count of {platform} {metric}?")
    questions.append(f"Kindly provide the {operation} count of {platform} {metric}.")
    questions.append(f"Could you share the {operation} statistics for {platform} {metric}?")
    questions.append(f"I'd like to know the {operation} count of {platform} {metric}, please.")
    questions.append(f"Can you identify the {operation} count of {platform} {metric}?")
    return questions


def preprocess_question(questions):
    """
    generating combination of tokens to form potential column name in sequence
    @param questions
    @return candidates
    """
    stop_words = set(nltk.corpus.stopwords.words('english'))
    candidates_list = []

    for question in questions:
        tokens = word_tokenize(question.lower())
        tokens = [token for token in tokens if token not in stop_words]

        candidates = []
        for i in range(1, len(tokens) + 1):
            for j in range(len(tokens) - i + 1):
                candidate = "_".join(tokens[j:j + i])
                candidates.append(candidate)

        candidates_list.append(candidates)

    logging.info("Calculated the combination of column names for each question")
    return candidates_list


def column_name(question):
    """
    Checking if there is any match for the column name from the candidates.
    @param question
    @return matching_columns
    """
    dataframe_columns_lower = [column.lower() for column in dataframe_columns]

    candidates_list = preprocess_question([question])

    matching_columns_list = []

    for candidates in candidates_list:
        matching_columns = [dataframe_columns[dataframe_columns_lower.index(candidate)] for candidate in candidates if
                            candidate in dataframe_columns_lower]
        matching_columns_list.extend(matching_columns)  # Extend the list instead of appending

    logging.info("Task : Finding the column")

    return matching_columns_list[0] if matching_columns_list else None


def generate_response(question, result, operation, platform, metric):
    """
    generating response through all the parameters.
    @param question
    @param result
    @param operation
    @param platform
    @param metric
    @return question and answer
    """

    keyword_responses = {
        "kindly": f"Certainly, {result} is the {operation} count for {platform} {metric}.",
        "statistics": f"Indeed, the {operation} statistics for {platform} {metric} is {result}.",
        "please": f"Of Course, the {operation} count for {platform} {metric} that you asked for is {result}.",
        "identify": f"Absolutely, {result} is the count for {platform} {metric} that you are seeking.",
    }

    default_response = f"Sure, the {operation} value for {platform} {metric} is {result}."

    for keyword, response in keyword_responses.items():
        if keyword in question.lower():
            return question, response

    return question, default_response


def handle_result(result):
    """
    handling result format when it is in dictionary or list
    @param result
    @return result
    """
    if isinstance(result, dict):
        return ', '.join([f"'{key}': {value}" for key, value in result.items()])
    elif isinstance(result, list):
        return ', '.join([str(item) for item in result])
    else:
        return str(result)


operations_mapping = {
    "highest": get_max_value,
    "greatest": get_max_value,
    "peak": get_max_value,
    "lowest": get_min_value,
    "least": get_min_value,
    "average": get_average,
    "percent increase": highest_percent_increase,
    "percent decrease": highest_percent_decrease,
    "standard deviation": standard_deviation,
    "IQR": calculate_iqr,
    "Outliers": find_outliers_iqr,
    "median": calculate_median,
    "covariance": calculate_covariance,
    "correlation": calculate_correlation
}


def select_function_based_on_keyword(question, operation, column_name):
    """
    Selecting the function to be called on the basis of the function.
    @param question
    @param operation
    @param column_name
    @return question , answer
    """
    try:
        logging.info("Task: Select function based on operation and generate response")

        dataframe = pd.read_csv(campaign_data)
        df = pd.DataFrame(dataframe)
        platform, metric = column_name.split("_")

        if operation in operations_mapping:
            for interval in intervals:
                result = operations_mapping[operation](df,column_name,interval)
                result_formatted = handle_result(result)
                response = generate_response(question, result_formatted, operation, platform, metric)
                return response
        else:
            return "Sorry, the input operation is not correct."

    except Exception as e:
        logging.error(f"Some error occurred in generating response, Error: {e}")
