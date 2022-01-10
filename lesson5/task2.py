with open("task2_text.txt") as f:

    content = f.readlines()
    print(f"Количество строк в файле  {len(content)}")

with open("task2_text.txt") as g:
    cont_words = g.read()
    words = cont_words.split()
    print(f"количество слов в файле {len(words)}")