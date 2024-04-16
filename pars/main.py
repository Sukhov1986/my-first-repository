from parsers import Parser


def main():
    for count in range(1, 50):
        pars = Parser(f'https://habr.com/ru/articles/page{count}/', 'data.json')
        pars.run()


if __name__ == '__main__':
    main()
