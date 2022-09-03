import re
from tkinter import *
from tkinter import ttk
from pygame import mixer
from PIL  import Image , ImageTk
import io
from ttkthemes import themed_tk
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import random
import audio_metadata
import os 
    

class MusicPlayer:
    def __init__(self, window):
        
        style=ttk.Style()
        style.theme_use('breeze')
        style.configure('TScale' , background='white')

        self.root=window
        self.root.configure(bg='white')

        self.play_image=Image.open('img/deer.png')
        self.play_image=self.play_image.resize((35 , 35))
        self.play_image=ImageTk.PhotoImage(image=self.play_image)

        self.repeat_on_image=Image.open('img/wand (2).png')
        self.repeat_on_image=self.repeat_on_image.resize((35 , 35))
        self.repeat_on_image=ImageTk.PhotoImage(image=self.repeat_on_image)

        self.repeat1_image=Image.open('img/key.png')
        self.repeat1_image=self.repeat1_image.resize((35 , 35))
        self.repeat1_image=ImageTk.PhotoImage(image=self.repeat1_image)

        self.repeat_off_image=Image.open('img/wand (1).png')
        self.repeat_off_image=self.repeat_off_image.resize((35 , 35))
        self.repeat_off_image=ImageTk.PhotoImage(image=self.repeat_off_image)

        self.fav_list_image =Image.open('img/magic_text.png')
        self.fav_list_image=self.fav_list_image.resize((35 , 35))
        self.fav_list_image=ImageTk.PhotoImage(image=self.fav_list_image)

        self.backward_image=Image.open('img/owl.png')
        self.backward_image=self.backward_image.resize((35 , 35))
        self.backward_image=ImageTk.PhotoImage(image=self.backward_image)

        self.favorite_off_image=Image.open('img/sparks.png')
        self.favorite_off_image=self.favorite_off_image.resize((35 , 35))
        self.favorite_off_image=ImageTk.PhotoImage(image=self.favorite_off_image)

        self.favorite_on_image=Image.open('img/sparks (1).png')
        self.favorite_on_image=self.favorite_on_image.resize((35 , 35))
        self.favorite_on_image=ImageTk.PhotoImage(image=self.favorite_on_image)

        self.next_image=Image.open('img/eyeglasses.png')
        self.next_image=self.next_image.resize((35 , 35))
        self.next_image=ImageTk.PhotoImage(image=self.next_image)

        self.font_image=Image.open('img/Screenshot (92).png')
        self.font_image=self.font_image.resize((250,110))
        self.font_image=ImageTk.PhotoImage(image=self.font_image)

        self.pause_image=Image.open('img/witch-hat.png')
        self.pause_image=self.pause_image.resize((35 , 35))
        self.pause_image=ImageTk.PhotoImage(image=self.pause_image)

        self.shuffle_on_image=Image.open('img/cards.png')
        self.shuffle_on_image=self.shuffle_on_image.resize((35 , 35))
        self.shuffle_on_image=ImageTk.PhotoImage(image=self.shuffle_on_image)

        self.shuffle_off_image=Image.open('img/cards(1).png')
        self.shuffle_off_image=self.shuffle_off_image.resize((35 , 35))
        self.shuffle_off_image=ImageTk.PhotoImage(image=self.shuffle_off_image)
        

        self.stop_image=Image.open('img/non_lighting.png')
        self.stop_image=self.stop_image.resize((30 , 30))
        self.stop_image=ImageTk.PhotoImage(image=self.stop_image)

        self.speaker_image=Image.open('img/noun-quill-.png')
        self.speaker_image=self.speaker_image.resize((25 , 25))
        self.speaker_image=ImageTk.PhotoImage(image=self.speaker_image)

        self.mute_image=Image.open('img/noun-dobby.png')
        self.mute_image=self.mute_image.resize((25 , 25))
        self.mute_image=ImageTk.PhotoImage(image=self.mute_image)

        self.search_image=Image.open('img/death.png')
        self.search_image=self.search_image.resize((35 , 35))
        self.search_image=ImageTk.PhotoImage(image=self.search_image)

        self.mother_label=Label(self.root , bg='white')
        self.mother_label.place(x=0 , y=460)

        self.list_of_song=Listbox(self.mother_label , font=('Ovation-axD6o' , 10) , width=54 ,selectmode= SINGLE)
        self.list_of_song.pack(side=LEFT , fill= BOTH)

        self.list_of_song_scrollbar=Scrollbar(self.mother_label ,orient= VERTICAL , command= self.list_of_song.yview)
        self.list_of_song_scrollbar.pack(side= RIGHT , fill= Y)


        self.fav_list_butten=Button(self.root ,  image=self.fav_list_image, command=self.favorite_song_list , bg='white' , relief= FLAT )
        self.fav_list_butten.place(x=20 , y=370)

        self.fav_list_label=Label(self.root , text= 'Fav songs list' , font=('times new roman'  , 7) , fg='black' , bg='white')
        self.fav_list_label.place(x=5 , y=410)

        self.backward_button=Button(self.root , image=self.backward_image ,command=self.previous_song , bg='white' , relief= FLAT)
        self.backward_button.place( x=80,y=370)

        self.backward_label=Label(self.root , text= 'Previos' , font=('times new roman'  , 7) , fg='black' , bg='white')
        self.backward_label.place(x=85 , y=410)

        self.play_button=Button(self.root , image=self.play_image ,command =self.check_pause_play, bg='white' , relief= FLAT)
        self.play_button.place(x=130 , y=370)

        self.play_label=Label(self.root , text= 'Play' , font=('times new roman'  , 7) , fg='black' , bg='white')
        self.play_label.place(x=135 , y=410)

        self.next_button=Button(self.root , image=self.next_image , command=self.next_song , bg='white' , relief= FLAT)
        self.next_button.place(x=180 , y=370)

        self.next_label=Label(self.root , text= 'Next' , font=('times new roman'  , 7) , fg='black' , bg='white')
        self.next_label.place(x=185 , y=410)

        self.repeat_button=Button(self.root , image=self.repeat_off_image , command=self.repeat , bg='white' , relief= FLAT)
        self.repeat_button.place(x=230 ,y=370)

        self.repeat_label=Label(self.root , text= 'Repeat' , font=('times new roman'  , 7) , fg='black' , bg='white')
        self.repeat_label.place(x=235 , y=410)

        self.shuffle_button=Button(self.root , image=self.shuffle_off_image, command=self.shuffle , bg='white' , relief= FLAT)
        self.shuffle_button.place(x=280 , y=370)

        self.shuffle_label=Label(self.root , text= 'Shuffle' , font=('times new roman'  , 7) , fg='black' , bg='white')
        self.shuffle_label.place(x=285 , y=410)

        self.favorite_button=Button(self.root ,  image=self.favorite_off_image ,command=self.favorite_song  , bg='white' , relief= FLAT)
        self.favorite_button.place(x=330, y=370)

        self.favorite_label=Label(self.root , text= 'Favorite' , font=('times new roman'  , 7) , fg='black' , bg='white')
        self.favorite_label.place(x=335 , y=410)

        self.song_scalebar=ttk.Scale(self.root , orient=HORIZONTAL , from_= 0 , command=self.scalebar_move, cursor= 'star' , length=150 , style='TScale')
        self.song_scalebar.place(x = 70 , y= 435)

        self.time_elapsed_label=Label(self.root , text='00:00' , width= 5 , foreground='black' , background='white')
        self.time_elapsed_label.place(x=10 , y=435)

        self.music_duration_label=Label(self.root , text='00:00' , width= 5 , foreground='black' , background='white')
        self.music_duration_label.place(x=235 , y=435)

        self.current_song_label=Label(self.root , text= 'Song: (0 / 0)' , fg='black' , background='white')
        self.current_song_label.place(x=290 , y=435)
        
        
        self.pic_song_label=Label(self.root ,  bg= 'white' )
        self.pic_song_label.place(x=110 , y=130)

        
        self.musicplayer_title=Label(self.root ,image=self.font_image , bg= 'white')
        self.musicplayer_title.place(x=70 , y=20 )

        self.menubar=Menu(self.root)
        self.add_menu=Menu(self.menubar , tearoff= 0)
        self.add_menu.add_command(label='Add song' , command=self.add_song, font= ('times new roman' , 11))
        self.menubar.add_cascade(label='Add Song' , menu= self.add_menu )
        self.root.configure(menu=self.menubar)

        self.delete_menu=Menu(self.menubar , tearoff= 0)
        self.delete_menu.add_command(label='delete song' , command=lambda :self.delet_song ('selected'), font= ('times new roman' , 11))
        self.delete_menu.add_command(label='delete all song' , command=lambda :self.delet_song ('all'), font= ('times new roman' , 11))
        self.menubar.add_cascade(label='Delete Song' , menu=self.delete_menu)

        self.song_name_label=Label(self.root ,width=27 , text='Song name Artist name' , fg= 'black' , font= ('times new roman' ,9) , bg='white')
        self.song_name_label.place(x=100 , y=325)
        
        self.scalebar_volume=ttk.Scale(self.root , length=60 , command=self.set_volum )
        self.scalebar_volume.place(x=300 , y=7)

        self.volume_butten=Button(self.root , image=self.speaker_image , background='white' , relief=FLAT , command=self.mute_unmute)
        self.volume_butten.place(x=260 , y=2)

        self.volume_label=Label(self.root , text= 'Volume' , font=('times new roman'  , 7) , fg='black' , bg='white')
        self.volume_label.place(x=310 , y=25)

        self.show_current_volume=Label(self.root , font=('times new romans' , 10) , bg= 'white')
        self.show_current_volume.place(x=370 , y=2)

        self.search_box_entry=Entry(self.root , width= 20  , bd=1 , bg='white'  , relief= SUNKEN)
        self.search_box_entry.place(x=90 , y= 8)
        self.search_box_entry.focus()

        self.search_box_label=Label(self.root ,text='Search Song'  , font=('times new roman' , 10) , bg='white', relief=FLAT)
        self.search_box_label.place(x=5 , y=6)
        self.list_of_song.config(yscrollcommand=self.list_of_song_scrollbar.set)

        self.repeat_mode= 0
        self.shuffle_mode= False
        self.fav_song_list=[]
        self.fav_mood=False
        self.fav_song_list_mode=False
        self.mute_mode=False
        self.pause_mode=False
        self.play_list=[]
        self.all_music=[]
        MusicPlayer.en_str =StringVar()
        self.search_box_entry['textvariable'] = MusicPlayer.en_str
        self.en_str.trace('w', self.check_song)
        #second way: 
        # self.search_box_entry.bind('<KeyRelease>' , self.check_song)
        #if we want put selected item in search box:
        # self.list_of_song.bind('<<ListboxSelect>>' , self.fillout)
        


    def add_song(self):
        self.filedialog=filedialog.askopenfilenames()
        for song in self.filedialog:
            self.all_music.append(song)
            self.list_of_song.insert(END , song)
    
    def play_song(self):
       current_song=self.list_of_song.get(ACTIVE)
       self.play_button.config(image=self.pause_image)

       self.time_elapsed_label['text']='00:00'
       self.song_scalebar['value']= 0

       self.data_song=MP3(current_song)
       self.song_lenght=int(self.data_song.info.length)

       self.sec_music=time.gmtime(self.song_lenght)
       self.music_duration_label['text']=time.strftime('%M:%S' , self.sec_music)

       self.song_scalebar['to']=self.song_lenght

       mixer.music.load(current_song)
       metadata=audio_metadata.load(current_song)
       artwork=metadata.pictures[0].data
       a = io.BytesIO(artwork)
       picofsong=Image.open(a)
       picofsong=picofsong.resize((180 , 180))
       self.pic_of_song=ImageTk.PhotoImage(image=picofsong)

       self.pic_song_label.config(image=self.pic_of_song)
       self.pic_song_label.image=self.pic_of_song
       
       full_name=os.path.join(current_song.split('/')[-1])
       song_name_format=os.path.join(full_name.split('-')[-1])
       song_name=os.path.join(song_name_format.split('.')[-2])
       artist_name=os.path.join(full_name.split('-')[-2])
       self.song_name_label['text']=f'{song_name} \n {artist_name}'
       self.song_name_label.text=f'{song_name} \n {artist_name}'

       index_song=self.list_of_song.index(ACTIVE)
       self.current_song_label['text']= f'Song: ( {index_song + 1} / {self.list_of_song.size()} ) '
       
       mixer.music.play()
       self.scale_update()

    
    def check_pause_play(self):
        if self.list_of_song.size() >=1 :
            self.play_list.append(self.list_of_song.get(ACTIVE))
            if self.list_of_song.get(ACTIVE) == self.play_list[0]:
                if len(self.play_list) == 1:
                    self.play_song()
                else:
                    self.puase_unpause()
            else:
                self.root.after_cancel(self.updater)
                self.play_list.clear()
                self.play_list.append(self.list_of_song.get(ACTIVE))
                self.play_song()


    def puase_unpause(self):
        if self.list_of_song.size() >=1 :
            if not self.pause_mode:
                self.root.after_cancel(self.updater)
                self.play_button.config(image=self.play_image)
                self.pause_mode=True
                mixer.music.pause()
            else:
                self.root.after_cancel(self.updater)
                self.play_button.config(image=self.pause_image)
                self.pause_mode=False
                mixer.music.unpause()
                self.scale_update()


    def scale_update(self):
        if self.song_scalebar['value'] < self.song_lenght:
            self.song_scalebar['value'] +=1

            self.time_elapsed_label['text']=time.strftime('%M:%S' , time.gmtime(self.song_scalebar.get()))
            self.updater=self.root.after(1000 , self.scale_update)
        elif self.repeat_mode == 1:
            self.next_song()

        elif self.repeat_mode == 2:
            self.play_song()

        else:
            self.time_elapsed_label['text']='00:00'
            self.song_scalebar['value']=0
            self.play_button.config(image=self.play_image)

            
    def scalebar_move(self,x):
        self.root.after_cancel(self.updater)
        

        present_position_scalbar=self.song_scalebar.get()
        current_song=self.list_of_song.get(ACTIVE)

        mixer.music.load(current_song)
        mixer.music.play(0 , present_position_scalbar)

        self.scale_update()
        
    def next_song(self):
        if self.list_of_song.size() >=1 :
            mixer.music.stop()
            self.root.after_cancel(self.updater)
            current_song_index=self.list_of_song.index(ACTIVE)
            self.list_of_song.selection_clear(ACTIVE)
        
            if current_song_index == self.list_of_song.size()-1:
                    
                self.list_of_song.selection_set(0)
                self.list_of_song.activate(0)
                self.check_pause_play()

            else:
                self.list_of_song.selection_clear(ACTIVE)
                self.list_of_song.selection_set(current_song_index + 1)
                self.list_of_song.activate(current_song_index + 1)
                self.check_pause_play()

            if self.fav_mood:
                self.fav_mood = False
                self.favorite_button.config(image= self.favorite_off_image)
        





    def previous_song(self):
        if self.list_of_song.size() >=1 :
            mixer.music.stop()
            current_song_index=self.list_of_song.index(ACTIVE)
            self.list_of_song.selection_clear(ACTIVE)
        
            if current_song_index == 0:
                self.list_of_song.selection_set(self.list_of_song.size() - 1)
                self.list_of_song.activate(self.list_of_song.size() - 1)
                self.check_pause_play()

            else:
                self.list_of_song.selection_set(current_song_index - 1)
                self.list_of_song.activate(current_song_index - 1)
                self.check_pause_play()
                
            if self.fav_mood:
                self.fav_mood = False
                self.favorite_button.config(image= self.favorite_off_image)
        
        

       
    def repeat(self):
        if self.repeat_mode == 0:
            self.repeat_button.config(image=self.repeat_on_image)
            self.repeat_mode = 1
            return
        elif self.repeat_mode == 1:
            self.repeat_button.config(image=self.repeat1_image)
            self.repeat_mode = 2
            return
        else:
            self.repeat_button.config(image= self.repeat_off_image)
            self.repeat_mode = 0
            return

    def shuffle(self):
        if self.list_of_song.size() >=1 :
            if not self.shuffle_mode:
                self.shuffle_mode=True
                self.shuffle_button.config(image=self.shuffle_on_image)
                current_song=self.list_of_song.get(ACTIVE)

                play_list=list(self.list_of_song.get('0' , END))
                self.list_of_song.delete('0', END)
                random.shuffle(play_list)

                for i , song in enumerate(play_list):
                    self.list_of_song.insert(i , song)

                    if song == current_song:
                        self.list_of_song.selection_set(i)
                        self.list_of_song.activate(i)

                self.list_of_song.update()
            else:
                self.shuffle_mode=False
                self.shuffle_button.config(image=self.shuffle_off_image)


    def favorite_song(self):
        if not self.fav_mood:
            self.favorite_button.config(image=self.favorite_on_image)
            self.current_song=self.list_of_song.get(ACTIVE)
            self.fav_song_list.append(self.current_song)
            self.fav_mood = True
        else:
            self.fav_song_list.remove(self.current_song)
            self.favorite_button.config(image=self.favorite_off_image)
            self.fav_mood=False

    def favorite_song_list(self):
        if not self.fav_song_list_mode:
            self.fav_song_list_mode = True
            self.label=Label(self.root, bg='white' , text='Favorite Musics:' , font=('times new roman' , 15) , anchor= N)
            self.label.pack(fill= BOTH, side= BOTTOM)
            self.fav_song_listbox=Listbox(self.label , font=('times new roman' , 10) , bg='white' , width= 55, height= 6)
            self.fav_song_listbox.pack(padx= 20 , pady= 30 , fill= BOTH , side=LEFT)

            self.fav_song_list_scrollbar=Scrollbar(self.label ,orient= VERTICAL , command=self.fav_song_listbox.yview )
            self.fav_song_list_scrollbar.pack(side=RIGHT ,  fill=Y)
            self.fav_song_listbox.config(yscrollcommand=self.fav_song_list_scrollbar.set)

            for i in self.fav_song_list:
                self.fav_song_listbox.insert(END , i)

            
        else:
            self.fav_song_list_mode= False
            self.label.pack_forget()
        
            

    def delet_song(self , name):
        self.root.after_cancel(self.updater)
        mixer.music.stop()
        if  name == 'selected':
            self.current_song=self.list_of_song.index(ACTIVE)
            self.list_of_song.delete(self.current_song)
            self.next_song()
        else:
            self.list_of_song.get('0' , END)
            self.list_of_song.delete('0' , END)
            self.time_elapsed_label['text']='00:00'
            self.music_duration_label['text']='00:00'
            self.song_scalebar['value']=0
            self.play_button.config(image=self.play_image)


    def set_volum(self , x):
        mixer.music.set_volume(self.scalebar_volume.get())
        self.current_volume=mixer.music.get_volume()
        self.current_volume *=100
        self.show_current_volume['text']= int(self.current_volume)

        if self.current_volume == 0:
            self.volume_butten.config(image= self.mute_image)
        else:
            self.volume_butten.config(image= self.speaker_image)
        
    
    def mute_unmute(self):
        if not self.mute_mode:
            mixer.music.set_volume(0.0)
            self.current_volume=mixer.music.get_volume()
            self.current_volume *=100
            self.show_current_volume['text']= int(self.current_volume)
            self.scalebar_volume['value'] = 0
            self.mute_mode = True
            self.volume_butten.config(image= self.mute_image)
            
        else:
            self.set_volum(x)
            self.mute_mode = False
            self.volume_butten.config(image=self.speaker_image)

    def check_song(self,*args):
        self.list_of_song.delete('0', END)
        typed = self.search_box_entry.get()
        for i in self.all_music:
            if re.search(typed.lower() , i.lower() , re.IGNORECASE):
                self.list_of_song.insert(END,i)
                
        #second way:       
        # if typed == '':
        #     for item in self.all_music:
        #         self.list_of_song.insert(END,item)
        # else:
        #     for item in self.all_music:
        #         if typed.lower() in item.lower():
        #             self.list_of_song.insert(END,item)


    # def fillout(self):
    #     self.search_box_entry.delete('0',END)
    #     self.search_box_entry.insert(END,self.list_of_song.get(ACTIVE))
    
    


if __name__== '__main__':

    window=themed_tk.ThemedTk()
    window.title('Harry Potter Music player')
    window.geometry('400x600')
    window.wm_iconbitmap('img/music.ico')

    mixer.init()

    x = MusicPlayer(window)
    window.mainloop()
