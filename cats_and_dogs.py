import PySimpleGUI as sg
import random as r
theme = r.choice(["Dark Black1", "DarkGrey3", "DarkGreen3", "Topanga"])
sg.theme('theme')

igrac_1 = ''
igrac_2 = ''
broj_partija = ''


def layout_first():
    layout = [[sg.Text('Igrač 1: '), sg.InputText(igrac_1)],
              [sg.Text('Igrač 2: '), sg.InputText(igrac_2)],
              [sg.Text('Broj partija: '), sg.InputText(broj_partija)],
              [sg.Button('KRENI', key='go')]]
    return layout


win = sg.Window('Igrači', layout_first())
klik = True
while True:
    e, v = win.read()
    if e == sg.WIN_CLOSED:
        igrac_1 = ''
        igrac_2 = ''
        klik = False
        broj_partija = 0
        win.close()
        break
    if e == 'go':
        igrac_1 = v[0]
        igrac_2 = v[1]
        broj_partija = v[2]
        while True:
            if v[2] == None:
                break
            elif v[2] == '0':
                broj_partija = ''
                win.close()
                win = sg.Window('Igrači', layout_first())
                while True:
                    e, v = win.read()
                    if e == sg.WIN_CLOSED:
                        igrac_1 = ''
                        igrac_2 = ''
                        klik = False
                        broj_partija = 0
                        win.close()
                        break
                    if e == 'go':
                        igrac_1 = v[0]
                        igrac_2 = v[1]
                        broj_partija = v[2]
                        while True:
                            try:
                                broj_partija = abs(int(v[2]))
                                break
                            except ValueError:
                                broj_partija = ''
                                win.close()
                                break
                            else:
                                break
                    win.close()
                    break
            elif v[2] < '0' or v[0] == '' or v[1] == '' or v[0] == v[1]:
                try:
                    broj_partija = abs(int(v[2]))
                    win.close()
                    win = sg.Window('Igrači', layout_first())
                    while True:
                        e, v = win.read()
                        if e == sg.WIN_CLOSED:
                            igrac_1 = ''
                            igrac_2 = ''
                            klik = False
                            broj_partija = 0
                            win.close()
                            break
                        if e == 'go':
                            igrac_1 = v[0]
                            igrac_2 = v[1]
                            broj_partija = v[2]
                            while True:
                                try:
                                    broj_partija = abs(int(v[2]))
                                    break
                                except ValueError:
                                    broj_partija = ''
                                    win.close()
                                    break
                                else:
                                    break
                        win.close()
                        break

                except ValueError:
                    broj_partija = ''
                    win.close()
                    win = sg.Window('Igrači', layout_first())
                    while True:
                        e, v = win.read()
                        if e == sg.WIN_CLOSED:
                            igrac_1 = ''
                            igrac_2 = ''
                            klik = False
                            broj_partija = 0
                            win.close()
                            break
                        if e == 'go':
                            igrac_1 = v[0]
                            igrac_2 = v[1]
                            broj_partija = v[2]
                            while True:
                                try:
                                    broj_partija = abs(int(v[2]))
                                    break
                                except ValueError:
                                    broj_partija = ''
                                    win.close()
                                    break
                                else:
                                    break
                        win.close()
                        break
                win.close()
                continue
            else:
                try:
                    broj_partija = abs(int(v[2]))
                    break
                except ValueError:
                    broj_partija = ''
                    win.close()
                    win = sg.Window('Igrači', layout_first())
                    while True:
                        e, v = win.read()
                        if e == sg.WIN_CLOSED:
                            igrac_1 = ''
                            igrac_2 = ''
                            klik = False
                            broj_partija = 0
                            win.close()
                            break
                        if e == 'go':
                            igrac_1 = v[0]
                            igrac_2 = v[1]
                            broj_partija = v[2]
                            while True:
                                try:
                                    broj_partija = abs(int(v[2]))
                                    break
                                except ValueError:
                                    broj_partija = ''
                                    win.close()
                                    break
                                else:
                                    break

                        win.close()
                        break

                    win.close()
                    continue
                else:
                    break

        win.close()
        break

