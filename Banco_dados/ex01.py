"""
produto-frutas
atributos:nome,codigo,preço,peso
    chave:codigo
    valor:nome,preço,peso
"""
import json
banco_dados={}
opcao= 1
#preciso carregar o que estiver no arquivo
try:
    with open('estoque.json', 'r') as arquivo:
        banco_dados = json.load(arquivo)
except:
    print('o arquivo não existe')        
while opcao!=7:
    print('='*10)
    print('1- Inserir produto')
    print('2- Consultar por codigo')
    print('3- Consultar todos')
    print('4- Alterar preço')                               #menu interativo
    print('5- Aplicar Acrescimo ou Desconto')
    print('6- excluir registro')
    print('7- Sair')
    opcao = int(input('Escolha a opção: ')) #solicitação do menu
    if opcao ==1:
        print('-'*10)
        print('Cadastro')
        codigo = input('Digite o código do produto: ') #inserir o codigo do produto
        nome = input('Nome do produto: ') #inserir nome do produto
        quantidade = input('Quantidades: ') #inserir quantidade do produto
        preço = float(input('Preço do produto kg/unidade: ')) #inserir preço do produto
        banco_dados[codigo] = {'Nome':nome, 'Quantidade':quantidade, 'Preco': preço} # código será a chave que recebe o 'valor'(informaçoes) "nome" "quantidade" "Preço"
        
        with open("estoque.json","w") as arquivo: #caminho onde será salvo as informaçoes em um naco de dados 'json'
            json.dump(banco_dados , arquivo, indent=4) #grava os arquivos
    
    elif opcao ==2:
        print('-'*10)
        print('consultar por codigo')
        codigo = input('Digite o codigo do produto: ') #solicitação do codigo para a pesquisa
        if codigo in banco_dados: # verifica se o codigo solicitado está no banco de dados
            dados = banco_dados[codigo] #variavel suporte para guardar a informação do código solicitado
            print(f'produto{dados}')
        else:
            print('Produto não encontrado')    
            

    elif opcao ==3:
        print('-'*20)
        print('Consultar todos')
        for produto in banco_dados.values(): #entrega os valores de cada chave do banco de dados
            print(produto)
        
    elif opcao ==4:
        print('-'*20)
        print('Alterar preço')
        codigo = input('Digite o codigo do produto para alteração de preço: ') #solicitação do codigo para alteração de preço
        if codigo in banco_dados: # verifica se o codigo solicitado está no banco de dados
            print(banco_dados[codigo]) # mostra o produto solicitado
            novo_preço = input('novo preço: ') #variavel suporte para guardar o novo preço
            banco_dados[codigo]['Preco'] = novo_preço #altera o valor 'Preço' dentro do codigo do produto solicitado
            with open('estoque.json', 'w') as arquivo: #salva os dados imediatamente após a alterção do preço
                json.dump(banco_dados, arquivo, indent=4)
        else:
            print('Produto não encontrado.')

    elif opcao ==5:
        print('-'*20)
        print('Acrescimo ou juros em porcentagem:')
        porcentagem = float(input('Digite a oscilação de preço em porcentagem:')) #entrada da porccentagem de acrescimo ou desconto
        for codigo in banco_dados: #percorre nos codigo de cada produto do banco de dados
            produto = banco_dados[codigo] #variavel produto recebe o produto do loop
            preco = produto['Preco'] #variavel suporte preço recebe o preço atual do produto
            novo_preço = preco*(1+porcentagem/100) #gera um novo preço e armazena em uma variavel
            produto['Preco'] = novo_preço   #insere o novo valor de volta ao produto
    
    elif opcao ==6:
        print('Excluir produto')
        codigo = input('Digite o codigo do produto a ser excluido: ') #solicitação do codigo do produto a ser excluido
        if codigo in banco_dados: #verifica se o codigo está no banco de dados
            del banco_dados[codigo] #deleta a chave(codigo) do banco de dados        
            with open('estoque.json', 'w') as arquivo: #salva os dados imediatamnet após a exclusão
                json.dump(banco_dados, arquivo, indent=4)
        else:
            print('Produto não encontrado.')
        
    elif opcao ==7:
        print('Saindo...')
        with open('estoque.json', 'w') as arquivo: #salva os dados antes de sair do programa
            json.dump(banco_dados, arquivo, indent=4)
        arquivo.close    
    else:
        print('Opção inválida.')   