# Movie Tracker Application

## Project Overview
This project is a **Movie Tracker Application** built using Flask. It allows users to create a personal list of their top movies by noting down details such as poster image, title, release year, description, user rating, movie ranking, and personal review. The application integrates with an external movie database API to fetch movie details and poster images dynamically, providing a seamless user experience.
      <br>
      <p align='center'>
        <a>
          <img src='https://github.com/user-attachments/assets/b8635372-24b8-4e9d-bafe-d9d53db17664' width="600">
        </a>
      </p>
      <br>

---

## Features

1. **Home Page**:
   - The home page displays all the movies stored in the database, sorted by user ratings. Additionally, it automatically assigns rankings to movies based on their ratings, ensuring that the top-rated movies are prominently highlighted.
   - The front side of the card will be shown on the home screen as below.
       <br>
      <p align='center'>
        <a>
          <img src='https://github.com/user-attachments/assets/e237b367-0357-4676-80ad-566dd65820d0' width="600">
        </a>
      </p>
      <br>
   - The back side of the card will contain all the remaining information, including the name of the movie, the year of release, rating, review, and description. Additionally, it will include both update and delete buttons.
  <br>
    <p align='center'>
      <a>
        <img src='https://github.com/user-attachments/assets/c4540e9c-0916-40ef-9b12-1f4b475165a9' width="600">
      </a>
    </p>
    <br>

2. **Add Movie**:
   - Users can search for a movie by entering its title.
       <br>
        <p align='center'>
          <a>
            <img src='https://github.com/user-attachments/assets/25f804d1-05ca-4c8b-a797-ab96d02cd1f9' width="600">
          </a>
        </p>
        <br>
   - The application fetches search results dynamically from the movie database API and presents a list of potential matches. Users can then select a movie from the list to add it to their personal collection.
  <br>
    <p align='center'>
      <a>
        <img src='https://github.com/user-attachments/assets/27ed96fa-1184-43f8-bc3e-d4eff1a77aa2' width="600">
      </a>
    </p>
    <br>

3. **Edit Movie**:
   - This feature allows users to update the user rating and personal review for a specific movie in their collection. This ensures that users can refine their preferences as they watch or re-watch movies.


  <br>
    <p align='center'>
      <a>
        <img src='https://github.com/user-attachments/assets/0736cd60-bb17-42f4-b976-80f2483331fb' width="600">
      </a>
    </p>
    <br>

4. **Delete Movie**:
   - Users have the ability to remove any movie from the database effortlessly. This feature provides flexibility in maintaining a curated list of favorite movies.

5. **Dynamic Ranking**:
   - The application dynamically adjusts the rankings of all movies whenever a rating is updated or a movie is deleted. This ensures that the rankings are always accurate and reflective of the user's preferences.

6. **Adding Duplicate Movie**:
   - "An error message indicating that the movie already exists will be displayed on the home screen if we attempt to add the same movie.


  <br>
    <p align='center'>
      <a>
        <img src='https://github.com/user-attachments/assets/20345b53-4430-42ad-a2b4-24237ad1be4b' width="600">
      </a>
    </p>
    <br>

---

## Technologies Used

- **Python**
- **Flask**
- **Flask-Bootstrap**
- **Flask-WTF** (for form handling)
- **Flask-SQLAlchemy** (for database management)
- **SQLite** (as the database engine)
- **WTForms** (for form validation)
- **Requests** (to interact with the movie API)
- **Dotenv** (for environment variable management)

---

## Installation Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yashskumar9/movie-tracker.git
   cd movie-tracker
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the project root directory and add the following keys and replace `<YOUR_API_KEY>` and `<API_URL>` with your API credentials(Refer API Integration below for more information):
     ```env
     API_KEY=<YOUR_API_KEY>
     MOVIE_API=<API_SEARCH_URL>
     MOVIE_INFO_URL=<API_MOVIE_DETAILS_URL>
     MOVIE_IMAGE_URL=<API_IMAGE_BASE_URL>
     ```

5. **Run the Application**:
   ```bash
   flask run
   ```
   Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## API Integration
- **The Movie Database(TMDb) API** is used for getting movie data and images. Refer the [TMDb documentation](https://developers.themoviedb.org/3/search/search-movies) to figure out how to request for movie data by making a search query.

---

## Future Improvements

1. **User Authentication**:
   - Add login and signup functionality to allow multiple users.

2. **Advanced Search**:
   - Allow filtering by genre, release year, and popularity.

3. **Responsive Design**:
   - Improve mobile-friendliness.

4. **Deployment**:
   - Deploy the application to a hosting platform like Heroku or AWS.

