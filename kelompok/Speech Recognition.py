'''

Pastikan Anda telah menginstal modul-modul yang diperlukan sebelum menjalankan program ini. 
Anda dapat menginstal modul tersebut dengan menjalankan perintah berikut di terminal atau command prompt:

pip install SpeechRecognition nltk pygame pyphen


'''

from tkinter import *
from tkinter.messagebox import *
import speech_recognition as sr
from nltk import edit_distance
from string import punctuation
import pyphen
import pygame
import tempfile
import os

class YukBicaraApp:
    def __init__(self, master):
        self.master = master
        master.title("YukBicara")

        self.frame = Frame(master, bg='#f8b474')
        self.frame.pack()

        self.bg = PhotoImage(file="background.png")

        self.canvas = Canvas(self.frame, width=self.bg.width(), height=self.bg.height())
        self.canvas.pack()

        self.canvas.create_image(0, 0, anchor=NW, image=self.bg)

        self.reference_text_display = Text(self.frame, height=10, width=95, wrap="word", font=("Josefin sans", 12), bg='#F0F0F0', fg='#333333')
        self.reference_text_display.place(x=405, y=50)
        self.reference_text_display.config(highlightthickness = 0, borderwidth=0)

        self.user_reference_label = Label(self.frame, text="Masukkan teks Anda :", font=("Josefin sans", 12), bg='#ffb464', fg='#333333')
        self.user_reference_label.place(x=500, y=320)
        self.user_reference_label.config(highlightthickness = 0, borderwidth=0)


        self.user_reference_entry = Entry(self.frame, width=35, font=("Josefin sans", 12), bg='#F0F0F0')
        self.user_reference_entry.place(x=710, y=320)
        self.user_reference_entry.config(highlightthickness = 0, borderwidth=0)

        self.speed_category_label = Label(self.frame, text="Pilih Kategori Kecepatan Berbicara Anda:", font=("Josefin sans", 12), bg='#ffb464', fg='#333333')
        self.speed_category_label.place(x=500, y=365)

        self.speed_options = ["Slow (110 WPM)", "Average (140 WPM)", "Fast (170 WPM)"]
        self.speed_variable = StringVar(master)
        self.speed_variable.set(self.speed_options[1])

        self.speed_dropdown = OptionMenu(self.frame, self.speed_variable, *self.speed_options)
        self.speed_dropdown.place(x=833, y=364)
        self.speed_dropdown.config(highlightthickness = 0, borderwidth=0)
        self.speed_dropdown.config(bg = '#F0F0F0')
        self.speed_dropdown.config(font=("Josefin sans", 12))

        self.reference_info_label = Label(self.frame, text='Tekan "Enter" untuk melihat informasi', font=("Josefin sans", 12), bg='#ffb464', fg='#333333')
        self.reference_info_label.place(x=730, y=406)

        self.change_user_reference_button = Button(self.frame, text="Enter", command=self.change_user_reference, font=("Josefin sans", 12), bg='#F0F0F0', fg='#333333')
        self.change_user_reference_button.place(x=863, y=453)
        self.change_user_reference_button.config(highlightthickness = 0, borderwidth=0)
        
        self.listen_button = Button(self.frame, text="Rekam", command=self.listen_and_process, font=("Josefin sans", 12), bg='#F0F0F0', fg='#333333')
        self.listen_button.place(x=857, y=509)
        self.listen_button.config(highlightthickness = 0, borderwidth=0)

        self.accuracy_label = Label(self.frame, text="Akurasi : ", font=("Josefin sans", 12), bg='#ffb464', fg='#333333')
        self.accuracy_label.place(x=850, y=560)
        self.accuracy_label.config(highlightthickness = 0, borderwidth=0)

        self.speed_label = Label(self.frame, text="Kecepatan Berbicara : ", font=("Josefin sans", 12), bg='#ffb464', fg='#333333')
        self.speed_label.place(x=805, y=600)
        self.speed_label.config(highlightthickness = 0, borderwidth=0)

        self.playback_button = Button(self.frame, text="Playback", command=self.playback, font=("Josefin sans", 12), bg='#F0F0F0', fg='#333333')
        self.playback_button.place(x=848, y=644)
        self.playback_button.config(highlightthickness = 0, borderwidth=0)

        self.error_label = Label(self.frame, text="Kata yang salah :", font=("Josefin sans", 12), bg='#ffb464', fg='#333333')
        self.error_label.place(x=500, y=740)

        self.error_display = Text(self.frame, height=5, width=68, wrap="word", font=("Josefin sans", 12), bg='#F0F0F0', fg='#333333')
        self.error_display.place(x=670, y=703)
        self.error_display.config(highlightthickness = 0, borderwidth=0)

        self.pyphen_dict = pyphen.Pyphen(lang='id')

    def update_reference_text_display(self):
        self.reference_text_display.delete(1.0, "end")
        self.reference_text_display.insert("end", f" {self.current_reference_text}\n")

    def update_reference_info(self):
        word_count = len(self.current_reference_text.split())
        speed_wpm = self.get_speed_wpm()
        speaking_time = self.estimate_speaking_time(self.current_reference_text.split(), speed_wpm)
        info_text = f"Jumlah Kata: {word_count} | Perkiraan Waktu Bicara: {speaking_time:.2f} detik"
        self.reference_info_label.config(text=info_text)

    def change_user_reference(self):
        user_reference_text = self.user_reference_entry.get()
        if user_reference_text:
            self.current_reference_text = user_reference_text
            self.update_reference_text_display()
            self.update_reference_info()

    def get_speed_wpm(self):
        speed_text = self.speed_variable.get()
        if "Slow" in speed_text:
            return 110
        elif "Average" in speed_text:
            return 140
        elif "Fast" in speed_text:
            return 170
        else:
            return 140

    def estimate_speaking_time(self, words, speed_wpm):
        return len(words) / speed_wpm * 60

    def calculate_speech_rate(self, audio_duration, text):
        syllables = sum(len(self.pyphen_dict.inserted(word).split('-')) for word in text.split())
        speech_rate = (syllables / audio_duration) * 60
        return speech_rate

    def calculate_accuracy(self, reference, hypothesis):
        reference = ''.join(char for char in reference if char not in punctuation).lower()
        hypothesis = ''.join(char for char in hypothesis if char not in punctuation).lower()

        if reference == hypothesis:
            return 100.0

        distance = edit_distance(reference.split(), hypothesis.split())
        accuracy = max(0, (1 - distance / max(len(reference.split()), 1))) * 100
        return accuracy

    def detect_errors(self, reference, hypothesis):
        reference = ''.join(char for char in reference if char not in punctuation).lower()
        hypothesis = ''.join(char for char in hypothesis if char not in punctuation).lower()

        reference_words = reference.split()
        hypothesis_words = hypothesis.split()

        errors = []
        for ref_word, hyp_word in zip(reference_words, hypothesis_words):
            if ref_word != hyp_word:
                errors.append((ref_word, hyp_word))

        return errors

    def playback_audio(self, audio_path):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            pygame.mixer.music.stop()  
            pygame.mixer.quit()  
        except Exception as e:
            print("Error saat pemutaran audio:", e)

    def playback(self):
        try:
            if hasattr(self, 'temp_audio_path') and os.path.exists(self.temp_audio_path):
                print("Playback file path:", self.temp_audio_path)
                self.playback_audio(self.temp_audio_path)
            else:
                print("File audio tidak ditemukan:", self.temp_audio_path)
        except Exception as e:
            print("Error saat playback:", e)

    def save_audio_temporarily(self, audio):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            temp_audio_path = temp_audio.name
            temp_audio.write(audio.get_wav_data())
            return temp_audio_path
        
    def listen_and_process(self):
        try:
            
            with sr.Microphone() as source:
                r = sr.Recognizer()
                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)
                text = r.recognize_google(audio, language="id")
                text = text.lower()

                audio_duration = len(audio.frame_data) / audio.sample_rate
                speech_rate = self.calculate_speech_rate(audio_duration, text)
                self.speed_label.config(text=f"Kecepatan berbicara: {speech_rate:.2f} words per minute")

                accuracy = self.calculate_accuracy(self.current_reference_text, text)
                self.accuracy_label.config(text=f"Akurasi: {accuracy:.2f}%")

                errors = self.detect_errors(self.current_reference_text, text)
                self.error_display.delete(1.0, "end")

                self.temp_audio_path = self.save_audio_temporarily(audio)
                
                if errors:
                    for ref_word, hyp_word in errors:
                        self.error_display.insert("end", f"- Seharusnya {ref_word}, sedangkan yang anda ucapkan adalah {hyp_word}\n")
                else:
                    self.error_display.insert("end", "Tidak ada kesalahan.")

        except sr.UnknownValueError:
            showinfo('Error','gangguan jaringan')
            print("Cek jaringan anda!")

if __name__ == "__main__":
    root = Tk()
    app = YukBicaraApp(root)
    root.geometry("1430x930")
    root.grid_columnconfigure(0, weight=1)
    app.frame.grid(row=0, column=0, sticky="e", padx=20, pady=20)
    root.mainloop()
    

