import fresh_tomatoes
import media

gone_girl = media.Movie("Gone Girl",
                        "With his wife's disappearance having become the focus of an intense media circus, a man sees the spotlight turned on him when it's suspected that he may not be innocent.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk0MDQ3MzAzOV5BMl5BanBnXkFtZTgwNzU1NzE3MjE@._V1_SY1000_CR0,0,678,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=Ym3LB0lOJ0o")
#print(toy_story.storyline)

warrior = media.Movie("Warrior",
                     "The youngest son of an alcoholic former boxer returns home, where he's trained by his father for competition in a mixed martial arts tournament - a path that puts the fighter on a collision course with his estranged, older brother.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk4ODk5MTMyNV5BMl5BanBnXkFtZTcwMDMyNTg0Ng@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                     "https://www.youtube.com/watch?v=kY7HcUACs58")
#print(avatar.storyline)
#avatar.show_trailer()

man_of_steel = media.Movie("Man of Steel",
                           "Clark Kent, one of the last of an extinguished race disguised as an unremarkable human, is forced to reveal his identity when Earth is invaded by an army of survivors who threaten to bring the planet to the brink of destruction.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMjI5OTYzNjI0Ml5BMl5BanBnXkFtZTcwMzM1NDA1OQ@@._V1_.jpg",
                           "https://www.youtube.com/watch?v=T6DJcgm3wNY")
#man_of_steel.show_trailer()

underworld = media.Movie("Underworld",
                         "Selene, a vampire warrior, is entrenched in a conflict between vampires and werewolves, while falling in love with Michael, a human who is sought by werewolves for unknown reasons.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNDExNDEyMV5BMl5BanBnXkFtZTcwODY1OTkxMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                         "https://www.youtube.com/watch?v=MqT-e44kIM8")

movies = [gone_girl, warrior, man_of_steel, underworld]
fresh_tomatoes.open_movies_page(movies)
