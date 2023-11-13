
# CREATE TABLES

artist_table_query = """
        CREATE TABLE IF NOT EXISTS `Artists` (
            `artist_id` varchar(100) NOT NULL,
            `name` varchar(100) NOT NULL,
            `location` varchar(100) NOT NULL,
            `logetitude` INT NOT NULL,
            `latitude` INT NOT NULL,

            PRIMARY KEY (`artist_id`)
        );
    """

time_table_query = """
    CREATE TABLE IF NOT EXISTS `Time` (
            `start_time` TIMESTAMP NOT NULL,
            `day` INT NOT NULL CHECK (`day` >= 0),
            `hour` INT NOT NULL CHECK (`hour` >= 0),
            `week` INT NOT NULL CHECK (`week` >= 0),
            `month` INT NOT NULL CHECK (`month` >= 0),
            `year` INT NOT NULL CHECK (`year` >= 0),
            `weekday` VARCHAR(50) NOT NULL,
            
            PRIMARY KEY (`start_time`)
        );
    """

session_table_query = """
        CREATE TABLE IF NOT EXISTS `Sessions` (
            `session_id` INT NOT NULL,
            `item_in_session` INT NOT NULL,

            PRIMARY KEY (`session_id`)
        );
    """ 

song_table_query = """
        CREATE TABLE IF NOT EXISTS `Songs` (
            `song_id` varchar(100) NOT NULL,
            `artist_id` varchar(100) NOT NULL,
            `title` varchar(255) NOT NULL,
            `year` INT NOT NULL CHECK (`year` >= 0),
            `duration` DECIMAL(8,5) NOT NULL,

            PRIMARY KEY (`song_id`),
            FOREIGN KEY (`artist_id) REFERENCES `Artists`(`artist_id`)

        );
    """

user_table_query = """
        CREATE TABLE IF NOT EXISTS `Users` (
            `user_id` INT NOT NULL,
            `first_name` varchar(100) NOT NULL,
            `last_name` varchar(100) NOT NULL,
            `gender` varchar(1) NOT NULL,
            `level` INT(100) NOT NULL,

            PRIMARY KEY (`user_id`)
        );
    """

songplay_table_query = """
        CREATE TABLE IF NOT EXISTS `Songplays` (
            `songplay_id` varchar(100) NOT NULL,
            `user_id` INT NOT NULL,
            `artist_id` varchar(100) NOT NULL,
            `song_id` varchar(100) NOT NULL,
            `session_id` INT NOT NULL,
            `start_time` TIMESTAMP NOT NULL,
            `location` varchar(100) NOT NULL,
            `user_Agent` TEXT NOT NULL,

            PRIMARY KEY (`songplay_id`),
            FOREIGN KEY (`user_id) REFERENCES `Users`(`user_id`),
            FOREIGN KEY (`artist_id) REFERENCES `Artists`(`artist_id`),
            FOREIGN KEY (`song_id) REFERENCES `Songs`(`song_id`),
            FOREIGN KEY (`session_id) REFERENCES `Sessions`(`session_id`),
            FOREIGN KEY (`start_time) REFERENCES `Time`(`start_time`)

        );
    """ 

# INSERT RECORDS INTO TABLES






