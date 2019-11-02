import logging
import requests
from io import BytesIO
from lxml import etree

logger = logging.getLogger(__name__)
# use Bytes throughout because that's how lxml says XML should be used


def download_uri_data(uri):
    """
    returns file object
    """
    logger.info('download_uri_data requesting: %s' % uri)
    # using requests to follow any redirects that happen
    headers = {'Content-Type': 'application/xml;charset=utf-8'}
    r = requests.get(uri, headers=headers)
    # ensure it's the decompressed content
    r.raw.decode_content = True
    logger.debug("r.content: {}, type: {}".format(
        r.content,
        type(r.content)
    ))
    return r.content


def data_to_element(data):
    """
    data parameter should be bytes
    """
    logger.debug('dataToElement retrieved: %s ' % data)
    content = BytesIO(data)
    logger.debug('dataToElement BytesIO: %s ' % content)

    root = None
    try:
        utf8_parser = etree.XMLParser(encoding='utf-8')
        downloaded_xml = etree.parse(content, parser=utf8_parser)
        logger.debug("downloaded_xml {}".format(downloaded_xml))
        root = downloaded_xml.getroot()
        logger.debug("download root {}".format(root))
    except SyntaxError as err:
        logger.warning("Parsing failed {}".format(err))
        raise SyntaxError from err
    return root
