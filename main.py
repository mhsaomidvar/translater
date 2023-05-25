from translate import Translator

languageName = input('enter language name: ')
translat = input('what to translate? : ')

translator = Translator(to_lang=languageName)
translation = translator.translate(translat)
print(translation)