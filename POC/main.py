import openai, os

class Modules:

    def clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system("clear")

class Variables:

    global key

    key = "YOUR KEY"
    openai.api_key = key


class AI:

    def main():
        try:
            while True:
                Modules.clear()
                prompt = input('➜ ')
                response = openai.Completion.create(
                    engine='text-davinci-003',
                    prompt=prompt, temperature=0.1,
                    top_p=1,
                    max_tokens=4000
                )
                print(response.choices[0].text)
                input("")

        except SyntaxError:
            print("[ DEBUG ] Err, ", SyntaxError)


AI.main()
