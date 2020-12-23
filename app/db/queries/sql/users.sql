-- name: get-user-by-email^
SELECT id,
       name,
       email,
       salt,
       hashed_password,
       created_at,
       updated_at
FROM users
WHERE email = :email
LIMIT 1;


-- name: get-user-by-name^
SELECT id,
       name,
       email,
       salt,
       hashed_password,
       created_at,
       updated_at
FROM users
WHERE name = :name
LIMIT 1;


-- name: create-new-user<!
INSERT INTO users (name, email, salt, hashed_password, date_of_birth, phone_number, address, pet_owner, admin, block)
VALUES (:name, :email, :salt, :hashed_password, :date_of_birth, :phone_number, :address, :pet_owner, false, false)
RETURNING
    id, created_at, updated_at;


-- name: update-user-by-name<!
UPDATE
    users
SET name            = :name,
    email           = :new_email,
    salt            = :new_salt,
    hashed_password = :new_password,
WHERE name = :name
RETURNING
    updated_at;
