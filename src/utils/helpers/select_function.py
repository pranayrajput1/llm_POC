import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

from src.analysis_engine.min_max_avg import get_max_value, get_min_value, get_average
from src.utils.constants import campaign_data
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
    questions.append(f"Tell me the {operation} count of {platform} {metric}.")
    questions.append(f"What are the {operation} statistics for {platform} {metric}?")
    questions.append(f"Give me the {operation} count of {platform} {metric}.")
    questions.append(f"Identify the {operation} count of {platform} {metric}?")
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
    dataframe_columns = ["Facebook_Clicks", "Facebook_Views", "Facebook_bought", "Youtube_Views",
                         "Youtube_Clicks", "Youtube_Followers", "Youtube_bought", "Youtube_Subscription",
                         "Instagram_Views", "Instagram_Clicks", "Instagram_Followers"]
    dataframe_columns_lower = [column.lower() for column in dataframe_columns]

    candidates_list = preprocess_question([question])

    matching_columns_list = []

    for candidates in candidates_list:
        matching_columns = [dataframe_columns[dataframe_columns_lower.index(candidate)] for candidate in candidates if
                            candidate in dataframe_columns_lower]
        matching_columns_list.extend(matching_columns)  # Extend the list instead of appending

    logging.info("Task : Finding the column")

    return matching_columns_list[0] if matching_columns_list else None


def select_function_based_on_keyword(question, operation, column_name):
    """
    Selecting the function to be called on the basis of the function.
    @param question
    @param operation
    @param column_name
    @return question , answer
    """
    dataframe = pd.read_csv(campaign_data)
    df = pd.DataFrame(dataframe)
    platform, metric = column_name.split("_")

    if operation in ["highest", "greatest", "peak"]:
        result = get_max_value(df, column_name)
        if "tell me" in question.lower():
            return question, f"Certainly, {result} is the {operation} count for {platform} {metric}."
        elif "statistics" in question.lower():
            return question, f"Certainly, the {operation} statistics for {platform} {metric} is {result}."
        elif "give me" in question.lower():
            return question, f"Sure, the {operation} count for {platform} {metric} that you asked for is {result}."
        elif "identify" in question.lower():
            return question, f"Certainly, {result} is the count for {platform} {metric} that you asked for. "
        else:
            return question, f"Sure, the {operation} value for {platform} {metric} is {result}."


    elif operation in ["lowest", "least"]:
        result = get_min_value(df, column_name)
        if "tell me" in question.lower():
            return question, f"Certainly, {result} is the {operation} count for {platform} {metric}."
        elif "statistics" in question.lower():
            return question, f"Certainly, the {operation} statistics for {platform} {metric} is {result}."
        elif "give me" in question.lower():
            return question, f"Sure, the {operation} count for {platform} {metric} that you asked for is {result}."
        elif "identify" in question.lower():
            return question, f"Certainly, {result} is the count for {platform} {metric} that you asked for. "
        else:
            return question, f"Sure, {platform} {metric} {operation} count is {result}"


    elif operation == "average":
        result = get_average(df, column_name)
        if "tell me" in question.lower():
            return question, f"Certainly, {result} is the {operation} count for {platform} {metric}."
        elif "statistics" in question.lower():
            return question, f"Certainly, the {operation} statistics for {platform} {metric} is {result}."
        elif "give me" in question.lower():
            return question, f"Sure, the {operation} count for {platform} {metric} that you asked for is {result}."
        elif "identify" in question.lower():
            return question, f"Certainly, {result} is the count for {platform} {metric} that you asked for. "
        else:
            return question, f"Sure, The average value of {platform} {metric} is {result}"

    else:
        return "Sorry, the input is not correct."
        pass
