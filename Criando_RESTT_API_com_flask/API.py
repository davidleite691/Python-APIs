from flask import Flask
import pandas as pd

app = Flask(__name__) # cria o site
tabela = pd.read_excel(r"C:\Users\david\Documents\CursoDePython\Criando_RESTT_API_com_flask\Vendas - Dez.xlsx") # Banco de dados para ser acessado

@app.route("/") # decorator -> diz em qual link a função vai rodar
def fat(): # Função para acessar o cálculo do faturamento
    faturamento = float(tabela["Valor Final"].sum())
    return {"faturamento": faturamento}

@app.route("/vendas/produtos") 
def vendas_produtos(): # Função que retorna o valor de vendas de todos os produtos
    tabela_vendas_produtos = tabela[["Produto", "Valor Final"]].groupby("Produto").sum()
    dic_vendas_produtos = tabela_vendas_produtos.to_dict()
    return dic_vendas_produtos

@app.route("/vendas/produtos/<produto>") 
def fat_produto(produto): # Função que retorna o valor de vendas de um produto específico
    tabela_vendas_produtos = tabela[["Produto", "Valor Final"]].groupby("Produto").sum()
    if produto in tabela_vendas_produtos.index:
        vendas_produto = tabela_vendas_produtos.loc[produto]
        dic_vendas_produto = vendas_produto.to_dict()
        return dic_vendas_produto
    else:
        return {produto: "Inexistente"}
    
app.run()