from tkinter import *
import time
import simpleaudio as sa
from datetime import datetime
from datetime import timedelta
from meditation_log_sql import MeditationLogSQL as mls


class MeditationLog:

    def __init__(self, master):
        self.session_begin = datetime.now()
        self.session_length = 0

        # Menu
        menu = Menu(master)
        master.config(menu=menu)

        # Header Label
        grid_row = 0

        header_label = Label(master, text="Meditation Timer")
        header_label.grid(row=grid_row, column=0, columnspan=2)

        grid_row += 1

        # Filler Row
        label_filler_1 = Label(master, text="")
        label_filler_1.grid(row=grid_row)

        grid_row += 1

        # Timer Section
        buffer_entry = Entry(master)
        time_entry = Entry(master)

        buffer_label = Label(master, text="Buffer (seconds)")
        time_label = Label(master, text="Time (minutes)")

        buffer_label.grid(row=grid_row, column=0)
        buffer_entry.grid(row=grid_row, column=1)

        # Sound Selection
        sound_choice = StringVar(master)
        sound_choice.set("Bell 1")

        choices = {"Bell 1", "Bell 2", "Bell 3"}

        sound_dropdown = OptionMenu(master, sound_choice, *choices)
        sound_dropdown.grid(row=grid_row, column=3)

        grid_row += 1

        time_label.grid(row=grid_row, column=0)
        time_entry.grid(row=grid_row, column=1)

        grid_row += 1

        # Countdown Section
        countdown_label = Label(master, text="Time Remaining")

        self.countdown_amt = StringVar()
        self.countdown_amt.set("Not started")
        countdown_amt_label = Label(master, textvariable=self.countdown_amt)

        countdown_label.grid(row=grid_row, column=0)
        countdown_amt_label.grid(row=grid_row, column=1)

        # Filler Row
        label_filler_2 = Label(master, text="")
        label_filler_2.grid(row=grid_row)

        grid_row += 1

        # Timer Control Buttons
        start_button = Button(master, text="Start", command=lambda: self.start_timer(time_entry.get(),
                                                                                     buffer_entry.get()))
        pause_button = Button(master, text="Pause", command=self.pause_timer)
        stop_button = Button(master, text="Stop")

        start_button.grid(row=grid_row, column=0)
        pause_button.grid(row=grid_row, column=1)
        stop_button.grid(row=grid_row, column=2)

        grid_row += 1

        # Filler Row
        label_filler_3 = Label(master, text="")
        label_filler_3.grid(row=grid_row)

        grid_row += 1

        # Previous session info
        prev_label = Label(master, text="Previous Session")
        prev_label.grid(row=grid_row, column=1)

        grid_row += 1
        duration_label = Label(master, text="Duration (minutes)")
        duration_label.grid(row=grid_row, column=0)

        self.duration_amt = StringVar()
        self.duration_amt.set("Empty")
        duration_amt_label = Label(master, textvariable=self.duration_amt)
        duration_amt_label.grid(row=grid_row, column=1, sticky="W")

        grid_row += 1
        save_prev_session = Button(master, text="Save Session", command=self.save_session)
        save_prev_session.grid(row=grid_row, column=1)

    def start_timer(self, time_length, buffer_length):
        time_length_sec = float(time_length) * 60
        buffer_length_sec = int(buffer_length)

        self.session_begin = datetime.now()
        self.session_length = time_length_sec

        # Wait before beginning timer
        print("buffer start")
        time.sleep(buffer_length_sec)

        # Play beginning tone
        wave_obj = sa.WaveObject.from_wave_file("C:/Users/Matt/Desktop/bell_1.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()

        # Start counting down
        print("The timer has started " + str(time_length) + str(buffer_length))
        print(str(time_length_sec))

        time.sleep(time_length_sec)

        # Play end tone
        play_obj = wave_obj.play()
        play_obj.wait_done()

        # Update previous session values
        self.duration_amt.set(str(time_length))

    def pause_timer(self):
        pass

    def save_session(self):
        meditation_log = mls("C:/Users/Matt/PycharmProjects/MeditationLog/MeditationData.db")

        session_end = self.session_begin + timedelta(seconds=self.session_length)

        # ToDo: Create a notes field
        session_values = (self.session_begin, session_end, "create notes field")
        meditation_log.insert_session(session_values)

        print(session_values)


root = Tk()
log = MeditationLog(root)
root.mainloop()
