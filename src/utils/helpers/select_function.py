import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

from src.analysis_engine.min_max_avg import get_max_value, get_min_value, get_average
from src.utils.constants import campaign_data
import logging


def get_log():
    """
    Initializing logger basic configuration
    """
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    return logging


def append_to_dataframe(question, answer):
    """
    appending the question and answer in a dataframe.
    :param question:
    :param answer:
    """
    global df
    df = df.append({"Question": question, "Answer": answer}, ignore_index=True)
    return df


def preprocess_question(question):
    """
    generating combination of tokens to form potential column name in sequence
    :param question
    :return candidates
    """
    tokens = word_tokenize(question.lower())

    stop_words = set(nltk.corpus.stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    candidates = []
    for i in range(1, len(tokens) + 1):
        for j in range(len(tokens) - i + 1):
            candidate = "_".join(tokens[j:j + i])
            candidates.append(candidate)

    logging.info("Calculated the combination of column name")
    return candidates


def column_name(question):
    """
    Checking if there is any match for the column name from the candidates.
    :param question
    :return matching_columns
    """
    dataframe_columns = ["Facebook_Clicks", "Facebook_Views", "Facebook_bought", "Youtube_Views",
                         "Youtube_Clicks", "Youtube_Followers", "Youtube_bought", "Youtube_Subscription",
                         "Instagram_Views", "Instagram_Clicks", "Instagram_Followers"]

    dataframe_columns_lower = [column_name.lower() for column_name in dataframe_columns]

    candidates = preprocess_question(question)

    matching_columns = [dataframe_columns[dataframe_columns_lower.index(candidate)] for candidate in candidates if
                        candidate in dataframe_columns_lower]

    logging.info("Task : Finding the column")
    return matching_columns if matching_columns else None


def extract_operation(question):
    """
    Finding out the operation to be done from the question
    :param question
    :return operation
    """

    keywords = question.lower().split()
    if "highest" in keywords:
        logging.info("Operation found highest")
        return "highest"
    elif "lowest" in keywords:
        logging.info("Operation found lowest")
        return "lowest"
    elif "increase percentage" in keywords:
        logging.info("Operation found increase percentage")
        return "increase percentage"
    elif "average" in keywords:
        logging.info("Operation found average")
        return "average"
    else:
        return None


def select_function_based_on_keyword(question, operation, platform1, platform2=None):
    """
    Selecting the function to be called on the basis of the function.
    :param question
    :param operation
    :param platform1
    :param platform2
    :return answer
    """
    dataframe = pd.read_csv(campaign_data)
    df = pd.DataFrame(dataframe)
    if platform2 is None:
        if operation == "highest":
            result = get_max_value(df, platform1)
            data = [question, f"The highest value for {platform1} is {result}"]
            return data

        elif operation == "lowest":
            result = get_min_value(df, platform1)
            data = [question,f"The lowest value for {platform1} is {result}"]
            return data

        elif operation == "average":
            result = get_average(df, platform1)
            data = [question, f"The average value of {platform1} is {result}"]
            return data
        else:
            return "Sorry, the input is not correct."


    else:
        if operation == "highest":
            result1 = get_max_value(df, platform1)
            result2 = get_max_value(df, platform2)
            data = [question,f"The highest value for {platform1} is {result1}, and for {platform2} is {result2}"]
            return data

        elif operation == "lowest":
            result1 = get_min_value(df, platform1)
            result2 = get_min_value(df, platform2)
            data = [question,f"The lowest value for {platform1} is {result1}, and for {platform2} is {result2}"]
            return data

        elif operation == "average":
            result1 = get_average(df, platform1)
            result2 = get_average(df, platform2)
            data = [question,f"The average value of {platform1} is {result1}, and for {platform2} is {result2}"]
            return data
        else:
            return "Sorry, the input is not correct."
