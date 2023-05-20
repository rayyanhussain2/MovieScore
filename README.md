Sure! Here's an example of a README file for your project:

# MovieScore

Members:
- Rayyan Hussain (2022399)
- Rahul Ramesh Omalur (2022392)
- Mehul Aggarwal (2022294)

## Project Brief

'MovieScore' is a search portal that allows users to search for movie descriptions and other information. Additionally, users can check if a movie is available on the top four streaming platforms worldwide: Netflix, Hulu, Amazon Prime, and Disney+.

## Brief Description of Source Code

The project consists of one file with 134 lines of code. We utilized the public API provided by TMDB (The Movie Database) to fetch movie data. The following classes and functions were implemented:

- Class: Movie
- Functions: createMovieObjects, platCheck, returnOTT, results

We also used the tkinter module to create the graphical user interface (GUI) for user interaction.

## Testing Approach

1. We started by creating a rough sketch and translated it into a GUI using tkinter.
2. Each function and class was tested using specific movies, comparing the results with the expected outputs.
3. We used the TMDB API and a CSV file containing movies available on at least one of the platforms.
4. The API functions were examined and tested individually.
5. Finally, we verified the details and platform availability of the movies listed in the CSV file.
