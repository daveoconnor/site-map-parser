import argparse


def uri_modifier(url):
    if not url.startswith('https://') and not url.startswith('http://'):
        url = 'http://'+url

    if not url.endswith('.xml'):
        if not url.endswith('/'):
            url = url + '/'
        url = url + 'sitemap.xml'
    return url


def get_args():
    """
    :return: (url, log)
    """
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "url",
        help="Url & path to sitemap.xml"
    )
    arg_parser.add_argument(
        "--log",
        "-l",
        choices=[
            "CRITICAL",
            "ERROR",
            "WARNING",
            "INFO",
            "DEBUG",
        ]
    )

    found_args = arg_parser.parse_args()
    return (
        found_args.url,
        found_args.log
    )
