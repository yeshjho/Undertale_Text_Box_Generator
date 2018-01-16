from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PIL import Image
import sys
import os

number = 0
who_is_current = ''
selected_character = ''
selected_number = 0
text_cache = 0
last_letter = ''
letter_size = (0, 0)
image2 = None
is_invalid = False
hide_aster = False
main_list = ['Sans', 'Papyrus', 'Toriel', 'Flowey', 'Undyne', 'Alphys', 'MettatonEx', 'Napstablook', 'Asgore', 'Asriel',
             'Color', 'Color2', 'Color3', 'Others']
# height = 기본보다 위쪽에서 높이가 얼마나 낮은가 (높은 것도 기재함) (아래쪽에서 길거나 짧은 건 기재하지 않음)
# space = 기본보다 얼마나 폭이 오른쪽으로 넓은가 (좁은 건 기재하지 않음)
normal_height = {'a': 9, 'c': 9, 'e': 9, 'g': 9, 'i': -4, 'j': -14, 'm': 9, 'n': 9, 'o': 9, 'p': 9, 'q': 9, 'r': 9,
                 's': 9, 'u': 9, 'v': 9, 'w': 9, 'x': 9, 'y': 9, 'z': 9, '`': -5, '~': 10, '!': -4, '$': -9, '^': -4,
                 '*': 10, 'Asterisk': 10, '-': 9, '=': 9, '_': -10, '+': 9, ',': 9, ';': 9, ':': 9, 'Colon': 9}
normal_space = {'m': 5, 'w': 5, 'M': 5, 'W': 5, '~': 5, '#': 5, '%': 5, '&': 5, '*': 9, 'Asterisk': 9, '.': 27, "'": 17}
sans_height = {'a': 13, 'c': 13, 'e': 13, 'g': 13, 'm': 13, 'n': 13, 'o': 13, 'p': 13, 'q': 13, 'r': 13, 's': 13, 't': 5,
               'u': 13, 'v': 13, 'w': 13, 'x': 13, 'y': 13, 'z': 13, '$': -8, '+': 13, '=': 13, '-': 13, '^': -4,
               '`': -4, '<': 13, '>': 13, 'BracketOpen': 13, 'BracketClose': 13, '~': 13}
sans_space = {'d': 5, 'm': 9, 'w': 9, 'x': 5, 'y': 5, '2': 5, '4': 5, '7': 5, '@': 14, '#': 14, '%': 23, '&': 13,
              '_': 14, '?': 5, 'QMark': 5, '~': 5, '.': 27, "'": 17, 'l': 20, '!': 15}
papyrus_height = {}
papyrus_space = {'I': 10, '!': 15, '.': 10, ',': 20, "'": 10, '?': 15, 'QMark': 15}
gaster_height = {}
gaster_space = {}


def ShowNHideAll(self, status):
    if status == "show":
        self.FinalImage.show()
        self.Text.show()
        self.SaveButton.show()
        self.SaveSmallButton.show()
        self.ResetButton.show()
        self.NewLineSecond.show()
        self.NewLineThird.show()
        self.Warning.show()
        self.Warning_2.show()
        self.HideAster.show()

    else:
        self.FinalImage.hide()
        self.Text.hide()
        self.SaveButton.hide()
        self.SaveSmallButton.hide()
        self.ResetButton.hide()
        self.NewLineSecond.hide()
        self.NewLineThird.hide()
        self.Warning.hide()
        self.Warning_2.hide()
        self.HideAster.hide()


def IconSetting(name):
    icon_name = name.lower() + 'icon'
    tn_name = name + 'TN'

    code1 = icon_name + ' = QtGui.QIcon()'
    code2 = icon_name + '.addPixmap(QtGui.QPixmap("./Images/Thumbnail/' + name + '.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)'
    code3 = 'self.' + tn_name + '.setIcon(' + icon_name + ')'

    return code1, code2, code3


