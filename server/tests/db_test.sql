drop table if EXISTS transactions;

drop table if EXISTS accounts;

drop table if EXISTS users;

CREATE TABLE
    users (
        id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        surname VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        cpf VARCHAR(11) NOT NULL,
        birthdate DATE NOT NULL
    );

CREATE TABLE
    accounts (
        id CHAR(36),
        name VARCHAR(255) NOT NULL,
        user_id CHAR(36),
        balance int,
        max_daily_withdraw int,
        type int,
        is_active BOOLEAN DEFAULT TRUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id),
        FOREIGN KEY (user_id) REFERENCES users (id)
    );

CREATE TABLE
    transactions (
        id CHAR(36) PRIMARY KEY,
        account_id CHAR(36) NOT NULL,
        account_name VARCHAR(255) NOT NULL,
        amount INT NOT NULL,
        transaction_date TIMESTAMP NOT NULL,
        FOREIGN KEY (account_id) REFERENCES accounts (id)
    );

INSERT INTO
    users (
        id,
        name,
        surname,
        email,
        password,
        cpf,
        birthdate
    )
VALUES
    (
        'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
        'John',
        'Doe',
        'john.doe@example.com',
        'password',
        '12345678901',
        '1980-01-01'
    );

INSERT INTO
    accounts (
        id,
        name,
        user_id,
        balance,
        is_active,
        max_daily_withdraw,
        type,
        created_at
    )
VALUES
    (
        'b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12',
        'Conta 1',
        'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
        1000,
        TRUE,
        10000,
        1,
        CURRENT_TIMESTAMP
    );

INSERT INTO
    transactions (
        id,
        account_id,
        account_name,
        amount,
        transaction_date
    )
VALUES
    (
        'c2eebc99-9c0b-4ef8-bb6d-6bb9bd380a13',
        'b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12',
        'Conta 1',
        200,
        CURRENT_TIMESTAMP
    );