win.close()


def layout():
    layout = [[sg.Text('Pokušaj broj: ', size=(20, 0), font=('Helvetica', 15), key='p'), sg.Text('0', size=(4, 0), font=('Helvetica', 20), key='pok')],
              [sg.Text('Točno: ', size=(20, 0), font=('Helvetica', 15), key='t'), sg.Text(
                  '0', size=(4, 0), font=('Helvetica', 20), key='toc')],
              [sg.Button('', button_color=(sg.theme_background_color(), sg.theme_background_color()),
                         image_filename="cat_button.png", image_size=(150, 150), image_subsample=4, border_width=2, key="button_cat"),
               sg.Text('ili', size=(2, 0), font=('Helvetica', 50),
                       justification='center', key='ili'),
               sg.Button('', button_color=(sg.theme_background_color(), sg.theme_background_color()),
                         image_filename="dog_button.png", image_size=(150, 150), image_subsample=4, border_width=2, key="button_dog")],
              [sg.Text('', size=(16, 0), font=('Helvetica', 30),
                       justification='center', key='odabir')],
              [sg.Text('', size=(16, 0), font=('Helvetica', 30),
                       justification='center', key='postotak')],
              [sg.Image('', size=(1, 1), key="slika")],
              [sg.Text('', text_color="", size=(12, 0), font=(
                  'Helvetica', 30), justification='center', key='rezultat')],
              [sg.Button('GOTOVO', size=(20, 2), visible=False, key='gotovo')]]
    return layout


win = sg.Window(f'{igrac_1}', layout(), element_justification='center')
cat_list = []
dog_list = []
for x in range(9):
    cat_list.append(f"cat{x+1}.png")
    dog_list.append(f"dog{x+1}.png")
r_dog_last = ""
r_cat_last = ""


def cat():
    global r_cat_last
    global cat_list
    r_cat = r.choice(cat_list)
    while True:
        if r_cat_last == r_cat:
            r_cat = r.choice(cat_list)
            continue
        else:
            break
    return [r_cat, r_cat]


def dog():
    global r_dog_last
    global dog_list
    r_dog = r.choice(dog_list)
    while True:
        if r_dog_last == r_dog:
            r_dog = r.choice(dog_list)
            continue
        else:
            break
    return [r_dog, r_dog]


postotak_last = 0
pokusaj = 0
tocno = 0
postotak = 0
while True and klik:
    e, v = win.read()
    if e == 'button_cat':
        pokusaj += 1
        win.Element('pok').Update(pokusaj)
        win.Element('toc').Update(tocno)
        win.Element('odabir').Update("CAT")
        r_cat_last, r_cat = cat()
        r_dog_last, r_dog = dog()
        random = r.choice([r_cat, r_dog])
        postotak = int(tocno / pokusaj * 100)
        win.Element('postotak').Update(f'{postotak} %')
        if random == r_cat:
            win.Element('slika').Update(random)
            win.Element('rezultat').Update("BRAVO", text_color="green")
            tocno += 1
            win.Element('toc').Update(tocno)
            postotak = int(tocno / pokusaj * 100)
            win.Element('postotak').Update(f'{postotak} %')
        else:
            win.Element('slika').Update(random)
            win.Element('rezultat').Update("KRIVO", text_color="red")
            postotak = int(tocno / pokusaj * 100)
            win.Element('postotak').Update(f'{postotak} %')
    if e == 'button_dog':
        pokusaj += 1
        win.Element('pok').Update(pokusaj)
        win.Element('toc').Update(tocno)
        win.Element('odabir').Update("DOG")
        r_cat_last, r_cat = cat()
        r_dog_last, r_dog = dog()
        random = r.choice([r_cat, r_dog])
        postotak = int(tocno / pokusaj * 100)
        win.Element('postotak').Update(f'{postotak} %')
        if random == r_dog:
            win.Element('slika').Update(random)
            win.Element('rezultat').Update("BRAVO", text_color="green")
            tocno += 1
            win.Element('toc').Update(tocno)
            postotak = int(tocno / pokusaj * 100)
            win.Element('postotak').Update(f'{postotak} %')
        else:
            win.Element('slika').Update(random)
            win.Element('rezultat').Update("KRIVO", text_color="red")
            postotak = int(tocno / pokusaj * 100)
            win.Element('postotak').Update(f'{postotak} %')

    if e == sg.WIN_CLOSED:
        klik = 0
        pokusaj = 0
        tocno = 0
        win.close()
        break

    if pokusaj == broj_partija:
        postotak_last = postotak
        win.Element('gotovo').Update(visible=True)
        win.Element('button_cat').Update(disabled=True)
        win.Element('button_dog').Update(disabled=True)

    if e == 'gotovo':
        pokusaj = 0
        tocno = 0
        win.close()
        break


