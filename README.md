# dxc_edi_api_relatorios
 
python -m venv edi_api_relatorios
edi_api_relatorios\Scripts\activate


Criando a imagem
    docker build -f docker/Dockerfile -t danieldias/api .

Criando um container a partir da imagem
    docker run -d -p 8080:5000 danieldias/api


