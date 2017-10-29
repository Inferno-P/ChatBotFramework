from lib.actions import Action
from lib.entities import Entity
from lib.intents import Intent
from lib.UserInput import UserInput
from bot import Bot

def playMusic(singer = None, genre = None):
    print("playing music\nSinger : ",singer,"\nGenre : ",genre)

if __name__ == '__main__':
    #Action
    playMusicAction = Action(name="Play Music",method=playMusic)

    #Entities
    singer_names = ["A R Rahman","John Denver","Frank Sinatra","Queen B"]
    singer = Entity(name="Singer",domain=singer_names)

    genre_names = ["pop","rock","jazz","country"]
    genre = Entity(name="Genre",domain=genre_names)

    #Intent
    playMusicIntent = Intent(name="Play Music",entities=[singer,genre],action=playMusicAction)

    #UserInput
    inputList = ["play some jazz music","play some pop","How about some rock music","play John Denver","play music by Frank Sinatra"]
    playMusicUserInput = UserInput(inputList=inputList)


    #construct bot
    music = Bot("MusicBot")
    music.mapIntentToInput(intent=playMusicIntent,userInput=playMusicUserInput)
    music.build()
    music.test("play some jazz music")
