def adicionar_tags_p_e_quebra_linha(letra):
    estrofes = letra.strip().split('\n\n')
    resultado = ""
    for estrofe in estrofes:
        linhas = estrofe.strip().split('\n')
        for i, linha in enumerate(linhas):
            resultado += "<p>" + linha.strip() + "</p>\n"
        resultado += "<br>\n"  
    return resultado


letra_exemplo = """
Just a castaway, an island lost at sea, oh
Another lonely day, with no one here but me, oh
More loneliness than any man could bear
Rescue me before I fall into despair, oh

I'll send an S.O.S. to the world
I'll send an S.O.S. to the world
I hope that someone gets my
I hope that someone gets my
I hope that someone gets my
Message in a bottle, yeah
Message in a bottle, yeah

A year has passed since I wrote my note
But I should have known this right from the start
Only hope can keep me together
Love can mend your life but
But love can break your heart

I'll send an S.O.S. to the world
I'll send an S.O.S. to the world
I hope that someone gets my
I hope that someone gets my
I hope that someone gets my
Message in a bottle, yeah
Message in a bottle, yeah
Message in a bottle, yeah
Message in a bottle, yeah

Walked out this morning, don't believe what I saw
Hundred billion bottles washed up on the shore
Seems I'm not alone at being alone
Hundred billion castaways, looking for a home

I'll send an S.O.S. to the world
I'll send an S.O.S. to the world
I hope that someone gets my
I hope that someone gets my
I hope that someone gets my
Message in a bottle, yeah
Message in a bottle, yeah
Message in a bottle, oh
Message in a bottle, yeah

Sending out an S.O.S.
Sending out an S.O.S.
I'm sending out an S.O.S.
I'm sending out an S.O.S.
Sending out an S.O.S.
Sending out an S.O.S.

"""
letra_formatada = adicionar_tags_p_e_quebra_linha(letra_exemplo)
print(letra_formatada)