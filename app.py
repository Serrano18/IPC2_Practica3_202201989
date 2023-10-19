from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de películas (simulación de base de datos)

movies = []
#Add Movie
@app.route('/api/new-movie', methods=['POST'])
def add_movie():
    data = request.get_json()
    movie_id = data.get('movieId')
    name = data.get('name')
    genre = data.get('genre')
    
    if movie_id is None or name is None or genre is None:
        return jsonify(f"Falta informacion en la solicitud"), 400

    movie = {
        "movieId": movie_id,
        "name": name,
        "genre": genre
    }
    movies.append(movie)

    return jsonify( f"La pelicula '{name}' fue agregada con exito")

#Obtener Peliculas
@app.route('/api/all-movies-by-genre/<string:genre>', methods=['GET'])
def get_movies_by_genre(genre):
    matching_movies = [movie for movie in movies if movie['genre'] == genre]
    
    if not matching_movies:
        return jsonify({"message": "No se encontraron películas en ese género"}), 404

    # Convierte el conjunto en una lista antes de serializarlo en JSON
    matching_movies_list = list(matching_movies)

    return jsonify(matching_movies_list)


#Actualizar 
@app.route('/api/update-movie', methods=['PUT'])
def update_movie():
    data = request.get_json()
    movie_id = data.get('movieId')
    name = data.get('name')
    genre = data.get('genre')
    
    if movie_id is None or name is None or genre is None:
        return jsonify({"message": "Falta información en la solicitud"}), 400

    for movie in movies:
        if movie['movieId'] == movie_id:
            movie['name'] = name
            movie['genre'] = genre
            return jsonify({"message": f"La película '{name}' fue actualizada con éxito"})

    return jsonify({"message": f"No se encontró una película con ID {movie_id}"})


if __name__ == '__main__':
    app.run()
