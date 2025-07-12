-- 📌 Create main table for Indian states
CREATE TABLE IF NOT EXISTS states_info (
    state_name VARCHAR,
    tagline VARCHAR,
    image_url VARCHAR,
    description TEXT,
    places TEXT,
    cuisine TEXT,
    festivals TEXT,
    language_snippets TEXT
);

-- 📌 Track visits per state for analytics
CREATE TABLE IF NOT EXISTS visits (
    state VARCHAR,
    timestamp TIMESTAMP
);

-- 📌 Store user reviews and ratings
CREATE TABLE IF NOT EXISTS reviews (
    id INT AUTOINCREMENT,
    state VARCHAR,
    email VARCHAR,
    review TEXT,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ✅ Optional: Insert sample state (Rajasthan)
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

-- ✅ Optional: Insert sample visit
INSERT INTO visits (state, timestamp) VALUES ('Rajasthan', CURRENT_TIMESTAMP);

-- ✅ Optional: Insert sample review
INSERT INTO reviews (state, email, review) VALUES (
    'Rajasthan',
    'meghana@example.com',
    'I loved exploring Jaipur and the forts of Rajasthan!'
);
