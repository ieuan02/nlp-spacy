import spacy
nlp = spacy.load("en_core_web_md")


def watch_next(user_movie):
    with open("movies.txt", "r+") as f:
        lines = f.readlines()

    movie_info = {}  # empty dict to append movie, with corresponding descriptions to.

    for i in range(len(lines)):
        # using appropriate string comprehension, text split into the movie title and description.
        movie_info[lines[i].split(" :")[0]] = lines[i].split(" :")[1]

    if user_movie in movie_info:
        info_to_compare = nlp(movie_info[user_movie])  # variable declared for nlp of our input, for better readability.

        # A separate dict is created, iterating through movie_info, with values assigned to similarity floats.
        similarities = {k: nlp(movie_info[k]).similarity(info_to_compare) for k in movie_info}

        # To ensure the recommendation isn't the movie the user just watched, we update the value in the dict.
        similarities.update({user_movie: 0})

        vals = list(similarities.values())  # Values and keys of this dict are created into two separate lists.
        keys = list(similarities.keys())  # Lets us cross-reference the index of the highest value to the movie name.
        print(f"Based on your watch history, we can recommend {keys[vals.index(max(vals))]}")

    else:  # Else clause covers possibility that user inputs a movie that doesn't exist
        print("Sorry, this film is not in our list of movies!")


watch_next("Movie B")  # Though I have just typed into the function directly, program could also take a user input.
