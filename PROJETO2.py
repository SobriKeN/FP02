# 'O Prado' made by Fábio Sobrinho
# Utilizador:ist1103473

# Funções auxiliares

def zero(x):
    return abs(x) < 0.00000000000000001  # Devolve True se o numero é 0


###############
# TAD posicao #
###############

# Construtores

def cria_posicao(x, y):
    """
    cria_posicao: int,int -> posicao
    Esta função recebe dois numeros inteiros positivos correspondentes as coordenadas x e y do prado e devolve a posicao
    correspondente a essas coordenadas, levantando erro se um dos argumentos não for numero ou um dos argumentos for um
    numero negativo.
    """
    # Verificação de argumentos: ambas as componentes tem que ser um numero inteiro positivo
    if type(x) != int or type(y) != int or x < 0 or y < 0:
        raise ValueError('cria_posicao: argumentos invalidos')
    return x, y


def cria_copia_posicao(posicao):
    """
    cria_copia_posicao: posicao -> posicao
    Esta função recebe uma posicao de coordenadas x e y e devolve um copia nova do prado.
    """
    return tuple(list(posicao).copy())


# Seletores

def obter_pos_x(posicao):
    """
    obter_pos_x: posicao -> int
    Esta função recebe uma posicao de coordenadas x e y e devolve a componente x (linha) da posicao
    """
    return posicao[0]


def obter_pos_y(posicao):
    """
    obter_pos_y: posicao -> int
    Esta função recebe uma posicao de coordenadas x e y e devolve a componente y (coluna) da posicao
    """
    return posicao[1]


# Reconhecedor

def eh_posicao(argumento):
    """
    eh_posicao: univeral -> booleano
    Esta função recebe um argumento de qualquer tipo e devolve True se corresponder a um TAD posicao e False caso
    contrario.
    """
    # Verificar se é um TAD posicao: um tuplo de dois numeros inteiros positivos
    return type(argumento) == tuple and len(argumento) == 2 and type(obter_pos_x(argumento)) == int \
           and type(obter_pos_y(argumento)) == int and obter_pos_x(argumento) >= 0 and obter_pos_y(argumento) >= 0


# Teste

def posicoes_iguais(posicao1, posicao2):
    """
    posicoes_iguais: posicao,posicao -> booleano
    Esta função recebe duas posicoes e devolve True se as posicoes forem iguais.
    """
    # Verificar se ambas as posicoes sao iguais
    return zero(obter_pos_x(posicao1) - obter_pos_x(posicao2)) and zero(obter_pos_y(posicao1) - obter_pos_y(posicao2))


# Transformador

def posicao_para_str(posicao):
    """
    posicao_para_str: posicao -> str
    Esta função recebe uma posicao e devolve uma cadeia de caracteres correspondente a essa posição.
    """
    return str(posicao)


# Alto nivel

def obter_posicoes_adjacentes(posicao):
    """
    obter_posicoes_adjacentes: posicao -> tuplo
    Esta função recebe uma posicao e os tuplos correspondentes as posições adjacentes da posicao original(cima, baixo,
    esquerda e direita) dando-as por sentido dos ponteiros do relógio.
    """
    # Descoberta das posicoes adjacentes
    adjacente_cima = (obter_pos_x(posicao), obter_pos_y(posicao) - 1)
    adjacente_direita = (obter_pos_x(posicao) + 1, obter_pos_y(posicao))
    adjacente_baixo = (obter_pos_x(posicao), obter_pos_y(posicao) + 1)
    adjacente_esquerda = (obter_pos_x(posicao) - 1, obter_pos_y(posicao))

    # Criar uma lista com essas posicoes e verificar se elas sao TAD posicao. Se não, são eliminadas da lista
    lista_adjacentes = [adjacente_cima, adjacente_direita, adjacente_baixo, adjacente_esquerda]
    for i in range(len(lista_adjacentes) - 1, -1, -1):
        if not eh_posicao(lista_adjacentes[i]):
            del lista_adjacentes[i]

    # Devolver o resultado em forma de tuplo
    return tuple(lista_adjacentes)


