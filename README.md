![header](https://user-images.githubusercontent.com/123844821/232592287-d2578b53-4339-46c6-881d-d03e4220012d.png)

> Status: Developing 💻

## Comments

It is a system for a vehicle dealership where it is possible to register new vehicles and display them in a stock list, as well as filter this list by brand, category, price, year, and state. For data storage, an integration with a PostgreSQL database was used. The vehicles stored in it, through a field to store the visualizations, can be listed according to their "popularity".

## Technologies Used:

<table>
  <tr>
    <td>Django</td>
    <td>PostgreSQL</td>
  </tr>
</table>

## User fields are:

+ id 
+ name 
+ modelo
+ motor
+ cor 
+ ano 
+ placa
+ km
+ cambio
+ combustível
+ portas
+ opcionais
+ observações
+ preçõ
+ estado
+ status
+ vizualizações
+ categoria_id
+ fabricante_id
+ tipo_id

## Commands:

### `python -m venv venv`

Create a new virtual environment.\

### `venv\Scripts\Activate`

Activates the created virtual environment.\

### `python manage.py migrate`

Performs database migrations\

### `python manage.py runserver`

Start the server in the development mode.\
Open [http://127.0.0.1:8000](http://127.0.0.1:8000) to view it in your browser.


## How to use this project:
1) download the files from this repository
2) open folder in terminal
3) run the command "python -m venv venv"
4) run the command "venv\Scripts\Activate"
5) create an empty PostgreSQL database
6) access the "settings.py" file in your app's folder and fill in the "DATABASE" session according to the database data created
7) run the command "python manage.py migrate"
8) run the command "python manage.py runserver"


## Project image
![project](https://user-images.githubusercontent.com/123844821/232592423-7b5e7432-138c-461e-83b4-d5ee1dd034cf.png)
