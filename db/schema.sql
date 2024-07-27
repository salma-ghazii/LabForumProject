-- Labs table
CREATE TABLE IF NOT EXISTS labs (
    LabID INTEGER PRIMARY KEY AUTOINCREMENT,
    Location TEXT NOT NULL
);

-- Users table
CREATE TABLE  IF NOT EXISTS users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT UNIQUE NOT NULL,
    Password TEXT NOT NULL
);

-- Create Chemicals Table (Optional)
CREATE TABLE IF NOT EXISTS chemicals (
    ChemicalID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Description TEXT
);

-- Create Posts Table
-- CREATE TABLE IF NOT EXISTS posts (
--     PostID INTEGER PRIMARY KEY AUTOINCREMENT,
--     LabID INTEGER,
--     UserID INTEGER, -- Poster
--     Date TEXT, -- ISO 8601 Date Format
--     ClaimedByUserID INTEGER, -- Nullable
--     PostContent TEXT, 
--     FOREIGN KEY (LabID) REFERENCES labs(LabID),
--     FOREIGN KEY (UserID) REFERENCES users(UserID),
--     FOREIGN KEY (ClaimedByUserID) REFERENCES users(UserID),
--     FOREIGN KEY (ChemicalID) REFERENCES chemicals(ChemicalID)
-- );

-- Posts table (updated to include UserID)
CREATE TABLE IF NOT EXISTS posts (
    PostID INTEGER PRIMARY KEY AUTOINCREMENT,
    LabID INTEGER,
    UserID INTEGER,
    PostContent TEXT NOT NULL,
    FOREIGN KEY (LabID) REFERENCES labs (LabID),
    FOREIGN KEY (UserID) REFERENCES users (UserID)
);