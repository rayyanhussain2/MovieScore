import requests
import tkinter 
from PIL import Image, ImageTk
import csv

class Movie:
    def __init__(self, title, lang, date, vote_av, vote_count, overview, thumb):
        self.title = title
        self.lang = lang
        self.date = date
        self.vote_av = vote_av
        self.vote_count = vote_count
        self.overview = overview
        self.link = ""
        self.thumb = thumb

def createMovieObjects(movie_list, resp_dict):
    for i in range(len(resp_dict['results'])):
        curr_movie = resp_dict['results'][i]
        new = Movie(curr_movie['original_title'], curr_movie['original_language'], curr_movie['release_date'].split('-')[0], curr_movie['vote_average'], curr_movie['vote_count'], curr_movie['overview'], curr_movie['poster_path'])
        movie_list.append(new)

def platCheck(s):
    fh=open("movies.csv","r",errors="ignore")
    fhr=csv.reader(fh)
    movDict={}  

    for i in fhr:
        movDict[i[2].lower()]=[i[6],i[7],i[8],i[9]]

    if s.lower() in movDict:
        return movDict[s.lower()]
    else:
        return ['0', '0', '0', '0']

def returnOTT(OTTtf):
    result = []
    
    if OTTtf[0] == '1':
        result.append("Netflix")
    if OTTtf[1] == '1':
        result.append("Hulu")
    if OTTtf[2] == '1':
        result.append("Prime Video")
    if OTTtf[3] == '1':
        result.append("Disney Hotstar")
        

    return ", ".join(result)

def results():
    s = search_box.get()
    "+".join(s.split())
    resp = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key=dfaaf6d24c827c1c42bba06f155ae1ec&query={s}')
    resp_dict = resp.json() 

    movie_list = []
    createMovieObjects(movie_list, resp_dict)
    
    if len(movie_list) > 0:
        result_window = tkinter.Toplevel()
        result_window.title(f'{movie_list[0].title}')
        result_window.geometry("1024x720")

        movie_name = tkinter.Label(result_window, text = f"{movie_list[0].title}", font = ("Helvetica", 30))
        movie_name.place(x = 10, y = 150)    

        movie_date = tkinter.Label(result_window, text = f"{movie_list[0].date}", font = ("Helvetica", 15))
        movie_date.place(x = 11, y = 200)

        movie_vote_av = tkinter.Label(result_window, text = f"{round(movie_list[0].vote_av, 1)}/10", font = ("Helvetica", 15))
        movie_vote_av.place(x = 150, y = 200)

        movie_vote_count = tkinter.Label(result_window, text = f"out of {movie_list[0].vote_count} reviews", font = ("Helvetica", 10))
        movie_vote_count.place(x = 220, y = 205)

        movie_lang = tkinter.Label(result_window, text = f"{movie_list[0].lang}", font = ("Helvetica", 15))
        movie_lang.place(x = 400, y = 200)

        movie_overview = tkinter.Label(result_window, text = f"{movie_list[0].overview}", font = ("Helvetica", 20), wraplength= 580, justify = "left")
        movie_overview.place(x = 11, y = 260)

        printOTT = returnOTT(platCheck(s))
        if printOTT != '':
            OTTprint = tkinter.Label(result_window, text = f"Watch on: {printOTT}", font = ("Helvetica", 20))
            OTTprint.place(x = 11, y = 630)   
        
        #Downloading the poster
        poster = Image.open(requests.get(f"https://image.tmdb.org/t/p/w500{movie_list[0].thumb}", stream = True).raw)
        poster.save(f'movie_poster.png')
              
        #Creating a container for the poster
        thumb = Image.open(f"movie_poster.png")
        thumb = thumb.resize((267, 400), Image.ANTIALIAS)
        thumb_Tk = ImageTk.PhotoImage(thumb)

        container = tkinter.Label(result_window, image = thumb_Tk)
        container.image = thumb_Tk
        container.place(x=650, y=160)

        result_window.mainloop()

#Main Script------------------------------------------------------------------------------------
#Initializing window
main_window = tkinter.Tk()
main_window.title("MovieScore")
main_window.geometry("1024x720")

#moviescore logo
logo = Image.open("logo.png")
logo_tk = ImageTk.PhotoImage(logo)

container0 = tkinter.Label(main_window, image = logo_tk)
container0.image = logo_tk
container0.place(x=250,y=80)

#search box
search_box = tkinter.Entry(main_window, bd=2, selectborderwidt=2, bg="white", width=30, font=('Helvetica 24'))
search_box.place(x=240,y=260)

#search button
search_button = tkinter.Button(main_window, text="Search", bg='white', fg="black", width=30, command = results)
search_button.place(x=400, y=320)

#tmdb logo
img = Image.open("tmdb.png")
img_tk = ImageTk.PhotoImage(img)

container = tkinter.Label(main_window, image = img_tk)
container.image = img_tk
container.place(x=370,y=600)

#running the window
main_window.mainloop()