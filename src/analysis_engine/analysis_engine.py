from src.utils.helpers.entries_fetcher import get_entries
from src.utils.helpers.input_helpers import get_user_query, get_keywords
from src.utils.helpers.log_setup import get_log

# getting log setup
logging = get_log()


class AnalysisEngine:

    @staticmethod
    def analysis_pipeline():
        user_query = get_user_query()
        extracted_keywords = get_keywords(user_query)
        response = get_entries(extracted_keywords)
        return response


if __name__ == "__main__":
    analysis_instance = AnalysisEngine()
    result = analysis_instance.analysis_pipeline()
    print(result.items())