def ordenar_posicoes(tuplo_posicoes):
    """
    ordenar_posicoes: tuplo -> tuplo
    Esta função recebe um tuplo com posicoes e ordena-o seguindo as regras da ordem de leitura do prado.
    """
    # Transfromação do tuplo para lista para organizar a lista
    lista_posicoes = list(tuplo_posicoes)
    t = len(lista_posicoes)

    # Organizar a lista através de bubble sort, verificando primeiro as componentes y e depois as componentes x
    while t > 0:
        for i in range(0, len(lista_posicoes) - 1):
            if obter_pos_y(lista_posicoes[i]) > obter_pos_y(lista_posicoes[i + 1]):
                lista_posicoes[i], lista_posicoes[i + 1] = lista_posicoes[i + 1], lista_posicoes[i]
            if obter_pos_y(lista_posicoes[i]) == obter_pos_y(lista_posicoes[i + 1]):
                if obter_pos_x(lista_posicoes[i]) > obter_pos_x(lista_posicoes[i + 1]):
                    lista_posicoes[i], lista_posicoes[i + 1] = lista_posicoes[i + 1], lista_posicoes[i]
        t -= 1

    # Devolver o resultado em forma de tuplo
    return tuple(lista_posicoes)


################
#  TAD animal  #
################

# Construtores

def cria_animal(s, r, a):
    """
    cria_animal: string,int,int -> animal
    Esta função recebe uma cadeia de caracteres significando a espécie do animal e dois numeros inteiros: um para a
    frequencia de reproducao(maior que 0) e a frequencia de alimentacao(maior ou igual que 0) e devolve o animal,
    levantando erro se não seguir de acordo com as instruçoes dadas.
    """
    if type(s) != str or len(s) == 0 or type(r) != int or type(a) != int or r <= 0 or a < 0:
        raise ValueError('cria_animal: argumentos invalidos')

    # Se a for maior que 0, é predador e terá valores para fome e frequancia de alimentação. Se não, é presa e não terá
    # esses valores.
    if a > 0:
        return {'especie': s, 'idade': 0, 'freq_rep': r, 'fome': 0, 'freq_ali': a}
    else:
        return {'especie': s, 'idade': 0, 'freq_rep': r, 'fome': 0, 'freq_ali': 0}


def cria_copia_animal(animal):
    """
    cria_copia_animal: animal -> animal
    Esta função recebe um animal e devolve uma copia dessse animal.
    """
    return animal.copy()


# Seletores

def obter_especie(animal):
    """
    obter_especie: animal -> string
    Esta função recebe o animal e devolve a espécie dele.
    """
    return animal['especie']


def obter_freq_reproducao(animal):
    """
    obter_freq_reproducao: animal -> int
    Esta função recebe o animal e devolve a frequencia de reproducao dele.
    """
    return animal['freq_rep']


def obter_freq_alimentacao(animal):
    """
    obter_freq_reproducao: animal -> int
    Esta função recebe o animal e devolve a frequencia de alimentacao dele.
    """
    return animal['freq_ali']


def obter_idade(animal):
    """
    obter_idade: animal -> int
    Esta função recebe o animal e devolve a idade dele.
    """
    return animal['idade']


def obter_fome(animal):
    """
    obter_fome: animal -> int
    Esta função recebe o animal e devolve a fome dele.
    """
    return animal['fome']


# Modificadores

def aumenta_idade(animal):
    """
    aumenta_idade: animal -> animal
    Esta função recebe um animal e incrementa o valor da idade por uma unidade, devolvendo o animal incrementado.
    """
    animal.update({'idade': obter_idade(animal) + 1})
    return animal


def reset_idade(animal):
    """
    reset_idade: animal -> animal
    Esta função recebe um animal e devolve um animal com idade 0.
    """
    animal.update({'idade': 0})
    return animal


