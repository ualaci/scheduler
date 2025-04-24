# 📅 Sistema de Cadastro e Gerenciamento de Reuniões

Este é um sistema web simples desenvolvido em **Django** para cadastrar, listar e remover reuniões. Ele permite registrar informações como data, solicitante, local, objetivo da reunião e se haverá serviço de café.

## 🚀 Funcionalidades

- ✅ Cadastro de reuniões com data, local, solicitante e propósito.
- 📋 Listagem de reuniões futuras com formatação visual (Bootstrap).
- 🗑️ Remoção de reuniões diretamente pela interface.
- ⏰ Filtragem automática para exibir apenas reuniões com data a partir de hoje.
- 🎨 Estilização com **Bootstrap 5** e ícones com **FontAwesome**.

## 🧱 Estrutura do Projeto

- `models.py`: contém o modelo `Meeting`, incluindo campos como data, solicitante, local, objetivo e serviço de café.
- `forms.py`: formulário `UserForm` para entrada de dados.
- `views.py`: lida com a lógica de cadastro, listagem e remoção de reuniões.
- `templates/`: arquivos HTML com uso do template engine do Django.
- `urls.py`: roteamento para as views de listagem, cadastro e remoção.

## 📦 Instalação

### Pré-requisitos

- Python 3.8+
- pip
- virtualenv (opcional, mas recomendado)

### Passos

```bash
# Clone o repositório
git clone https://github.com/seuusuario/seurepositorio.git
cd seurepositorio

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Realize as migrações
python manage.py migrate

# Crie um superusuário para acessar o admin
python manage.py createsuperuser

# Inicie o servidor de desenvolvimento
python manage.py runserver
