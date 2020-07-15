import dataset


class Banco(object):
 def __init__(self):   
    self.db = dataset.connect('sqlite:///mydatabase.db')
    self.table = self.db['Clientes']
 
 def cadastro(self,dados):
    self.dados = dados 
    print(self.dados)
    user = self.checka_user(dados['cpf'])
    if user == False:
       return "Usuario não existe na base"
     
    self.table.insert(self.dados)
    return "Usuario Cadastrado com sucesso !"

 def atualiza(self,ID,dados): 
     # checar se usuario existe
     user = self.checka_user(ID)
     if user == False:
       return "Usuario não existe na base"
     
     self.table.update(dados,['cpf'])
     return "Alteração feita com sucesso !"

 def lista(self,data=None):  # lista usuarios 

     users_list = []
     if data == '':
       lista = self.db['Clientes'].all()
       for user in lista:
           users_list.append(user)
     else:
       if data.isnumeric():
         user = self.table.find_one(cpf=data)
         users_list.append(user)

     return users_list

 def deleta(self,ID):
     # checar se usuario existe
     user = self.checka_user(ID)
     if user == False:
       return "Não Foi Posivel Deletar Usuario por que ele não consta na base"
     self.table.delete(cpf=ID)
     return "Usuario Deletado !"

 def checka_user(self,cpf=None):
   user = self.table.find_one(cpf=cpf)
   if user == None:
     return False
   return user
