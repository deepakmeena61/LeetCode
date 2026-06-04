/* Write your T-SQL query statement below */
SELECT Distinct author_id as id FROM Views
WHERE author_id = viewer_id
Order by author_id;