def aumenta_fome(animal):
    """
    aumenta_fome: animal -> animal
    Esta função recebe um animal e incrementa o valor da fome por uma unidade, devolvendo o animal incrementado, nao
    mudando os animais presa.
    """
    # Para ser presa, freq_alimentacao = 0
    if obter_freq_alimentacao(animal) == 0:
        return animal
    else:
        animal.update({'fome': obter_fome(animal) + 1})
        return animal


def reset_fome(animal):
    """
    reset_fome: animal -> animal
    Esta função recebe um animal e devolve um animal com fome 0 nao mudando os animais presa.
    """
    # Para ser presa, freq_alimentacao = 0
    if obter_freq_alimentacao(animal) == 0:
        return animal
    else:
        animal.update({'fome': 0})
        return animal


# Reconhecedores

def eh_animal(arg):
    """
    eh_animal: universal -> booleano
    Esta função recebe um argumento de qualquer tipo e devolve True apenas se for um TAD animal, devolvendo False caso
    contrário.
    """
    # Para ser TAD animal, precisa de ser um dicionário com 5 chaves(especie,idade,freq_rep,fome,freq_ali) onde os
    # valores tem que ser respetivamente uma cadeia de caracteres, 0, um inteiro maior que 0, 0 e um inteiro maior ou
    # igual que 0
    return type(arg) == dict and len(arg) == 5 and 'especie' in arg and 'idade' in arg and 'freq_rep' in arg and \
           'fome' in arg and 'freq_ali' in arg and type(obter_especie(arg)) == str and \
           type(obter_freq_reproducao(arg)) == int and type(obter_freq_alimentacao(arg)) == int and \
           obter_idade(arg) >= 0 and obter_freq_reproducao(arg) > 0 and obter_fome(arg) >= 0 and \
           obter_freq_alimentacao(arg) >= 0


def eh_predador(arg):
    """
    eh_predador: universal -> booleano
    Esta função recebe um argumento de qualquer tipo e devolve True apenas se for um TAD animal que seja predador,
    devolvendo False caso contrário.
    """
    # Já que se tem eh_animal feito, para ser predador tem que ter as mesmas caracteristicas e frequencia de alimentacao
    # maior que 0
    return eh_animal(arg) and obter_freq_alimentacao(arg) > 0


def eh_presa(arg):
    """
    eh_presa: universal -> booleano
    Esta função recebe um argumento de qualquer tipo e devolve True apenas se for um TAD animal que seja presa,
    devolvendo False caso contrário.
    """
    # Já que se tem eh_animal feito, para ser presa tem que ter as mesmas caracteristicas exceto freq_ali, que é 0
    return eh_animal(arg) and obter_freq_alimentacao(arg) == 0


# Teste

def animais_iguais(ani1, ani2):
    """
    animais_iguais: animal,animal -> booleano
    Esta função recebe dois animais e devolve True se forem exatamente iguais, devolvendo False caso contrário.
    """
    if eh_presa(ani1) and eh_presa(ani2):
        return obter_especie(ani1) == obter_especie(ani2) and zero(obter_idade(ani1) - obter_idade(ani2)) and \
               zero(obter_freq_reproducao(ani1) - obter_freq_reproducao(ani2))
    elif eh_predador(ani1) and eh_predador(ani2):
        return obter_especie(ani1) == obter_especie(ani2) and zero(obter_idade(ani1) - obter_idade(ani2)) and \
               zero(obter_freq_reproducao(ani1) - obter_freq_reproducao(ani2)) and \
               zero(obter_fome(ani1) - obter_fome(ani2)) and \
               zero(obter_freq_alimentacao(ani1) - obter_freq_alimentacao(ani2))
    return False


# Transformadores

