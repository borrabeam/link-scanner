"""Scan link."""
from selenium import webdriver
import requests
import sys


def get_links(url: str):
    """Find all links on page at the given url.

    Returns:
        a list of all unique hyperlinks on the page,
        without page fragments or query parameters.
    """
    link_list = []
    driver = webdriver.Chrome()
    driver.get(url)
    web_element = driver.find_elements_by_tag_name("a")
    for element in web_element:
        href = element.get_attribute('href')
        if("#" in href):
            link_list.append(href.split("#")[0])
        elif("?" in href):
            link_list.append(href.split("?")[0])
        else:
            link_list.append(href)
    return link_list


def is_valid_url(url: str):
    """Validate url."""
    request = requests.get(url)
    return request.status_code == 200


def invalid_urls(urllist: list) -> list:
    """Validate the urls in urllist and return a new list containing
    the invalid or unreachable urls.
    """
    link_list = []
    for url in urllist:
        if(not is_valid_url(url)):
            link_list.append(url)
    return link_list


def main():
    """Check and return good and bad links."""
    link_input = sys.argv[1]
    all_link = get_links(link_input)
    bad_link = invalid_urls(all_link)
    for link in all_link:
        print(link)
    print("")
    print("Bad Link: ")
    for link in bad_link:
        print(link)


if __name__ == "__main__":
    main()
