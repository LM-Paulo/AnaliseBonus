import pandas as pd
from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = "AC9237e98b7f2a084e0fe90a35b2197be6"
# Your Auth Token from twilio.com/console
auth_token  = "3ceb515090f9bc3b7db25824e440698d"
client = Client(account_sid, auth_token)



#abrir os 6 arquivos em Exel
lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']


for mes in lista_meses:
   tabela_vendas = pd.read_excel(f'{mes}.xlsx')
   if (tabela_vendas['Vendas'] > 55000).any() :
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}, ')

        message = client.messages.create(
            to="+5531984804867",
            from_="+17407154938",
            body=f'No mês {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}, ')

        print(message.sid)


