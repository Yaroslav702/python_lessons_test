from googletrans import Translator

translator = Translator()

to_translate = "我们都想在作业上打 10 分！"

a = translator.translate(text=to_translate, dest='EN')
print(a.text)

# print(a)