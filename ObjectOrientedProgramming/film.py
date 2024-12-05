

class Movie:

    id:int
    title:str
    rating:int
    run_time:int
    director:str
    genre:str

    def set_movie(self,id,title,rating,run_time,director,genre):

        self.id=id
        self.title=title
        self.rating=rating
        self.run_time=run_time
        self.director=director
        self.genre=genre

    def display(self):

        print(self.id,self.title,self.rating,self.run_time,self.director,self.genre) 

Movie_instance1=Movie()
Movie_instance2=Movie()

Movie_instance1.set_movie("ARM",7.6,230,"Jithin lal","action adventure fantasy")
Movie_instance2.set_movie("KGF",8.2,235,"Prashanth Neel","Action")

Movie_instance1.display()
Movie_instance2.display()