def animal_para_char(animal):
    """
    animais_para_char: animal -> str
    Esta função recebe um animal e devolve uma cadeia de caracteres que significa o primeiro caracter da especie. É
    minuscula se for uma presa e maicula se for um predador.
    """
    # Se for predador, devolve uma letra maiscula. Se não, devolve uma letra minuscula
    if eh_predador(animal):
        return str(obter_especie(animal)[0].upper())
    if eh_presa(animal):
        return str(obter_especie(animal)[0])


def animal_para_str(animal):
    """
    animal_para_str: animal -> str
    Esta função recebe um animal e devolve a string do animal da seguinte maneira:
    'especie [idade/freq_rep][fome/freq_ali]' se for predador e 'especie [idade/freq_rep]' se for presa.
    """
    # Preencher a informação da maneira dada através de .format
    if eh_predador(animal):
        return '{} [{}/{};{}/{}]'.format(obter_especie(animal), obter_idade(animal),
                                         obter_freq_reproducao(animal),
                                         obter_fome(animal), obter_freq_alimentacao(animal))
    if eh_presa(animal):
        return '{} [{}/{}]'.format(obter_especie(animal), obter_idade(animal), obter_freq_reproducao(animal))


# Alto nivel

def eh_animal_fertil(animal):
    """
    eh_animal_fertil: animal -> booleano
    Esta função recebe um animal e devolve True apenas se o animal tenha passado a idade de reprodução (ou seja, a
    idade do animal e maior do que a frequencia de reproducao do animal), devolvendo False caso contrário
    """
    return zero(obter_idade(animal) - obter_freq_reproducao(animal))


def eh_animal_faminto(animal):
    """
    eh_animal_faminto: animal -> booleano
    Esta função recebe um animal e devolve True apenas se o animal tenha passado a idade de alimentação (ou seja, a
    fome do animal e maior do que a frequencia de alimentacao do animal), devolvendo False caso contrário. As presas
    dão sempre False.
    """
    if eh_presa(animal):
        return False
    else:
        return zero(obter_fome(animal) - obter_freq_alimentacao(animal))


def reproduz_animal(animal):
    """
    reproduz_animal: animal -> animal
    Esta função recebe um animal e devolve um animal da mesma especie, com fome e idade igual a 0. O animal passado
    também sofre mudanças, sendo que a idade dele volta a ser 0 quando reproduz.
    """
    # Para cada uma das especies, cria um novo animal com as caracteristicas do anterior, com fome e
    # idade igual a 0 e o animal original volta a ter idade 0 (para isso, usa-se reset_idade)
    if eh_presa(animal):
        animal_novo = cria_animal(obter_especie(animal), obter_freq_reproducao(animal), 0)
        reset_idade(animal)
        return animal_novo
    if eh_predador(animal):
        animal_novo = cria_animal(obter_especie(animal), obter_freq_reproducao(animal),
                                  obter_freq_alimentacao(animal))
        reset_idade(animal)
        return animal_novo


#############
# TAD prado #
#############

# Construtores

def cria_prado(d, r, a, p):
    """
    cria_prado: posicao,tuplo,tuplo,tuplo -> prado
    Esta função recebe quatro argumentos:
    d:posição que ocupa a montanha do canto inferior direito do prado (por outras palavras, a dimensão do prado)
    r:tuplo de 0 ou mais posições que correspondem aos rochedos (sitios onde não se pode movimentar que não sejam
    montanhas)
    a:tuplo de 1 ou mais animais
    p:tuplo da mesma dimensão que a, representa as posições dos animais
    Isto devolve um prado, representando o mapa e os animais presentes.
    """
    # Verificação de argumentos
    if not eh_posicao(d): raise ValueError('cria_prado: argumentos invalidos')
    if type(r) != tuple: raise ValueError('cria_prado: argumentos invalidos')
    i = 0
    while i < len(r):
        if not eh_posicao(r[i]): raise ValueError('cria_prado: argumentos invalidos')
        if r[i][0] <= 0 or r[i][0] >= d[0]: raise ValueError('cria_prado: argumentos invalidos')
        if r[i][1] <= 0 or r[i][1] >= d[1]: raise ValueError('cria_prado: argumentos invalidos')
        i += 1
    if type(a) != tuple: raise ValueError('cria_prado: argumentos invalidos')
    if len(a) < 1: raise ValueError('cria_prado: argumentos invalidos')
    for e in range(len(a)):
        if not eh_animal(a[e]): raise ValueError('cria_prado: argumentos invalidos')
    if type(p) != tuple: raise ValueError('cria_prado: argumentos invalidos')
    if len(p) != len(a): raise ValueError('cria_prado: argumentos invalidos')
    for n in range(len(p)):
        if not eh_posicao(p[n]): raise ValueError('cria_prado: argumentos invalidos')
    # Devolução em forma de dicionário
    return {'dim': {'x': d[0], 'y': d[1]}, 'rochas': r, 'animais': a, 'posicoes': p}


