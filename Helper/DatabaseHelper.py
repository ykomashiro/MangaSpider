import sqlite3


class DatabaseHelper(object):
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.cur = self.conn.cursor()

    def create(self, table_name: str, keys_dict: dict):
        content = [
            '{0} {1} NOT NULL'.format(item[0], item[1].upper())
            for item in keys_dict.items()
        ]
        content = ','.join(content)
        command = "CREATE TABLE {0}({1});".format(table_name, content)
        self.cur.execute(command)

    def insert(self, table, values):
        for value in values:
            content = []
            for item in value:
                if isinstance(item, str):
                    item = '\'' + item + '\''
                content.append(str(item))
            content = ', '.join(content)
            command = "INSERT INTO {0} VALUES ({1});".format(table, content)
            self.cur.execute(command)

    def select(self, table):
        result = self.cur.execute("SELECT * from {}".format(table))
        return list(result)

    def top(self, table, desc=False):
        pass

    def delete(self, table, cond):
        if isinstance(cond[1], str):
            cond[1] = '\'' + cond[1] + '\''
        content = cond[0] + '=' + cond[1]
        command = "DELETE from {0} where {1}".format(table, content)
        self.cur.execute(command)

    def find(self):
        pass

    def commit(self):
        self.conn.commit()


if __name__ == "__main__":
    a = DatabaseHelper('test.db')
    #a.create('test', {'id': 'int', 'name': 'char(50)'})
    # for i in range(10):
    #     a.insert('test', [[i, '11']])
    print(a.select('test'))
    a.commit()
