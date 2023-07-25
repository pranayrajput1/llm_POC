from src.utils.helpers.entries_fetcher import get_entries
from src.utils.helpers.input_helpers import get_user_query, get_keywords
from src.utils.helpers.log_setup import get_log
from src.utils.helpers.select_function import extract_operation, select_function_based_on_keyword

# getting log setup
logging = get_log()


class AnalysisEngine:

    @staticmethod
    def analysis_pipeline():
        user_query = get_user_query()
        extracted_keywords = get_keywords(user_query)
        response = get_entries(extracted_keywords)
        operation = extract_operation(user_query)
        function = select_function_based_on_keyword(response,operation)
        return function


if __name__ == "__main__":
    analysis_instance = AnalysisEngine()
    result = analysis_instance.analysis_pipeline()
    print(result)