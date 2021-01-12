def making_sandwiches(name, *ingredents):
    print(f"\nSumaraize sandwiche's ({name.title()}) : ")
    
    for ingredent in ingredents:
        print(f"-. {ingredent.title()}")

making_sandwiches('martin','cheese','jam','tomato sauce')
making_sandwiches('petra', 'pepper','onions','cheese','lettuce')
making_sandwiches('maria','cheese')
making_sandwiches('juana','salmon')