def Selected(name, self):
    global who_is_current, number
    who_is_current = name

    number = 0
    for i in range(1, 121):
        icon_name = 'tn' + str(i)
        tn_name = 'TN_' + str(i)

        path = './Images/Thumbnail/' + name + '/' + str(i) + '.png'
        code0 = "Image.open(path)"
        code1 = icon_name + ' = QtGui.QIcon()'
        code2 = icon_name + '.addPixmap(QtGui.QPixmap(path), QtGui.QIcon.Normal, QtGui.QIcon.Off)'
        code3 = 'self.' + tn_name + '.setIcon(' + icon_name + ')'
        if name == 'Napstablook':
            code4 = 'self.' + tn_name + '.resize(56, 62)'
        else:
            code4 = 'self.' + tn_name + '.resize(60, 60)'

        code = [code0, code4, code1, code2, code3]

        try:
            for j in range(5):
                exec(code[j])
            number += 1
        except:
            break

    for i in range(1, 121):
        code = 'self.TN_' + str(i) + '.hide()'
        exec(code)
    for i in range(1, number + 1):
        code = 'self.TN_' + str(i) + '.show()'
        exec(code)


def SubSelected(num, self):
    global selected_number
    global selected_character
    selected_number = num

    if who_is_current == 'Sans' or (who_is_current == 'Color2' and 0 < num < 39):
        selected_character = 'Sans'
    elif who_is_current == 'Papyrus' or (who_is_current == 'Color' and 88 < num < 112):
        selected_character = 'Papyrus'
    elif who_is_current == 'Others' and (num == 2 or num == 3):
        selected_character = 'Gaster'
    elif who_is_current == 'Others' and num == 1:
        selected_character = 'NoCharacter'
    else:
        selected_character = 'Whatever'

    if who_is_current == 'Others' and num == 1:
        new_image = Image.open('./Images/Base.png')
        new_image.save('./Images/Cache/Cache.png')
        new_image.save('./Images/Cache/CacheWOLetters.png')

        final_image = QtGui.QIcon()
        final_image.addPixmap(QtGui.QPixmap('./Images/Cache/Cache.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FinalImage.setIcon(final_image)
        self.FinalImage.setIconSize(QtCore.QSize(1300, 342))

        ShowNHideAll(self, "show")

    else:
        path = './Images/' + who_is_current + '/' + str(num) + '.png'
        character = Image.open(path)
        w, h = character.size

        if ((w + 20) > 330) | ((h + 20) > 330):
            self.ImageSizeError()

        else:
            new_image = Image.open('./Images/Base.png')
            new_image.paste(character, (20, 20, w + 20, h + 20))
            new_image.save('./Images/Cache/Cache.png')
            new_image.save('./Images/Cache/CacheWOLetters.png')

            final_image = QtGui.QIcon()
            final_image.addPixmap(QtGui.QPixmap('./Images/Cache/Cache.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.FinalImage.setIcon(final_image)
            self.FinalImage.setIconSize(QtCore.QSize(1300, 342))

            ShowNHideAll(self, "show")

    self.Text.setText('')
    self.NewLineSecond.setChecked(False)
    self.NewLineThird.setChecked(False)
    self.HideAster.setChecked(False)


def TextFunc(text, self):
    global is_invalid

    for char in text:
        if char.lower() in (
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '`', '~', '!', '@', '#', '$',
                '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', ';', ':', "'", '"', ',', '.', '<',
                '>', '/', '?', '\\', '|', ' ', '\n', ''):
            is_invalid = False
            pass

        else:
            is_invalid = True
            ShowNHideAll(self, "hide")
            for i in range(1, 121):
                code = 'self.TN_' + str(i) + '.hide()'
                exec(code)

            try:
                os.remove('./Images/Cache/Cache.png')
            except:
                pass
            try:
                os.remove('./Images/Cache/CacheWOLetters.png')
            except:
                pass

            self.Text.setText('')
            self.TextError()
            return

    if selected_character == 'Sans':
        NormalText(self, text, False, 'Sans')

    elif selected_character == 'Papyrus':
        NormalText(self, text, False, 'Papyrus')

    elif selected_character == 'NoCharacter':
        NormalText(self, text, False, 'NoCharacter')

    elif selected_character == 'Gaster':
        NormalText(self, text, False, 'WingDings')

    else:
        NormalText(self, text, False, 'Normal')


def NormalText(self, text, image3, character):
    if is_invalid:
        return

    global text_cache, last_letter, letter_size, image2

    if character == 'Papyrus' or character == 'WingDings':
        cursor = [330, 65]
    elif character == 'NoCharacter':
        cursor = [135, 65]
    else:
        cursor = [395, 65]

    current_line = 1
    i = -1
    letter_size_cache = letter_size

    if image3:
        image2 = image3
    else:
        image2 = Image.open('./Images/Cache/Cache.png')

    # 첫 줄 * 삽입
    if not hide_aster:
        if character == 'Sans':
            aster = Image.open('./Fonts/Sans/Other/Asterisk.png')
            image2.paste(aster, (395 - (aster.size[0] + 50), 65))
        elif character == 'Papyrus' or character == 'WingDings':
            pass
        elif character == 'NoCharacter':
            aster = Image.open('./Fonts/Normal/Other/Asterisk.png')
            image2.paste(aster, (135 - (aster.size[0] + 30), 75))
        else:
            aster = Image.open('./Fonts/Normal/Other/Asterisk.png')
            image2.paste(aster, (395 - (aster.size[0] + 30), 75))

    if character == 'Sans':
        text = text.lower()
    elif character == 'Papyrus':
        text = text.upper()

    for char in text:
        i += 1

        # 스페이스 바
        if char == ' ':
            if character == 'Papyrus':
                cursor[0] += 50
            else:
                cursor[0] += 40
            try:
                if character == 'Normal' or character == 'NoCharacter':
                    cursor[0] -= normal_space[text[i - 1]]
                elif character == 'Sans':
                    cursor[0] -= sans_space[text[i - 1]]
                elif character == 'Papyrus':
                    cursor[0] -= papyrus_space[text[i - 1]]
                else:
                    cursor[0] -= gaster_space[text[i - 1]]
            except:
                pass

        # 줄 바꿈
        elif char == '\n':
            current_line += 1
            if character == 'Papyrus' or character == 'WingDings':
                cursor = [330, 65]
            elif character == 'NoCharacter':
                cursor = [135, 65]
            else:
                cursor = [395, 65]

            if current_line >= 4:
                return

        # 글자들 프린팅
        elif char in (
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v',
                'w', 'x', 'y', 'z'):
            cursor, letter_size = SubText(character, 'Lower', char, current_line, cursor)

        elif char in (
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V',
                'W', 'X', 'Y', 'Z'):
            cursor, letter_size = SubText(character, 'Upper', char, current_line, cursor)

        else:
            if char == '*':
                cursor, letter_size = SubText(character, 'Other', 'Asterisk', current_line, cursor)

            elif char == '\\':
                cursor, letter_size = SubText(character, 'Other', 'BackSlash', current_line, cursor)

            elif char == '>':
                cursor, letter_size = SubText(character, 'Other', 'BracketClose', current_line, cursor)

            elif char == '<':
                cursor, letter_size = SubText(character, 'Other', 'BracketOpen', current_line, cursor)

            elif char == ':':
                cursor, letter_size = SubText(character, 'Other', 'Colon', current_line, cursor)

            elif char == '|':
                cursor, letter_size = SubText(character, 'Other', 'Pipe', current_line, cursor)

            elif char == '?':
                cursor, letter_size = SubText(character, 'Other', 'QMark', current_line, cursor)

            elif char == '/':
                cursor, letter_size = SubText(character, 'Other', 'Slash', current_line, cursor)

            elif char == '"':
                cursor, letter_size = SubText(character, 'Other', "2'", current_line, cursor)

            elif char == '':
                pass

            else:
                cursor, letter_size = SubText(character, 'Other', char, current_line, cursor)

    # 여기서부터는 글자들 전부 프린팅 한 다음에 실행

    # 백스페이스
    if text_cache - 1 == len(text):
        if last_letter != '\n':
            if current_line == 1:
                cursor[1] = 65
            elif current_line == 2:
                cursor[1] = 145
            elif current_line == 3:
                cursor[1] = 225
            try:
                if character == 'Normal' or character == 'NoCharacter':
                    cursor[1] += normal_height[last_letter]
                elif character == 'Sans':
                    cursor[1] += sans_height[last_letter]
                elif character == 'Papyrus':
                    cursor[1] += papyrus_height[last_letter]
                else:
                    cursor[1] += gaster_height[last_letter]
            except:
                pass

            black = Image.new('RGB', letter_size_cache)
            image2.paste(black, tuple(cursor))

            final_image = QtGui.QIcon()
            final_image.addPixmap(QtGui.QPixmap('./Images/Cache/Cache.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.FinalImage.setIcon(final_image)
            self.FinalImage.setIconSize(QtCore.QSize(1300, 342))

            cursor[0] += letter_size[0]

            try:
                if character == 'Normal' or character == 'NoCharacter':
                    cursor[0] += normal_space[last_letter]
                elif character == 'Sans':
                    cursor[0] += sans_space[last_letter]
                elif character == 'Papyrus':
                    cursor[0] += papyrus_space[last_letter]
                else:
                    cursor[0] += gaster_space[last_letter]
            except:
                if character == 'Papyrus':
                    cursor[0] += 5
                else:
                    cursor[0] += 10

    # 자동 줄 바꿈
    if cursor[0] + letter_size[0] > 1280:
        ind = 0

        while True:
            ind -= 1
            try:
                char = text[ind]
                if char == ' ':
                    if ind != -1:
                        text = text[:ind] + '\n' + text[ind + 1:]
                    else:
                        text = text[:ind] + '\n'
                    break

                elif char == '\n':
                    text = text[:-1] + '\n' + text[-1]
                    break

                else:
                    continue

            except:
                text = text[:-1] + '\n' + text[-1]
                break

        # 커서 위치 맨 끝으로 변경
        text_cursor = self.Text.textCursor()
        text_cursor.movePosition(QtGui.QTextCursor.End)
        self.Text.setText(text)
        self.Text.setTextCursor(text_cursor)

        # 줄 바꿈 시에 원래 윗줄에 있던 텍스트가 그대로 남아 있는 경우가 있으므로 새로 프린팅 위해 캐릭터만 있는 사진 불러옴
        image2 = Image.open('./Images/Cache/CacheWOLetters.png')
        NormalText(self, text, image2, character)

    if text != '':
        last_letter = text[-1]
    text_cache = len(text)

    image2.save('./Images/Cache/Cache.png')
    final_image = QtGui.QIcon()
    final_image.addPixmap(QtGui.QPixmap('./Images/Cache/Cache.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.FinalImage.setIcon(final_image)
    self.FinalImage.setIconSize(QtCore.QSize(1300, 342))


def SubText(path1, path2, char, current_line, cursor):
    global image2
    if path1 == 'NoCharacter':
        path1 = 'Normal'

    if current_line == 1:
        cursor[1] = 65
    elif current_line == 2:
        cursor[1] = 145
    elif current_line == 3:
        cursor[1] = 225
    try:
        if path1 == 'Normal':
            cursor[1] += normal_height[char]
        elif path1 == 'Sans':
            cursor[1] += sans_height[char]
        elif path1 == 'Papyrus':
            cursor[1] += papyrus_height[char]
        else:
            cursor[1] += gaster_height[char]
    except:
        pass

    path = './Fonts/' + path1 + '/' + path2 + '/' + char + '.png'
    letter = Image.open(path)
    size = letter.size
    image2.paste(letter, tuple(cursor))

    cursor[0] += size[0]
    try:
        if path1 == 'Normal':
            cursor[0] += normal_space[char]
        elif path1 == 'Sans':
            cursor[0] += sans_space[char]
        elif path1 == 'Papyrus':
            cursor[0] += papyrus_space[char]
        else:
            cursor[0] += gaster_space[char]
    except:
        if path1 == 'Papyrus':
            cursor[0] += 5
        else:
            cursor[0] += 10

    return cursor, size


def NewLineSecond(self, state):
    image = Image.open('./Images/Cache/Cache.png')
    image_cache = Image.open('./Images/Cache/CacheWOLetters.png')

    if state is True:
        if selected_character == 'Papyrus' or selected_character == 'Gaster':
            return

        elif selected_character == 'Sans':
            aster = Image.open('./Fonts/Sans/Other/Asterisk.png')
            image.paste(aster, (395 - (aster.size[0] + 50), 145))
            image_cache.paste(aster, (395 - (aster.size[0] + 50), 145))

        elif selected_character == 'NoCharacter':
            aster = Image.open('./Fonts/Normal/Other/Asterisk.png')
            image.paste(aster, (135 - (aster.size[0] + 30), 155))
            image_cache.paste(aster, (135 - (aster.size[0] + 30), 155))

        else:
            aster = Image.open('./Fonts/Normal/Other/Asterisk.png')
            image.paste(aster, (395 - (aster.size[0] + 30), 155))
            image_cache.paste(aster, (395 - (aster.size[0] + 30), 155))

    else:
        if selected_character == 'Papyrus' or selected_character == 'Gaster':
            return

        elif selected_character == 'Sans':
            aster = Image.open('./Fonts/Sans/Other/Asterisk.png')
            image.paste(Image.new('RGB', aster.size), (395 - (aster.size[0] + 50), 145))
            image_cache.paste(Image.new('RGB', aster.size), (395 - (aster.size[0] + 50), 145))

        elif selected_character == 'NoCharacter':
            aster = Image.open('./Fonts/Normal/Other/Asterisk.png')
            image.paste(Image.new('RGB', aster.size), (135 - (aster.size[0] + 30), 155))
            image_cache.paste(Image.new('RGB', aster.size), (135 - (aster.size[0] + 30), 155))

        else:
            aster = Image.open('./Fonts/Normal/Other/Asterisk.png')
            image.paste(Image.new('RGB', aster.size), (395 - (aster.size[0] + 30), 155))
            image_cache.paste(Image.new('RGB', aster.size), (395 - (aster.size[0] + 30), 155))

    image.save('./Images/Cache/Cache.png')
    image_cache.save('./Images/Cache/CacheWOLetters.png')
    final_image = QtGui.QIcon()
    final_image.addPixmap(QtGui.QPixmap('./Images/Cache/Cache.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.FinalImage.setIcon(final_image)
    self.FinalImage.setIconSize(QtCore.QSize(1300, 342))


def NewLineThird(self, state):
    image = Image.open('./Images/Cache/Cache.png')
    image_cache = Image.open('./Images/Cache/CacheWOLetters.png')

    if state is True:
        if selected_character == 'Papyrus' or selected_character == 'Gaster':
            return

        elif selected_character == 'Sans':
            aster = Image.open('./Fonts/Sans/Other/Asterisk.png')
            image.paste(aster, (395 - (aster.size[0] + 50), 225))
            image_cache.paste(aster, (395 - (aster.size[0] + 50), 225))

        elif selected_character == 'NoCharacter':
            aster = Image.open('./Fonts/Normal/Other/Asterisk.png')
            image.paste(aster, (135 - (aster.size[0] + 30), 235))
            image_cache.paste(aster, (135 - (aster.size[0] + 30), 235))

        else:
            aster = Image.open('./Fonts/Normal/Other/Asterisk.png')
            image.paste(aster, (395 - (aster.size[0] + 30), 235))
            image_cache.paste(aster, (395 - (aster.size[0] + 30), 235))

    else:
        if selected_character == 'Papyrus' or selected_character == 'Gaster':
            return

        elif selected_character == 'Sans':
            aster = Image.open('./Fonts/Sans/Other/Asterisk.png')
            image.paste(Image.new('RGB', aster.size), (395 - (aster.size[0] + 50), 225))
            image_cache.paste(Image.new('RGB', aster.size), (395 - (aster.size[0] + 50), 225))

        elif selected_character == 'NoCharacter':
            aster = Image.open('./Fonts/Normal/Other/Asterisk.png')
            image.paste(Image.new('RGB', aster.size), (135 - (aster.size[0] + 30), 235))
            image_cache.paste(Image.new('RGB', aster.size), (135 - (aster.size[0] + 30), 235))

        else:
            aster = Image.open('./Fonts/Normal/Other/Asterisk.png')
            image.paste(Image.new('RGB', aster.size), (395 - (aster.size[0] + 30), 235))
            image_cache.paste(Image.new('RGB', aster.size), (395 - (aster.size[0] + 30), 235))

    image.save('./Images/Cache/Cache.png')
    image_cache.save('./Images/Cache/CacheWOLetters.png')
    final_image = QtGui.QIcon()
    final_image.addPixmap(QtGui.QPixmap('./Images/Cache/Cache.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.FinalImage.setIcon(final_image)
    self.FinalImage.setIconSize(QtCore.QSize(1300, 342))


def HideAster(self, state):
    image = Image.open('./Images/Cache/Cache.png')
    image_cache = Image.open('./Images/Cache/CacheWOLetters.png')
    global hide_aster

    if state is False:
        hide_aster = False
        if selected_character == 'Papyrus' or selected_character == 'Gaster':
            return

        elif selected_character == 'Sans':
            aster = Image.open('./Fonts/Sans/Other/Asterisk.png')
            image.paste(aster, (395 - (aster.size[0] + 50), 65))
            image_cache.paste(aster, (395 - (aster.size[0] + 50), 65))

        elif selected_character == 'NoCharacter':
            aster = Image.open('./Fonts/Normal/Other/Asterisk.png')
            image.paste(aster, (135 - (aster.size[0] + 30), 75))
            image_cache.paste(aster, (135 - (aster.size[0] + 30), 75))

        else:
            aster = Image.open('./Fonts/Normal/Other/Asterisk.png')
            image.paste(aster, (395 - (aster.size[0] + 30), 75))
            image_cache.paste(aster, (395 - (aster.size[0] + 30), 75))

    else:
        hide_aster = True
        if selected_character == 'Papyrus' or selected_character == 'Gaster':
            return

        elif selected_character == 'Sans':
            aster = Image.open('./Fonts/Sans/Other/Asterisk.png')
            image.paste(Image.new('RGB', aster.size), (395 - (aster.size[0] + 50), 65))
            image_cache.paste(Image.new('RGB', aster.size), (395 - (aster.size[0] + 50), 65))

        elif selected_character == 'NoCharacter':
            aster = Image.open('./Fonts/Normal/Other/Asterisk.png')
            image.paste(Image.new('RGB', aster.size), (135 - (aster.size[0] + 30), 75))
            image_cache.paste(Image.new('RGB', aster.size), (135 - (aster.size[0] + 30), 75))

        else:
            aster = Image.open('./Fonts/Normal/Other/Asterisk.png')
            image.paste(Image.new('RGB', aster.size), (395 - (aster.size[0] + 30), 75))
            image_cache.paste(Image.new('RGB', aster.size), (395 - (aster.size[0] + 30), 75))

    image.save('./Images/Cache/Cache.png')
    image_cache.save('./Images/Cache/CacheWOLetters.png')
    final_image = QtGui.QIcon()
    final_image.addPixmap(QtGui.QPixmap('./Images/Cache/Cache.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.FinalImage.setIcon(final_image)
    self.FinalImage.setIconSize(QtCore.QSize(1300, 342))


class MainWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("GUI.ui", self)
        self.ui.show()

        self.error_window = None
        self.error_window2 = None
        self.error_window3 = None

        for i in range(1, 121):
            code = 'self.TN_' + str(i) + '.clicked.connect(self.TN' + str(i) + '_Pushed)'
            exec(code)

        # 아이콘 세팅
        for i in range(14):
            for j in range(3):
                exec(IconSetting(main_list[i])[j])

        custom_tn_icon = QtGui.QIcon()
        custom_tn_icon.addPixmap(QtGui.QPixmap("./Images/Thumbnail/Custom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CustomTN.setIcon(custom_tn_icon)
        self.Custom2TN.setIcon(custom_tn_icon)

        # 아이콘 세팅 끝
        # 버튼 및 텍스트 상자 숨기기
        ShowNHideAll(self, "hide")
        for i in range(1, 121):
            code = 'self.TN_' + str(i) + '.hide()'
            exec(code)

            # 버튼 및 텍스트 상자 숨기기 끝

    # 에러
    def ImageSizeError(self):
        if self.error_window is None:
            self.error_window = ErrorWindow(self)
        self.error_window.show()

    def TextError(self):
        if self.error_window2 is None:
            self.error_window2 = ErrorWindow2(self)
        self.error_window2.show()

    def UnknownError(self, code):
        if self.error_window3 is None:
            self.error_window3 = ErrorWindow3(self)
        self.error_window3.show()
        code = 'Error Code - ' + code
        self.error_window3.ErrorCode.setText(code)

    # 에러 끝
    # 메인 버튼 클릭 이벤트
    for i in main_list:
        code1 = "def " + i + "_Selected(self):\n"
        code2 = "   Selected('" + i + "', self)"
        exec(code1 + code2)

    def Custom_Selected(self):
        Selected('Custom', self)

    def Custom2_Selected(self):
        Selected('Custom2', self)

    # 메인 버튼 클릭 이벤트 끝
    # 부가 버튼 클릭 이벤트
    for i in range(1, 121):
        code1 = "def TN" + str(i) + "_Pushed(self):\n"
        code2 = "   SubSelected(" + str(i) + ", self)"
        exec(code1 + code2)

    # 부가 버튼 클릭 이벤트 끝
    # 저장 및 리셋
    def Save_Pushed(self):
        path = QtWidgets.QFileDialog.getSaveFileName(self, 'Save Image', 'C:\\Users\\user\\Desktop\\', 'Images(*.png)')
        image = Image.open('./Images/Cache/Cache.png')
        try:
            image.save(path)
        except:
            pass

    def SaveSmall_Pushed(self):
        path = QtWidgets.QFileDialog.getSaveFileName(self, 'Save Image', 'C:\\Users\\user\\Desktop\\', 'Images(*.png)')
        image = Image.open('./Images/Cache/Cache.png').resize((578, 152))
        try:
            image.save(path)
        except:
            pass

    def Reset_Pushed(self):
        ShowNHideAll(self, "hide")
        for i in range(1, 121):
            code = 'self.TN_' + str(i) + '.hide()'
            exec(code)
        self.Text.setText('')
        try:
            os.remove('./Images/Cache/Cache.png')
        except:
            pass
        try:
            os.remove('./Images/Cache/CacheWOLetters.png')
        except:
            pass

    # 저장 및 리셋 끝
    # 텍스트 변경 및 * 삽입 체크박스
    def Text_Changed(self):
        text = self.Text.toPlainText()
        TextFunc(text, self)

    def NewLineSecond_Changed(self):
        NewLineSecond(self, self.NewLineSecond.isChecked())

    def NewLineThird_Changed(self):
        NewLineThird(self, self.NewLineThird.isChecked())

    def HideAster_Changed(self):
        HideAster(self, self.HideAster.isChecked())

        # 텍스트 변경 및 * 삽입 체크박스 끝


# 에러 클래스
class ErrorWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("ImageError.ui", self)


class ErrorWindow2(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("TextError.ui", self)


class ErrorWindow3(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("UnknownError.ui", self)


# 에러 클래스 끝
# GUI 실행
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = MainWindow(None)
    p = Window.palette()
    p.setColor(Window.backgroundRole(), QtGui.QColor(0, 0, 0))
    Window.setPalette(p)
    Window.show()
    app.exec_()

# GUI 실행 끝
# 캐시 제거
try:
    os.remove('./Images/Cache/Cache.png')
except:
    pass
try:
    os.remove('./Images/Cache/CacheWOLetters.png')
except:
    pass

# 캐시 제거 끝
