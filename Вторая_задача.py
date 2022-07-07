from translate import Translator

def translate_ru():
    translator = Translator(to_lang='ru')
    user_input = input()
    ru_translate = translator.translate(user_input)
    return ru_translate

print(translate_ru())