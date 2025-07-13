-- schema_postgres.sql

CREATE TABLE IF NOT EXISTS states_info (
    state_name TEXT PRIMARY KEY,
    tagline TEXT,
    image_url TEXT,
    description TEXT,
    places TEXT,
    cuisine TEXT,
    festivals TEXT,
    language_snippets TEXT
);

CREATE TABLE IF NOT EXISTS visits (
    id SERIAL PRIMARY KEY,
    state TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS reviews (
    id SERIAL PRIMARY KEY,
    state TEXT,
    email TEXT,
    review TEXT,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Optional: Sample data
INSERT INTO states_info VALUES (
  'Rajasthan',
  'The Land of Kings',
  'https://upload.wikimedia.org/wikipedia/commons/0/05/Hawa_Mahal.jpg',
  'Rajasthan is known for its forts, palaces, and desert culture.',
  'Jaipur,Udaipur,Jodhpur,Jaisalmer',
  'Dal Baati Churma,Gatte ki Sabzi',
  'Pushkar Fair,Teej,Desert Festival',
  '[{"en": "Hello", "native": "राम राम"}, {"en": "Thank you", "native": "धन्यवाद"}]'
);
