# Importojmë bibliotekën random për zgjedhje rastësore
import random

# Importojmë biblioteken tk për krijimin e dritares
import tkinter as tk


# Krijojmë listën me aktivitete
activities = [
    'Reading',
    'Walking',
    'Gaming',
    'Watching a movie',
    'Cooking',
    'Drawing',
    'Listening to music',
    'Exercising',
    'Relaxing'
]


# Krijojmë funksionin që sugjeron një aktivitet
def suggest_activity():

    # Zgjedhim një aktivitet rastësisht nga lista
    activity = random.choice(activities)

    # Shfaqim aktivitetin e zgjedhur në dritare
    result_label.config(text='Suggested activity: ' + activity)


# Krijojmë funksionin për shtimin e aktiviteteve
def add_activity():

    # Marrim tekstin që përdoruesi ka shkruar në kuti
    new_activity = activity_entry.get()

    # Kontrollojmë nëse përdoruesi ka shkruar diçka
    if new_activity != '':

        # Shtojmë aktivitetin e ri në listë
        activities.append(new_activity)

        # Shfaqim mesazhin se aktiviteti është shtuar
        result_label.config(text='Added: ' + new_activity)

        # Fshijmë tekstin nga kutia
        activity_entry.delete(0, tk.END)

    # Nëse kutia është e zbrazët
    else:

        # Shfaqim mesazhin që të shkruhet një aktivitet
        result_label.config(text='Please enter an activity!')


# Krijojmë funksionin për numërimin e aktiviteteve
def show_activities():

    # Numërojmë sa aktivitete kemi në listë
    total = len(activities)

    # Shfaqim numrin e aktiviteteve në dritare
    result_label.config(text='Total activities: ' + str(total))


# Krijojmë dritaren kryesore
window = tk.Tk()

# Vendosim titullin e dritares
window.title('Random Activity Generator')

# Vendosim madhësinë e dritares
window.geometry('460x530')

# Vendosim ngjyrën e sfondit të dritares
window.configure(bg='#FFF7ED')

# Nuk lejojmë ndryshimin e madhësisë së dritares
window.resizable(False, False)


# Krijojmë titullin kryesor
title_label = tk.Label(
    window,
    text='Random Activity Generator',
    font=('Arial', 19, 'bold'),
    bg='#FFF7ED',
    fg='#7C3F2C'
)

# Shfaqim titullin në rreshtin e parë
title_label.grid(row=0, column=0, columnspan=3, pady=(25, 5))


# Krijojmë tekstin poshtë titullit
subtitle = tk.Label(
    window,
    text='Find something lovely to do today',
    font=('Arial', 10),
    bg='#FFF7ED',
    fg='#A4715C'
)

# Shfaqim tekstin në rreshtin e dytë
subtitle.grid(row=1, column=0, columnspan=3, pady=(0, 20))


# Ruajmë ngjyrën e kutive të aktiviteteve
card_color = '#FCE1D5'


# Kalojmë nëpër aktivitetet e listës
for i, activity in enumerate(activities):

    # Krijojmë një kuti për çdo aktivitet
    card = tk.Label(
        window,
        text=activity,
        font=('Arial', 10, 'bold'),
        bg=card_color,
        fg='#704333',
        width=17,
        height=2,
        relief='flat'
    )

    # Vendosim aktivitetet në 3 kolona
    card.grid(
        row=(i // 3) + 2,
        column=i % 3,
        padx=6,
        pady=6
    )


# Krijojmë butonin për sugjerimin e aktivitetit
button = tk.Button(
    window,
    text='Suggest an Activity',
    font=('Arial', 11, 'bold'),
    bg='#C96F4A',
    fg='white',
    command=suggest_activity
)

# Shfaqim butonin në dritare
button.grid(row=5, column=0, columnspan=3, pady=15, ipadx=18, ipady=7)


# Krijojmë tekstin që kërkon një aktivitet të ri
add_label = tk.Label(
    window,
    text='Add your own activity:',
    font=('Arial', 11),
    bg='#FFF7ED',
    fg='#704333'
)

# Shfaqim tekstin në dritare
add_label.grid(row=6, column=0, columnspan=3, pady=5)


# Krijojmë kutinë për shkrimin e aktivitetit të ri
activity_entry = tk.Entry(window, font=('Arial', 11))

# Shfaqim kutinë në dritare
activity_entry.grid(row=7, column=0, columnspan=3, pady=5)


# Krijojmë butonin Add Activity
add_button = tk.Button(
    window,
    text='Add Activity',
    font=('Arial', 10),
    bg='#FCE1D5',
    command=add_activity
)

# Shfaqim butonin Add Activity
add_button.grid(row=8, column=0, columnspan=3, pady=5)


# Krijojmë butonin Show All Activities
show_button = tk.Button(
    window,
    text='Show All Activities',
    font=('Arial', 10),
    bg='#FCE1D5',
    command=show_activities
)

# Shfaqim butonin Show All Activities
show_button.grid(row=9, column=0, columnspan=3, pady=5)



result_label = tk.Label(
    window,
    text='Your suggestion will appear here',
    font=('Arial', 11, 'bold'),
    bg='#FFF7ED',
    fg='#8B4A32',
    wraplength=400
)

# Shfaqim rezultatin në fund të dritares
result_label.grid(row=10, column=0, columnspan=3, pady=10)


# Mbajmë dritaren të hapur
window.mainloop()