def cria_copia_prado(prado):
    """
    cria_copia_prado: prado -> prado
    Esta função recebe um prado e devolve uma cópia desse prado.
    """
    prado_copia = prado.copy()
    return prado_copia


# Seletores

def obter_tamanho_x(prado):
    """
    cria_copia_prado: prado -> inteiro
    Esta função recebe um prado e devolve a dimensão x do prado.
    """
    return int(prado['dim']['x']) + 1


def obter_tamanho_y(prado):
    """
    cria_copia_prado: prado -> inteiro
    Esta função recebe um prado e devolve a dimensão y do prado.
    """
    return int(prado['dim']['y']) + 1


def obter_numero_predadores(prado):
    """
    obter_numero_predadores: prado -> inteiro
    Esta função recebe um prado e devolve o numero de predadores dentro do prado.
    """
    # Verificar a lista que contem os animais. Se predadores, contador aumenta para 1.
    c = 0
    for i in range(0, len(prado['animais'])):
        if eh_predador(prado['animais'][i]):
            c += 1
    return c


def obter_numero_presas(prado):
    """
    obter_numero_presas: prado -> inteiro
    Esta função recebe um prado e devolve o numero de presas dentro do prado.
    """
    # Verificar a lista que contem os animais. Se presas, contador aumenta para 1.
    c = 0
    for i in range(0, len(prado['animais'])):
        if eh_presa(prado['animais'][i]):
            c += 1
    return c


def obter_posicao_animais(prado):
    """
    obter_numero_presas: prado -> tuplo posicoes
    Esta função recebe um prado e devolve as posicoes de cada animal, ordenada de acordo com o prado.
    """
    return ordenar_posicoes(prado['posicoes'])


def obter_animal(prado, posicao):
    """
    obter_animal: prado,posicao -> animal
    Esta função recebe um prado e uma posicao corresponde ao animal e devolve o animal que esta nessa posicao.
    """
    for i in range(len(prado['posicoes'])):
        if posicoes_iguais(prado['posicoes'][i], posicao):
            return prado['animais'][i]


# Modificadores

def eliminar_animal(prado, posicao):
    """
    eliminar_animal: prado,posicao -> prado
    Esta função recebe o prado e uma posicao correspondente a um animal e irá eliminar o animal como tambem a posicao.
    """
    # Como tuplo e imutavel, transformar em lista para modificar destrutivamente. Após eliminar, voltar para tuplo.
    list_pos = list(prado['posicoes'])
    list_ani = list(prado['animais'])
    list_ani.remove(obter_animal(prado, posicao))
    list_pos.remove(posicao)
    prado['posicoes'] = tuple(list_pos)
    prado['animais'] = tuple(list_ani)
    return prado


def mover_animal(prado, p1, p2):
    """
    eliminar_animal: prado,posicao,posicao -> prado
    Esta função recebe o prado e duas posicoes e ira devolver o prado onde o animal se move da primeira posicao para a
    segunda posicao, eliminando a primeira
    """
    list_pos = list(prado['posicoes'])
    for i in range(len(prado['posicoes'])):
        if posicoes_iguais(list_pos[i], p1):
            list_pos[i] = p2
            prado['posicoes'] = tuple(list_pos)
            return prado


