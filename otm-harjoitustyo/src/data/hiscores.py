from initialize_database import initialize_database

class Hiscores:

    def __init__(self, connection):

        initialize_database()
        self.connection = connection


    def get_hiscores(self):
        cursor = self.connection.cursor()

        top_ten = cursor.execute('''SELECT username, score, status
                                    FROM Hiscores
                                    ORDER BY score DESC
                                    LIMIT 10''').fetchall()

        cursor.close()

        return top_ten

    def add_high_score(self, username, score, status):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Hiscores (username, score, status) VALUES (?,?,?);",
                        [username, score, status])
        cursor.close()
