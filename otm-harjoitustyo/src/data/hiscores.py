from initialize_database import initialize_database

class Hiscores:
    """Luokka, jonka tarkoitus on hoitaa tietokantaoperaatiot

    Attributes:
        connection: Connect-olio, joka toimii yhteytenä SQLite-tietokantaan"""

    def __init__(self, connection):
        """Luokan konstruktori, joka myös luo uuden tietokannan,
        mikäli sitä ei jo ole olemassa.
        """
        initialize_database()
        self.connection = connection


    def get_hiscores(self):
        """Tekee tietokantakyselyn, joka palauttaa tietokannasta top 10 pisteet.

        Returns:
            top_ten: Lista tupleista, joissa nimi, pisteet ja
            tieto siitä, pääsikö pelin läpi.
        """
        cursor = self.connection.cursor()

        top_ten = cursor.execute('''SELECT username, score, status
                                    FROM Hiscores
                                    ORDER BY score DESC
                                    LIMIT 10''').fetchall()

        cursor.close()

        return top_ten

    def add_high_score(self, username, score, status):
        """Lisää uuden tuloksen tietokantaan.

        Args:
            username: Käyttäjän valitsema nimi.
            score: Pelissä saadut pisteet.
            status: Tieto siitä, läpäistiinkö peli.
        """
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Hiscores (username, score, status) VALUES (?,?,?);",
                        [username, score, status])
        cursor.close()
