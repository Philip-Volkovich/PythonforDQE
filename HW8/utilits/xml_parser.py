import xml.etree.ElementTree as ET
import os
from feed_class.news_feed_parent import NewsFeed
from feed_class.news import News
from feed_class.private_ad import PrivateAd
from feed_class.currency_conv import CurrencyConversion
from utilits.text_functions import convert_to_normalized_case


class XmlParser:
    def __init__(self, file_name):
        """Initialize a XmlParser instance.

        Args:
        file_name (str): The name of the XML file to parse."""
        self.file_name = file_name
        self.full_path = None
        self.source_xml = None
        self.path = None

    def load_from_xml(self, path):
        """Load XML content from a file.

        Args:
        path (str): The path to the XML file."""
        self.path = path
        self.full_path = os.path.join(self.path, self.file_name)
        self.source_xml = ET.parse(f'{self.full_path}')

    def parse_from_xml(self):
        """Parse and process XML content."""

        root = self.source_xml.getroot()
        found_valid_transaction = False
        found_invalid_transaction = False

        if root.tag == 'data':
            for transaction in root.findall('transaction'):
                operation_type = transaction.find('operation_type').text
                if operation_type == 'news':
                    news_feed = NewsFeed('news')
                    news_feed.record = News(convert_to_normalized_case(transaction.find('input_text').text),
                                            convert_to_normalized_case(transaction.find('city').text))
                    news_feed.add_publication()
                    found_valid_transaction = True
                elif operation_type == 'private advertisement':
                    news_feed = NewsFeed('private advertisement')
                    news_feed.record = PrivateAd(convert_to_normalized_case(transaction.find('input_text').text),
                                                 (transaction.find('expir_date').text))
                    news_feed.add_publication()
                    found_valid_transaction = True
                elif operation_type == 'currency_conversion':
                    news_feed = NewsFeed('currency_conversion')
                    news_feed.record = CurrencyConversion(convert_to_normalized_case(transaction.find('from_currency').text),
                                                          convert_to_normalized_case(transaction.find('to_currency').text),
                                                          transaction.find('exchange_rate').text,
                                                          convert_to_normalized_case(transaction.find('city').text))
                    news_feed.add_publication()
                    found_valid_transaction = True
                else:
                    print(f'Invalid record: {operation_type}. Please check the file.')
                    found_invalid_transaction = True

        if not found_valid_transaction or found_invalid_transaction:
            print("Invalid record structure of the file. Please check the file.")
        else:
            try:
                os.remove(self.full_path)
            except FileNotFoundError:
                pass