def inserir_animal(prado, animal, posicao):
    """
    inserir_animal: prado,animal,posicao -> prado
    Esta função recebe o prado, um animal e uma posicao correspondente a esse animal e irá devolver o prado atualizado
    com os novos animais e posicoes.
    """
    list_ani = list(prado['animais'])
    list_pos = list(prado['posicoes'])
    list_ani.append(animal)
    list_pos.append(posicao)
    prado['animais'] = tuple(list_ani)
    prado['posicoes'] = tuple(list_pos)
    return prado


# Reconhecedores

def eh_prado(arg):
    """
    eh_prado: univeral -> booleano
    Esta função recebe um argumento de qualquer tipo e devolve True se corresponder a um TAD prado, devolvendo False
    caso contrario.
    """
    if (type(arg) == dict and len(arg) == 4 and 'dim' in arg and 'rochas' in arg and 'animais' in arg and
            'posicoes' in arg and 'x' in arg['dim'] and 'y' in arg['dim'] and type(obter_tamanho_x(arg)) == int and
            type(obter_tamanho_y(arg)) == int and obter_tamanho_x(arg) > 0 and obter_tamanho_y(arg) > 0 and
            type(arg['rochas']) == tuple and [eh_posicao([i]) and
                                              0 < obter_pos_x([i]) < obter_tamanho_x(arg) and 0 < obter_pos_y(
                [i]) < obter_tamanho_y(arg)
                                              for i in list(arg['rochas'])] and type(arg['animais']) == tuple and len(
                arg['animais']) >= 1 and
            [eh_animal([i]) for i in list(arg['animais'])] and type(arg['posicoes']) == tuple and
            len(arg['posicoes']) == len(arg['animais']) and [eh_posicao(i) for i in list(arg['posicoes'])]):
        return True
    return False


def eh_posicao_animal(prado, posicao):
    """
    eh_posicao_animal: prado, posicao -> booleano
    Esta função recebe o prado e uma posicao e devolve True se existir algum animal nessa posicao
    """
    return eh_prado(prado) and posicao in prado['posicoes']


def eh_posicao_obstaculo(prado, posicao):
    """
    eh_posicao_obstaculo: prado, posicao -> booleano
    Esta função recebe o prado e uma posicao e devolve True se existir algum obstaculo nessa posicao
    """
    return eh_prado(prado) and (posicao in prado['rochas'] or obter_pos_x(posicao) == 0 or
                                obter_pos_x(posicao) == obter_tamanho_x(prado)-1 or obter_pos_y(posicao) == 0 or
                                obter_pos_y(posicao) == obter_tamanho_y(prado)-1)


def eh_posicao_livre(prado, posicao):
    """
    eh_posicao_livre: prado, posicao -> booleano
    Esta função recebe o prado e uma posicao e devolve True se não existir nada nessa posicao.
    """
    if obter_pos_x(posicao) == 0 or obter_pos_x(posicao) == obter_tamanho_x(prado)-1:
        return False
    if obter_pos_y(posicao) == 0 or obter_pos_y(posicao) == obter_tamanho_y(prado)-1:
        return False
    return eh_prado(prado) and posicao not in prado['rochas'] and posicao not in prado['posicoes']


# Teste

