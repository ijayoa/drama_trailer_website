import media
import fresh_tomatoes

waikiki = media.Drama("Euchalala Waikiki",
                      "A korean comedy drama about six friends living in a guesthouse.",
                        "http://asianwiki.com/images/b/bc/Eulachacha_Waikiki-P3.jpg",
                        "https://www.youtube.com/watch?v=h-5HhJJLlUk", 2018, 20)

jealousy_incarnate = media.Drama("Jealousy Incarnate",
                      "A man develops breast cancer and finds love in the end.",
                        "http://asianwiki.com/images/f/ff/Jealousy_Incarnate-p1.jpg",
                        "https://www.youtube.com/watch?v=0HHy5nIxLFw", 2016, 24)

wok_of_love = media.Drama("Wok Of Love",
                      "A chef falls to the bottom in his career and struggles to rise again.",
                        "https://www.hancinema.net/photos/fullsizephoto971910.jpg",
                        "https://www.youtube.com/watch?v=1ccGurkcYcs", 2018, 40)

goblin = media.Drama("Goblin",
                      "A story of a god who waited 900 years for a human bride to end his immortal life.",
                        "http://asianwiki.com/images/b/b2/Goblin-p04.jpg",
                        "https://www.youtube.com/watch?v=U2UrxFwMORE", 2017, 16)

chief_kim = media.Drama("Chief Kim",
                        "A former accountant for gangs begin to work at a huge company by chance.",
                        "https://ia.media-imdb.com/images/M/MV5BMjU4Yzc3ZTctOGU5Yi00YjY0LWI0ZjktZDg4ZGIyZDNhOTA5L2ltYWdlXkEyXkFqcGdeQXVyNzk0NTA5NQ@@._V1_.jpg",
                        "https://www.youtube.com/watch?v=arBRqNeesCY", 2017, 20)

father_is_strange = media.Drama("Father Is Strange",
                      "A man falsely charged with murder is forced to impersonate his dead friend.",
                        "https://upload.wikimedia.org/wikipedia/en/0/0e/Father_is_Strange_poster.jpg",
                        "https://www.youtube.com/watch?v=J7SGe0FXIEI", 2017, 52)

black = media.Drama("Black",
                      "Black is a detective possessed by the Grim Reaper. Ha-Ram can see shadows of death.",
                        "http://asianwiki.com/images/9/91/Black_%28Korean_Drama%29-P1.jpg",
                        "https://www.youtube.com/watch?v=4JQoEw97sPI", 2017, 18)

because_life = media.Drama("Because This Is My First Life",
                      "Two people choose to marry purely out of material benefit but end up in love.",
                        "http://asianwiki.com/images/5/5d/Because_This_Is_My_First_Life-P1.jpg",
                        "https://www.youtube.com/watch?v=nGyMJU8zTjc", 2017, 16)


voice = media.Drama("Voice",
                      "A detective and a voice profiler work together to catch a serial killer.",
                        "http://asianwiki.com/images/a/ae/Voice_%28Korean_Drama%29-p1.jpg",
                        "https://www.youtube.com/watch?v=WFLuToc4Xek", 2017, 16)

full_dramas_list = [chief_kim, voice, because_life, black, goblin, wok_of_love, jealousy_incarnate, waikiki, father_is_strange]
fresh_tomatoes.open_movies_page(full_dramas_list)
