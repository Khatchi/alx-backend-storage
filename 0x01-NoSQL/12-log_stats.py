//Regex filter
db.school.find({ name: { $regex: '^Holberton*' } })
