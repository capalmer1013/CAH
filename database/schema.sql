CREATE TABLE whiteCards (
    ID integer PRIMARY KEY,
    cardText TEXT
);

CREATE TABLE blackCards (
    ID integer PRIMARY KEY,
    cardText TEXT,
    pick integer
);

CREATE TABLE users (
    ID integer PRIMARY KEY,
    userName text,
    password text,
    room integer
);

CREATE TABLE hand (
    ID integer PRIMARY KEY,
    playerID integer,
    cardID integer
);

CREATE TABLE deckWhite (
    ID integer PRIMARY KEY,
    whiteCardID integer,
    roomID integer
);

CREATE TABLE deckBlack (
    ID integer PRIMARY KEY,
    blackCardID integer,
    roomID integer
);

CREATE TABLE rooms (
    ID integer PRIMARY KEY,
    playersTurn integer
);