def prados_iguais(prado1, prado2):
    """
    prados_iguais: prado, prado -> booleano
    Esta função recebe dois prados e devolve True se tiverem as mesmas caracteristicas.
    """
    ani_sort = sorted(prado1['animais'], key=lambda i: i['especie'])
    ani_sort2 = sorted(prado2['animais'], key=lambda i: i['especie'])
    list_rochas1 = list(ordenar_posicoes(prado1['rochas']))
    list_rochas2 = list(ordenar_posicoes(prado2['rochas']))
    list_posicoes1 = list(ordenar_posicoes(prado1['posicoes']))
    list_posicoes2 = list(ordenar_posicoes(prado2['posicoes']))
    if (eh_prado(prado1) and eh_prado(prado2) and zero(obter_tamanho_x(prado1) - obter_tamanho_x(prado2)) and
            zero(obter_tamanho_y(prado1) - obter_tamanho_y(prado2)) and
            [posicoes_iguais(list_rochas1[i], list_rochas2[i]) for i in range(len(prado1['rochas']))] and
            [animais_iguais(ani_sort[i], ani_sort2[i]) for i in range(len(prado1['animais']))] and
            [posicoes_iguais(list_posicoes1[i], list_posicoes2[i]) for i in range(len(prado1['posicoes']))]):
        return True
    return False


# Transformador

def prado_para_str(prado):
    """
    prados_para_str: prado -> string
    Esta função recebe um prado e devolve a string com as caracteristicas do prado.
    """
    # Lista com todas as posições
    todas_pos = []
    i = 0
    e = 0
    while i < obter_tamanho_y(prado):
        while e < obter_tamanho_x(prado):
            todas_pos += [cria_posicao(e, i)]
            e += 1
        e = 0
        i += 1
    # Trocar posições com simbolos de acordo com o enunciado
    for i in range(0, len(todas_pos)):
        if todas_pos[i] == (0, 0) or todas_pos[i] == (obter_tamanho_x(prado)-1, 0) or \
                todas_pos[i] == (0, obter_tamanho_y(prado)-1) or todas_pos[i] == (
        obter_tamanho_x(prado)-1, obter_tamanho_y(prado)-1):
            todas_pos[i] = '+'
        elif obter_pos_y(todas_pos[i]) == 0 or obter_pos_y(todas_pos[i]) == obter_tamanho_y(prado)-1:
            todas_pos[i] = '-'
        elif obter_pos_x(todas_pos[i]) == 0 or obter_pos_x(todas_pos[i]) == obter_tamanho_x(prado)-1:
            todas_pos[i] = '|'
        elif todas_pos[i] in prado['rochas']:
            todas_pos[i] = '@'
        elif todas_pos[i] in prado['posicoes']:
            todas_pos[i] = str(animal_para_char(obter_animal(prado, todas_pos[i])))
        else:
            todas_pos[i] = '.'
    # Print
    contador = 0
    for i in range(len(todas_pos)):
        if todas_pos[i] == '|' or todas_pos[i] == '+':
            contador += 1
            if contador == 2:
                todas_pos.insert(i + 1, '\n')
                contador = 0
    prado_mapa = ''.join(todas_pos)
    return prado_mapa

# Alto nivel

def obter_valor_numerico(prado, posicao):
    """
    obter_valor_numerico: prado,posicao -> string
    Esta função recebe um prado e uma posicao do prado e devolve um numero corresponde à ordem de leitura do prado.
    """
    if eh_posicao(posicao):
        if obter_pos_x(posicao) < obter_tamanho_x(prado) and obter_pos_y(posicao) < obter_tamanho_y(prado):
            return int(obter_pos_x(posicao)) + (int(obter_tamanho_x(prado)) * int(obter_pos_y(posicao)))


def obter_movimento(prado, posicao):
    """
    obter_movimento: prado,posicao -> posicao
    Esta função recebe um prado e uma posicao do prado e devolve uma posicao corresponde ao movimento criado.
    """
    adj = obter_posicoes_adjacentes(posicao)
    if obter_pos_x(posicao) <= obter_tamanho_x(prado) and obter_pos_y(posicao) <= obter_tamanho_y(prado) and \
            not eh_posicao_obstaculo(prado, posicao):
        for i in adj:
            if obter_pos_x(i) != 0 and obter_pos_x(i) != obter_tamanho_x(prado):
                if obter_pos_y(i) != 0 and obter_pos_y(i) != obter_tamanho_y(prado):
                    if eh_presa(obter_animal(prado, posicao)):
                        if i not in prado['rochas']:
                            if i not in prado['posicoes']:
                                return i
                    else:
                        if i not in prado['rochas']:
                            if eh_posicao_animal(prado, i):
                                return i
    return posicao


