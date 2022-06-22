'''
#Tout d'abord, le jeu ne contient que deux joueurs
(je pourrais faire plus mais je n'avais pas assez de temps et de connaissances comme mon premier projet)
#Le plateau de jeu est composé d'une matrice de 64 lignes et 2 colonnes qui sont x et y
# Il y a une fenêtre principale qui contient l'entrée des deux noms de joueurs et le bouton de démarrage
#La deuxième fenêtre est l'endroit où les joueurs peuvent lancer les dés et déplacer leurs pions
//Les conditions//
1-Si le joueur tombe sur la case de l'autre joueur, il retourne sur son ancienne case
2-si le joueur atterrit sur la case 31, il retourne sur la case 20
3-si le joueur atterrit sur la case 42, il retourne sur la case 30
4-si le joueur atterrit sur la case 63 il gagne
'''
from time import sleep
from tkinter import *
import random
#counters in case if the player step on the case 19
blocking_counter1=0
blocking_counter2=0
#players turns 
player1_turn=1
player2_turn=2
click_times=0
#players amount counters (current place)
player1_counter=0
player2_counter=0
#this lst is a matrix composed of two columns (x and y ) those numbers describe every case x and y
lst=[[268,470],[268,420],[268,379],[268,332],[268,285],[268,240],[268,193],[268,148]
,[315,148],[355,148],[404,148],[452,148],[500,148],[545,148],[592,148],
[592,193],[592,240],[592,285],[592,332],[592,379],[592,420],[592,470],
[545,470],[500,470],[452,470],[404,470],[355,470],[315,470],
[315,425],[315,379],[315,332],[315,285],[315,240],[315,193],
[355,193],[404,193],[452,193],[500,193],[545,193],
[545,240],[545,285],[545,332],[545,379],[545,425],
[500,425],[452,425],[404,425],[355,425],
[355,379],[355,332],[355,285],[355,240],
[404,240],[452,240],[500,240],
[500,285],[500,332],[500,379],
[452,379],[404,379],
[404,332],[404,285],
[452,285],
[452,332]]
#the new window of the game (second window)
def start_game():
   new_game_window=Toplevel()
   new_game_window.geometry("909x599")
   new_game_window_bg=Canvas(new_game_window,width=1280,height=720)
   new_game_window_bg.pack()
   new_game_window_bg.create_image(0,0,image=duck_picture,anchor= "nw")
   leave_button=Button(new_game_window,text='leave',width=15,height=2
   ,command=new_game_window.destroy,font='arial',bg="red").place(x=720,y=0)
   #rest button command :
   def rest_counters() :
      global player1_counter
      global player2_counter
      global blocking_counter1
      global blocking_counter2
      player1_counter=0
      player2_counter=0
      pion1.place(x=lst[0][0],y=lst[0][1])
      pion2.place(x=lst[0][0],y=lst[0][1])
      player_2_amount.config(text="0")
      player_1_amount.config(text="0")
      player_1_pos.config(text="0")
      player_2_pos.config(text="0")
      matrix_place.config(text=lst)
      players_news.config(text='')
      blocking_counter1=0
      blocking_counter2=0
      player_2_playing_dice1.config(state=DISABLED,text="dice !",bg='white')
      player_1_playing_dice1.config(state=ACTIVE,text="dice !",bg='white')
   #player1 dice _ in the command dice
   def dice1() :
     global player1_counter
     global blocking_counter1
     global player2_counter
     global blocking_counter2
     global player1_turn
     players_news.config(text="")
     old_place=player1_counter
     player_1_dice1=random.randint(1,12)
     player_1_pos.config(text=str(player_1_dice1))
     player1_counter+=player_1_dice1
     if player2_counter==player1_counter :
         for i in range(old_place,player1_counter+1) :
             pion1.place(x=lst[i][0],y=lst[i][1])
             sleep(0.1)
             new_game_window.update()
         for i in range(player1_counter,old_place,-1) :
           pion1.place(x=lst[i][0],y=lst[i][1])
           sleep(0.1)
           new_game_window.update()
         player1_counter=old_place
         players_news.config(text=Entry_name_player1.get()+" back to old place")
     if player1_counter<63 :
         player_1_amount.config(text="amount :"+str(player1_counter))   
         for i in range(old_place,player1_counter+1) :
           pion1.place(x=lst[i][0],y=lst[i][1])
           sleep(0.1)
           new_game_window.update()

         player_2_playing_dice1.config(state=ACTIVE,bg='green')
         player_1_playing_dice1.config(state=DISABLED,bg='red')
     #case "Le Puits"
     if player1_counter==31 :
         for i in range(31,20,-1) :
            pion1.place(x=lst[i][0],y=lst[i][1])
            sleep(0.1)
            new_game_window.update()
         player1_counter=20
         player_1_amount.config(text="amount :"+str(player1_counter))   
         players_news.config(text="Le Puits :"+Entry_name_player1.get()+ " back to 20!")
     #case of 42 return to 30
     if player1_counter==42 :
          for i in range(42,30,-1) :
           pion1.place(x=lst[i][0],y=lst[i][1])
           sleep(0.1)
           new_game_window.update()
          player1_counter=30
          player_1_amount.config(text="amount :"+str(player1_counter))   
          players_news.config(text=Entry_name_player1.get()+" back to 30!")
     #case of winning
     if player1_counter==63 :
         for i in range(old_place,64) :
          pion1.place(x=lst[i][0],y=lst[i][0])
          sleep(0.1)
          new_game_window.update()
         players_news.config(text=Entry_name_player1.get()+' Won!!!')
     #case of getting more than 63
     if player1_counter>63 :
         for i in range(old_place,63) :
             pion1.place(x=lst[i][0],y=lst[i][1])
             sleep(0.1)
             new_game_window.update()
         for i in range(63,old_place-1,-1) :
             pion1.place(x=lst[i][0],y=lst[i][1])
             sleep(0.1)
             new_game_window.update()
         player1_counter=old_place
         player_1_amount.config(text=str(player1_counter))
         players_news.config(text='you can t depass 63')          
         player_2_playing_dice1.config(state=ACTIVE,bg='green')
         player_1_playing_dice1.config(state=DISABLED,bg='red')
     #case of 19 blocking rounds
     #case of Tête de mort
     if player1_counter==58 :
         players_news.config(text=Entry_name_player1.get()+" back to start")
         for i in range(58,-1,-1) :
             pion1.place(x=lst[i][0],y=lst[i][1]) 
             sleep(0.03)
             new_game_window.update()
         player1_counter=0
     #stopping the game when someone wins 
     if player1_counter==63 and player1_counter>player2_counter :
        player_1_playing_dice1.config(state=DISABLED,text="winner",bg="white")
        player_2_playing_dice1.config(state=DISABLED,text="lost",bg="white")
    #end of player1 dice
    #player2 dice
   def dice2() :
     global player2_counter
     global blocking_counter2
     global blocking_counter1
     global player1_counter
     players_news.config(text="")
     old_palce2=player2_counter
     player_2_dice1=random.randint(1,12)
     player_2_pos.config(text=str(player_2_dice1))
     player2_counter+=player_2_dice1  
     #case of same place
     if player2_counter==player1_counter :
         for i in range(old_palce2,player2_counter+1) :
             pion2.place(x=lst[i][0],y=lst[i][1])
             sleep(0.1)
             new_game_window.update()
         for i in range(player2_counter,old_palce2,-1) :
           pion2.place(x=lst[i][0],y=lst[i][1])
           sleep(0.1)
           new_game_window.update()
         player2_counter=old_palce2
         players_news.config(text=Entry_name_player2.get()+" back to old place")
     #normal play
     if player2_counter<63 :
         player_2_amount.config(text="amount :"+str(player2_counter))   
         for i in range(old_palce2,player2_counter+1) :
          pion2.place(x=lst[i][0],y=lst[i][1])
          sleep(0.1)
          new_game_window.update()
         player_1_playing_dice1.config(state=ACTIVE,bg='green')
         player_2_playing_dice1.config(state=DISABLED,bg='red')
     #case "Le Puits"
     if player2_counter==31 :
      for i in range(31,20,-1) :
            pion2.place(x=lst[i][0],y=lst[i][1])
            sleep(0.1)
            new_game_window.update()
      player2_counter=20
      player_2_amount.config(text="amount :"+str(player2_counter))   
      players_news.config(text="Le Puits "+Entry_name_player2.get()+" back to 20!")
     #case of 42 return to 30
     if player2_counter==42 :
          for i in range(42,30,-1) :
            pion2.place(x=lst[i][0],y=lst[i][1])
            sleep(0.1)
            new_game_window.update()
          player2_counter=30
          player_2_amount.config(text="amount :"+str(player2_counter))   
          players_news.config(text=Entry_name_player2.get()+" back to 30!") 
     #case of winning
     if player2_counter==63 :
         for i in range(old_palce2,64) :
             pion2.place(x=lst[i][0],y=lst[i][1])
             sleep(0.1)
             new_game_window.update()
         players_news.config(text=Entry_name_player2.get()+' Won!!')
    #case of getting more than 63
     if player2_counter>63 :
         for i in range(old_palce2,63) :
             pion2.place(x=lst[i][0],y=lst[i][1])
             sleep(0.1)
             new_game_window.update()
         for i in range(63,old_palce2-1,-1) :
             pion2.place(x=lst[i][0],y=lst[i][1])
             sleep(0.1)
             new_game_window.update()
         player2_counter=old_palce2
         player_2_amount.config(text=str(player2_counter))
         players_news.config(text='you can t depass 63')          
         player_1_playing_dice1.config(state=ACTIVE,bg='red')
         player_2_playing_dice1.config(state=DISABLED,bg='green')
      #case of player 1 beeing blocked 
      #case of Tête de mort
     if player2_counter==58 :
         players_news.config(text=Entry_name_player2.get()+" back to start")
         for i in range(58,-1,-1) :
             pion2.place(x=lst[i][0],y=lst[i][1]) 
             sleep(0.03)
             new_game_window.update()
         player2_counter=0
    #adding thins when someone wins 
     if player2_counter==63 and player2_counter>player1_counter :
        player_1_playing_dice1.config(state=DISABLED,text="lost",bg="white")
        player_2_playing_dice1.config(state=DISABLED,text="winner",bg="white")
    #end of player2 dice     
   matrix_place=Label(new_game_window,text=lst,
   width=400,height=400,image=hash_table)
   matrix_place.place(x=250,y=130)
   players_news=Label(new_game_window,width=40,height=2,text="",bg='black',fg='red',font="arial")
   players_news.place(x=220,y=15)
   #player 1 dice :
   player_1_name_label=Label(new_game_window,text=Entry_name_player1.get(),
   width=10,height=2,fg='red',font='arial')
   player_1_name_label.place(x=90,y=120)
   player_1_playing_dice1=Button(new_game_window,bg='green',command=dice1,text='dice !',width=10,height=2,font='arial')
   player_1_playing_dice1.place(x=90,y=180)
   player_1_pos=Label(new_game_window,text='',width=8,height=1,font='arail',bg='cyan')
   player_1_pos.place(x=90,y=250)
   player_1_amount=Label(new_game_window,text="",width=11,height=1,font='arial')
   player_1_amount.place(x=90,y=300)
   pion1=Label(new_game_window,image=Pion1,width=45,height=45)
   pion1.place(x=lst[0][0],y=lst[0][1])
  #player2 dice :
   player_2_name_label=Label(new_game_window,text=Entry_name_player2.get(),
   width=10,height=2,fg='red',font='arial')
   player_2_name_label.place(x=680,y=120)
   player_2_playing_dice1=Button(new_game_window,bg='red',state=DISABLED,command=dice2,text='dice !',width=10,height=2,font='arial')
   player_2_playing_dice1.place(x=680,y=180)
   player_2_pos=Label(new_game_window,text='',width=8,height=1,font='arail',bg='cyan')
   player_2_pos.place(x=680,y=250)
   player_2_amount=Label(new_game_window,text="",width=11,height=1,font='arial')
   player_2_amount.place(x=680,y=300)
   pion2=Label(new_game_window,image=Pion2,width=45,height=45)
   pion2.place(x=lst[0][0],y=lst[0][1])
