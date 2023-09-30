from datetime import datetime
from datetime import date


class NewsFeed:
    def __init__(self, operation_type):
        """Initialize a NewsFeed instance.

        Args:
            operation_type (str): The type of operation (e.g., 'news', 'private advertisement',
            'currency conversion rate').
        """
        self.operation_type = operation_type
        self.record = None

    def add_record(self):
        """Add a record of the specified type to the news feed.

        Returns:
            record: An instance of a specific record type (News, PrivateAd, or CurrencyConversion).
        """
        if self.operation_type == 'news':
            text = input('Enter the news text: ')
            city = input('Enter the news city: ')
            self.record = News(text, city)
            return self.record
        elif self.operation_type == 'private advertisement':
            text = input('Enter the private advertisement text: ')
            expir_date = input('Enter expiration date (YYYY-MM-DD): ')
            self.record = PrivateAd(text, expir_date)
            return self.record
        elif self.operation_type == 'currency conversion rate':
            currency_from = input('Enter FROM which currency you want to convert (3 capital letters, e.g., USD): ')
            currency_to = input('Enter TO which currency you want to convert (3 capital letters, e.g., USD): ')
            rate = float(input('Enter currency exchange rate (integer or decimal): '))
            city = input('Enter city for currency exchange rate: ')
            self.record = CurrencyConversion(currency_from, currency_to, rate, city)
            return self.record

    def add_publication(self):
        """Add the record to a text file and print a success message."""
        with open('news_feed.txt', 'a') as file:
            file.write(self.record.publish())
            file.write('\n\n')
        print(f'Your {self.operation_type} was successfully published ')


class News(NewsFeed):
    def __init__(self, text, city):
        """Initialize a News record.

        Args:
            text (str): The news text.
            city (str): The city associated with the news.
        """
        super().__init__('news')
        self.text = text
        self.city = city
        self.date = datetime.now().strftime('%Y-%m-%d, %H:%M')

    def publish(self):
        """Format and return the news record as a string.

        Returns:
            str: The formatted news record.
        """
        return f''' News------------------
 {self.text} 
 {self.city}. {self.date}
        '''


class PrivateAd(NewsFeed):
    def __init__(self, text, expir_date):
        """Initialize a Private Advertisement record.

        Args:
            text (str): The advertisement text.
            expir_date (str): The expiration date in the format 'YYYY-MM-DD'.
        """
        super().__init__('private advertisement')
        self.text = text
        self.expir_date = datetime.strptime(expir_date, '%Y-%m-%d').date()
        self.days_left = (self.expir_date - date.today()).days

    def publish(self):
        """Format and return the private advertisement record as a string.

        Returns:
            str: The formatted private advertisement record.
        """
        return f''' PrivateAd--------------
 {self.text} 
 Actual until: {self.expir_date}, {self.days_left} days left
        '''


class CurrencyConversion(NewsFeed):
    def __init__(self, currency_from, currency_to, rate, city):
        """Initialize a Currency Conversion Rate record.

        Args:
            currency_from (str): The currency code to convert from (e.g., 'USD').
            currency_to (str): The currency code to convert to (e.g., 'EUR').
            rate (float): The currency exchange rate.
            city (str): The city associated with the exchange rate.
        """
        super().__init__('currency conversion rate')
        self.currency_from = currency_from
        self.currency_to = currency_to
        self.rate = rate
        self.city = city
        self.date = datetime.now().strftime('%Y-%m-%d, %H:%M')

    def publish(self):
        """Format and return the currency conversion rate record as a string.

        Returns:
            str: The formatted currency conversion rate record.
        """
        return f''' CurrencyConversion--------------
 Todays rate: 1 {self.currency_from} = {self.rate} {self.currency_to}
 {self.city}, {self.date}
        '''


class AppRunner:
    def console_runner(self):
        """Run the console-based news feed application."""
        while True:
            print("\nSelect type of record to add:")
            print("1. News")
            print("2. Private Advertisement")
            print("3. Currency Rate")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                news_feed = NewsFeed('news')
                news_feed.add_record()
                news_feed.add_publication()
            elif choice == '2':
                news_feed = NewsFeed('private advertisement')
                news_feed.add_record()
                news_feed.add_publication()
            elif choice == '3':
                news_feed = NewsFeed('currency conversion rate')
                news_feed.add_record()
                news_feed.add_publication()
            elif choice == '4':
                print("Exiting the program.")
                break
            else:
                print('Invalid choice. Please select a valid option.')


if __name__ == "__main__":
    run_app = AppRunner()
    run_app.console_runner()