######################
# Funcoes adicionais #
######################

def geracao(prado):
    """
    geracao: prado -> prado
    Esta função recebe um prado e devolve o prado com todas as operações possiveis feitas(movimentos, fome e idade,
    entre outros)
    """
    # 1- Incremento da idade e fome
    for i in prado['animais']:
        if eh_presa(i):
            aumenta_idade(i)
        else:
            aumenta_fome(i)
            aumenta_idade(i)
    # 2- Movimentos
    for e in prado['posicoes']:
        mover_animal(prado, e, obter_movimento(prado, e))
    # 3- Idade de reprodução
    for m in range(len(prado['animais'])):
        if eh_animal_fertil(prado['animais'][m]):
            inserir_animal(prado, reproduz_animal(prado['animais'][m]), prado['posicoes'][m])
    # 4- Predador comer a presa
    for l in range(len(prado['posicoes'])):
        if eh_predador(obter_animal(prado, prado['posicoes'][l])):
            for x in range(len(prado['posicoes'])):
                if posicoes_iguais(prado['posicoes'][l], prado['posicoes'][x]):
                    if l == x:
                        continue
                    else:
                        eliminar_animal(prado, prado['posicoes'][x])
    # 5- Fome(para predadores)
    k = 0
    t = len(prado['animais'])
    while k < t:
        if eh_animal_faminto(prado['animais'][k]):
            eliminar_animal(prado, prado['posicoes'][k])
            t -= 1
            k += 1
        k += 1
    return prado


def simula_ecossistema(f, g, v):
    """
    simula_ecossistema: string,inteiro,booleano -> tuplo
    Esta função recebe uma string(nome do ficheiro de configuração), um inteiro(significando o numero de gerações) e um
    booleano(corrsponde à maneira de visualizar o jogo, se False, mostra a primeira e ultima geração, se True, mostra
    todas as gerações ate acabar o jogo) e devolve um tuplo de dois elementos que correspondem ao numero de predadores
    e presas no final da simulação.
    """
    with open(f, 'r') as f:
        prado_des = f.readlines()
        dim = eval(prado_des[0])
        roc = eval(prado_des[1])
        ani = []
        pos = []
        for i in range(2, len(prado_des)):
            animal_car = eval(prado_des[i])
            animal = cria_animal(animal_car[0], animal_car[1], animal_car[2])
            ani += [animal]
            pos += [animal_car[3]]
        f.close()
        prado = cria_prado(dim, roc, tuple(ani), tuple(pos))
        if v == False:
            print('Predadores: {} vs Presas: {} (Gen. 0)'.format(obter_numero_predadores(prado),
                                                                obter_numero_presas(prado)))
            print(prado_para_str(prado))
            for i in range(0,g+1):
                geracao(prado)
                if i == g:
                    print('Predadores: {} vs Presas: {} (Gen. {})'.format(obter_numero_predadores(prado),
                                                                 obter_numero_presas(prado), g))
                    print(prado_para_str(prado))
                    return obter_numero_predadores(prado),obter_numero_presas(prado)
        else:
            for i in range(0,g+1):
                if i == 0:
                    print('Predadores: {} vs Presas: {} (Gen. {})'.format(obter_numero_predadores(prado),
                                                                    obter_numero_presas(prado),i))
                    print(prado_para_str(prado))
                else:
                    print('Predadores: {} vs Presas: {} (Gen. {})'.format(obter_numero_predadores(prado),
                                                                          obter_numero_presas(prado), i))
                    geracao(prado)
                    print(prado_para_str(prado))
            return obter_numero_predadores(prado),obter_numero_presas(prado)

#Fim



