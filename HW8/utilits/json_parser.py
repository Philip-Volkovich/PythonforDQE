import json
import os
from feed_class.news_feed_parent import NewsFeed
from feed_class.news import News
from feed_class.private_ad import PrivateAd
from feed_class.currency_conv import CurrencyConversion
from utilits.text_functions import convert_to_normalized_case
from utilits.db_connection import DBConnection


class JsonParser:
    def __init__(self, file_name):
        """Initialize a JsonParser instance.

        Args:
        file_name (str): The name of the JSON file to parse."""
        self.file_name = file_name
        self.full_path = None
        self.source_dict = None
        self.path = None

    def load_from_json(self, path):
        """Load JSON content from a file.

        Args:
        path (str): The path to the JSON file."""
        self.path = path
        self.full_path = os.path.join(self.path, self.file_name)
        self.source_dict = json.load(open(f'{self.full_path}', 'r'))

    def parse_from_json(self):
        """Parse and process JSON content."""
        for key, value in self.source_dict.items():
            if key == 'operations':
                for record_dict in self.source_dict['operations']:
                    if record_dict['operation_type'] == 'news':
                        news_feed = NewsFeed('news')
                        news_feed.record = News(convert_to_normalized_case(record_dict.get('input_text')),
                                                convert_to_normalized_case(record_dict.get('city')))
                        news_feed.add_publication()
                        db_record = DBConnection('new_db')
                        db_record.db_create('news',db_record.columns_news)
                        db_record.db_insert('news',"input_text, city, date",
                                            f"""'{news_feed.record.input_text}',
                                            '{news_feed.record.city}',
                                            '{news_feed.record.date}'""")
                    elif record_dict['operation_type'] == 'private advertisement':
                        news_feed = NewsFeed('private advertisement')
                        news_feed.record = PrivateAd(convert_to_normalized_case(record_dict.get('input_text')),
                                                     record_dict.get('expir_date'))
                        news_feed.add_publication()
                        db_record = DBConnection('new_db')
                        db_record.db_create('private_ad', db_record.columns_private_ad)
                        db_record.db_insert('private_ad', "input_text, expir_date, days_left",
                                            f"""'{news_feed.record.input_text}',
                                            '{news_feed.record.expir_date}',
                                            '{news_feed.record.days_left}'""")
                    elif record_dict['operation_type'] == 'currency_conversion':
                        news_feed = NewsFeed('currency_conversion')
                        news_feed.record = CurrencyConversion(convert_to_normalized_case(record_dict.get('from_currency')),
                                                              convert_to_normalized_case(record_dict.get('to_currency')),
                                                              record_dict.get('exchange_rate'),
                                                              convert_to_normalized_case(record_dict.get('city')))
                        news_feed.add_publication()
                        db_record = DBConnection('new_db')
                        db_record.db_create('currency_conv', db_record.columns_currency_conv)
                        db_record.db_insert('currency_conv', "currency_from, currency_to, rate, city, date",
                                            f"""'{news_feed.record.currency_from}',
                                             '{news_feed.record.currency_to}',
                                             '{news_feed.record.rate}',
                                             '{news_feed.record.city}',
                                             '{news_feed.record.date}'""")
                    else:
                        print(f'Invalid record: {record_dict}. Please check the file.')

                    try:
                        os.remove(self.full_path)
                    except FileNotFoundError:
                        pass
            else:
                print(f'Invalid record structure of the file. Please check the file.')