win = sg.Window(f'{igrac_2}', layout(), element_justification='center')
pokusaj = 0
tocno = 0
postotak = 0
while True and klik:
    e, v = win.read()
    if e == 'button_cat':
        pokusaj += 1
        win.Element('pok').Update(pokusaj)
        win.Element('toc').Update(tocno)
        win.Element('odabir').Update("CAT")
        r_cat_last, r_cat = cat()
        r_dog_last, r_dog = dog()
        random = r.choice([r_cat, r_dog])
        postotak = int(tocno / pokusaj * 100)
        win.Element('postotak').Update(f'{postotak} %')
        if random == r_cat:
            win.Element('slika').Update(random)
            win.Element('rezultat').Update("BRAVO", text_color="green")
            tocno += 1
            win.Element('toc').Update(tocno)
            postotak = int(tocno / pokusaj * 100)
            win.Element('postotak').Update(f'{postotak} %')
        else:
            win.Element('slika').Update(random)
            win.Element('rezultat').Update("KRIVO", text_color="red")
            postotak = int(tocno / pokusaj * 100)
            win.Element('postotak').Update(f'{postotak} %')
    if e == 'button_dog':
        pokusaj += 1
        win.Element('pok').Update(pokusaj)
        win.Element('toc').Update(tocno)
        win.Element('odabir').Update("DOG")
        r_cat_last, r_cat = cat()
        r_dog_last, r_dog = dog()
        random = r.choice([r_cat, r_dog])
        postotak = int(tocno / pokusaj * 100)
        win.Element('postotak').Update(f'{postotak} %')
        if random == r_dog:
            win.Element('slika').Update(random)
            win.Element('rezultat').Update("BRAVO", text_color="green")
            tocno += 1
            win.Element('toc').Update(tocno)
            postotak = int(tocno / pokusaj * 100)
            win.Element('postotak').Update(f'{postotak} %')
        else:
            win.Element('slika').Update(random)
            win.Element('rezultat').Update("KRIVO", text_color="red")
            postotak = int(tocno / pokusaj * 100)
            win.Element('postotak').Update(f'{postotak} %')

    if e == sg.WIN_CLOSED:
        klik = 0
        pokusaj = 0
        tocno = 0
        win.close()
        break

    if pokusaj == broj_partija:
        win.Element('gotovo').Update(visible=True)
        win.Element('button_cat').Update(disabled=True)
        win.Element('button_dog').Update(disabled=True)

    if e == 'gotovo':
        pokusaj = 0
        tocno = 0
        win.close()
        break

if postotak_last > postotak:
    ispis = f'Bravo {igrac_1}!'
if postotak_last < postotak:
    ispis = f'Bravo {igrac_2}!'
if postotak_last == postotak:
    ispis = f'Izjednačeno'


layout = [[sg.Text(f'{igrac_1}: {postotak_last} %', size=(30, 0), font=('Helvetica', 50),  justification='center')],
          [sg.Text(f'{igrac_2}: {postotak} %', size=(30, 0),
                   font=('Helvetica', 50),  justification='center')],
          [sg.Text(f'{ispis}', size=(30, 0), font=('Helvetica', 50),  justification='center')]]

win = sg.Window('Rezultat', layout, element_justification='center')

while True and klik:
    e, v = win.read()
    if e == sg.WIN_CLOSED:
        win.close()
        break
