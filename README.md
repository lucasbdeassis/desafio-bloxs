# Technical Challenge - Full Stack Developer

## Objective

In this challenge we were asked to build a backend using Python and a frontend using ReactJS.

The proposal was to simulate a bank account management system, where the user could make deposits, withdrawals, create and block accounts.

## How to run

There is a docker-compose file in the root of the project, which can be used to run the application. To do this, just run the following command:

```bash
docker-compose up
```

The application will be available at [http://localhost](http://localhost)

The docker compose will start all the services, including the database, and will also run the creation of the database tables and the insertion of the initial data.

The app can be accessed wit the credentials:

```txt
email: john.doe@example.com
password: password
```

## Frontend

The frontend was built using ReactJS, with the help of Vite. I chose to use Vite because it is a very fast build tool, which makes the development process much more agile. The styling was done using Bootstrap 5.

## Backend

The backend was built using Flask, with the MySQL database and the SQLAlchemy ORM.

As for the chosen architecture, I used the concepts of Clean Architecture, where the code is divided into layers according to their responsibilities.

To ensure interdependence between the layers, and that structures in the inner layers don't depend on structures in the outer layers, I used the concept of Dependency Inversion, with the declaration of interfaces.

I also applied the concept of dependency injection, where dependencies are injected into the classes that use them, rather than being instantiated within them. Orchestration is done through the Main input file, and injection is facilitated by the use of a Factory pattern.

The development was done using TDD, where the tests were created first and then the code for the tests to pass. The integration tests use an in-memory instance of the bank, with automatic assembly and disassembly. The end-to-end tests use the actual database, and the data needs to be inserted and deleted manually.

The application has an authentication layer using JWT, where the user can authenticate and receive a token, which must be used to access the protected routes. The token ensures that the user only has access to the data that belongs to them.

Just a detail about the way the values are stored in the database, I chose to save them as integers knowing that you only have to divide the value by 100 to get its monetary correspondent. I found it simpler to work with integer values than float/decimals.

### Bloxs Application Domain

The Bloxs application is a banking system simulation that allows users to manage accounts and perform transactions.

#### Domain Overview

The domain of the Bloxs application is composed of three main entities: User, Account, and Transaction.

##### User
A User represents an individual who uses the banking system. Each user is identified by a unique ID and has associated personal information such as email and password.

##### Account

An Account represents a bank account owned by a user. Each account is identified by a unique ID and has associated attributes such as balance, maximum daily withdrawal limit, and name. An account also has a status indicating whether it is active or blocked.

##### Transaction

A Transaction represents a monetary operation performed on an account, such as a deposit or withdrawal. Each transaction is identified by a unique ID and has associated attributes such as the account ID, amount, and transaction date.

##### Domain Implementation

The domain entities are implemented as Python classes in the bloxs/domain directory:

* User: Represents a user in the banking system.
* Account: Represents a bank account.
* Transaction: Represents a transaction performed on an account.

These classes encapsulate the core business logic and rules of the Bloxs application. They are independent of any specific infrastructure, database, or web framework, which allows the business logic to be developed and tested independently of the rest of the application.

### Endpoints

#### Account Controller

GET ``/accounts/{account_id}``
This endpoint retrieves the details of a specific account.

URL Parameters:

account_id: The ID of the account to retrieve.
Response:

Returns a JSON object representing the account.

GET ``/accounts``
This endpoint retrieves a list of all accounts associated with the authenticated user.

Response:

Returns a JSON array of objects, each representing an account.

POST ``/accounts``
This endpoint creates a new account for the authenticated user.

Request Body:

A JSON object containing the details of the account to create.

Response:

Returns a JSON object representing the created account.

POST ``/accounts/{account_id}/deposit``
This endpoint makes a deposit into a specific account.

URL Parameters:

account_id: The ID of the account to deposit into.
Request Body:

A JSON object containing the details of the deposit.

Response:

Returns a JSON object representing the updated account.

POST ``/accounts/{account_id}/withdraw``
This endpoint makes a withdrawal from a specific account.

URL Parameters:

account_id: The ID of the account to withdraw from.
Request Body:

A JSON object containing the details of the withdrawal.

Response:

Returns a JSON object representing the updated account.

POST ``/accounts/{account_id}/block``
This endpoint blocks a specific account.

URL Parameters:

account_id: The ID of the account to block.
Response:

Returns a JSON object representing the blocked account.

POST ``/accounts/{account_id}/unblock``
This endpoint unblocks a specific account.

URL Parameters:

account_id: The ID of the account to unblock.
Response:

Returns a JSON object representing the unblocked account.

#### Auth Controller

POST ``/auth/login``
This endpoint logs in a user.

Request Body:

A JSON object containing the user's email and password.

Response:

Returns a JSON object containing the user's authentication token.

POST ``/auth/validate``
This endpoint validates a user's authentication token.

Request Body:

A JSON object containing the user's authentication token.

Response:

Returns a JSON object indicating whether the token is valid.

#### Transaction Controller

GET ``/transactions``
This endpoint retrieves a list of all transactions associated with the authenticated user.

Response:

Returns a JSON array of objects, each representing a transaction.
