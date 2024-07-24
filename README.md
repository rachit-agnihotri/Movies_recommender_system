
# Movie Recommender System

Welcome to the Movie Recommender System! This application helps you find movie recommendations based on a selected movie. It uses a similarity matrix to identify and suggest movies similar to your chosen one, along with their posters.
Trained on TMDB movies data set using content based filtering method. App built using streamlit for deployment. TMDB api to fetch movies data like posters and images

## Features

- **Movie Recommendations:** Select a movie from a list to get recommendations for similar movies.
- **Movie Posters:** View posters of recommended movies.

## Installation

To run this application, you'll need to set up your environment with the following dependencies:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Movies_recommender_system.git
   cd Movies_recommender_system
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

## Files

- **`movies.pkl`**: Contains the movie data used for recommendations.
- **`similarity.pkl`**: Contains the similarity matrix used for finding similar movies. *Note: Due to size constraints, this file is not included in the repository.*

## Usage

1. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

2. **Access the app:**
   Open your web browser and go to `http://localhost:8501` to interact with the Movie Recommender System.

## Generating the Similarity Matrix

The `similarity.pkl` file is not uploaded due to its large size. You can generate this file using the `movies_recommender.py` script. Follow these steps:

1. **Ensure you have the required packages installed.**
2. **Run the script:**
   ```bash
   python movies_recommender.py
   ```

   This script will generate the `similarity.pkl` file that you need for the recommender system.

## Contributing

If you would like to contribute to this project, feel free to submit a pull request. Please ensure that your contributions follow the guidelines and add tests where applicable.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to adjust any specifics based on your project or personal preferences!
