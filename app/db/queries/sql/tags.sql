-- name: get-all-tags
SELECT name
FROM tags;


-- name: create-new-tags*!
INSERT INTO tags (tag)
VALUES (:tag)
ON CONFLICT DO NOTHING;
