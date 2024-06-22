import json
import requests
import toml


def search_openalex(query: str):
    """
    search_openalex

    Args:
        query: User-provided string that serves as the search term that open alex api uses to return a set of works
        base_url: The base_url of the works api of open alex

    Returns:
        response: a json object of search results from the open alex api
    """

    base_url = "https://api.openalex.org/autocomplete/works?filter=is_oa:true&search="
    url = f"{base_url}{query}"

    response = requests.get(url).json()

    return response


def ask_user_for_search_string():
    """
    ask_user_for_search_string

    Args:
        None
    Returns:
        query: a string object that represents the user's search query
    """

    query = input("Input what you would like to search for:\n")

    return query


def read_config(file_path):
    config = toml.loads(file_path)
    return config


def main():
    print(read_config("config.toml"))


main()