#reset game button
   rest_game=Button(new_game_window,command=rest_counters,text="rest game",width=10,height=2,bg='red',font='arial')
   rest_game.place(x=0,y=0)
def okey1() :
   welcome_player1.config(text="welcome "+Entry_name_player1.get()
   ,font= 'Helvetica 13')
#function in the first page when you enter the names and click done it shows u the welcome+name
def okey2(): 
   welcome_player2.config(text="welcome "+Entry_name_player2.get()
   ,font= 'Helvetica 13')
game_window=Tk()
game_window.geometry("909x599")
game_window.title("Jeu de l oie")
#images of the game
duck_picture = PhotoImage(file="ducknormal.png")
start_pic=PhotoImage(file="start_pic.png")
hash_table=PhotoImage(file="table.png")
Pion1=PhotoImage(file="pion1.png")
Pion2=PhotoImage(file="pion2.png")
#end images
# the background picture 
duck_with_table=PhotoImage(file="duckpic.png")
duck_picture_place=Canvas(game_window,width=1280,height=720)
duck_picture_place.pack(fill="both",expand=True)
duck_picture_place.create_image(0,0,image=duck_picture,anchor = "nw")
#end here background picture
# Button of the main window (first window)
Button_leave=Button(text='Leave !',bg='red',
width=15,height=2,font='arial',command=game_window.destroy).place(x=720,y=0)
Button_start=Button(text='Start',font='arial',bg='red',image=start_pic,
width=320,height=110,command=start_game).place(relx=0.5,rely=0.5,anchor=CENTER)
#First player Buttons 
player_1_text=Label(game_window,text="Enter the first player name ! :"
,width=30,height=3,fg='red').place(x=0,y=0)
Entry_name_player1=Entry(game_window,width=15,
font='arial')
Entry_name_player1.place(x=0,y=55)
welcome_player1=Label(game_window, text="", font="Courier 22 bold",width=15)
welcome_player1.place(x=330,y=450)
done_button1=Button(game_window,command=okey1,text='done',width=10).place(x=202,y=58)
#end of the first player
#second player buttons
player_2_text=Label(game_window,text="Enter the second player name ! :"
,width=30,height=3,fg='red').place(x=0,y=90)
Entry_name_player2=Entry(game_window,width=15,
font='arial')
Entry_name_player2.place(x=0,y=150)
welcome_player2=Label(game_window, text="", font="Courier 22 bold",width=15)
welcome_player2.place(x=330,y=370)
done_button=Button(game_window,command=okey2,text='done',width=10).place(x=202,y=150)
#end of the second player  
#end of buttons(main window) 
game_window.mainloop()