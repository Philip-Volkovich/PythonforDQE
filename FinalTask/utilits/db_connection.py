import pyodbc


class DBConnection:
    def __init__(self):
        """Initialize a DBConnection instance for database operations."""
        self.database = 'final_task'
        self.table_name = 'locations'
        self.columns_with_types = """id INTEGER PRIMARY KEY AUTOINCREMENT,
                            city TEXT,
                            latitude DECIMAL(9,6),
                            longitude DECIMAL(9,6),
                            UNIQUE (city)"""

        with pyodbc.connect(f'''Driver=SQLite3 ODBC Driver;
                                          Database={self.database}''', autocommit=True) as cnxn:
            self.cursor = cnxn.cursor()

    def db_create(self):
        """Create the 'locations' table if it does not exist."""
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.table_name} (
                                {self.columns_with_types})''')

    def db_insert(self, columns, insert_values):
        """Insert a new row into the 'locations' table.

        Args:
            columns (str): Comma-separated column names.
            insert_values (str): Comma-separated values to be inserted."""
        try:
            self.cursor.execute(f"""INSERT INTO {self.table_name} ({columns})
                           VALUES ({insert_values})""")
            print(f"Row inserted successfully into {self.table_name} table")
        except pyodbc.Error as e:
            if 'UNIQUE constraint failed' in str(e):
                print("Error: Unique constraint violation - Record already exists")
            else:
                raise e

    def db_select(self, columns='*'):
        """Select data from the 'locations' table.

        Args:
        columns (str, optional): Comma-separated column names to select. Defaults to '*'.

        Returns:
        list: List of selected rows.
        """
        self.cursor.execute(f"SELECT {columns} FROM {self.table_name}")
        rows = self.cursor.fetchall()
        return rows

    def db_select_city_record(self, city, columns='*'):
        """Select data for a specific city from the 'locations' table.

        Args:
        city (str): The name of the city.
        columns (str, optional): Comma-separated column names to select. Defaults to '*'.

        Returns:
        str: Selected data for the city or 'None' if the city is not found.
        """
        self.cursor.execute(f"""SELECT {columns} FROM {self.table_name}
                            WHERE city = '{city}'""")
        rows = self.cursor.fetchall()
        if not rows:
            return 'None'

        return rows[0][0]
