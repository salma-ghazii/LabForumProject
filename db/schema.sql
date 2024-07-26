-- Create Labs Table
CREATE TABLE IF NOT EXISTS labs (
    LabID INTEGER PRIMARY KEY AUTOINCREMENT,
    Location TEXT
);

-- Create Users Table
CREATE TABLE IF NOT EXISTS users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    ContactInfo TEXT
);

-- Create Chemicals Table (Optional)
CREATE TABLE IF NOT EXISTS chemicals (
    ChemicalID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Description TEXT
);

-- Create Posts Table
CREATE TABLE IF NOT EXISTS posts (
    PostID INTEGER PRIMARY KEY AUTOINCREMENT,
    LabID INTEGER,
    UserID INTEGER, -- Poster
    Date TEXT, -- ISO 8601 Date Format
    ClaimedByUserID INTEGER, -- Nullable
    ChemicalID INTEGER,
    FOREIGN KEY (LabID) REFERENCES labs(LabID),
    FOREIGN KEY (UserID) REFERENCES users(UserID),
    FOREIGN KEY (ClaimedByUserID) REFERENCES users(UserID),
    FOREIGN KEY (ChemicalID) REFERENCES chemicals(ChemicalID)
);
