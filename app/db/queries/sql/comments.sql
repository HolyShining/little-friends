-- name: get-comment-by-id-and-slug^
SELECT c.id,
       c.content,
       c.created_at,
       c.updated_at,
       (SELECT name FROM users WHERE id = c.author_id) as author_username
FROM commentaries c
         INNER JOIN announcements a ON c.announcement_id = a.id AND (a.slug = :announcement_slug)
WHERE c.id = :comment_id;

-- name: create-new-comment<!
WITH users_subquery AS (
        (SELECT id, name FROM users WHERE name = :author_username)
)
INSERT
INTO commentaries (content, author_id, announcement_id)
VALUES (:content,
        (SELECT id FROM users_subquery),
        (SELECT id FROM announcements WHERE slug = :announcement_slug))
RETURNING
    id,
    content,
        (SELECT name FROM users_subquery) AS author_username,
    created_at,
    updated_at;

-- name: delete-comment-by-id!
DELETE
FROM commentaries
WHERE id = :comment_id
  AND author_id = (SELECT id FROM users WHERE name = :author_username);
