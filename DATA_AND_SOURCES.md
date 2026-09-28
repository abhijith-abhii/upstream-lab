# Data, code and model sources

The topic comes from the source mapping in the portfolio index. Original authored synthetic fixtures and procedural images are distributed under the repository MIT license. Synthetic records do not describe actual customers, employees, players or transactions.

Implementation references:
- Flask: https://flask.palletsprojects.com/en/stable/ — request handling and security considerations.
- Python SQLite: https://docs.python.org/3/library/sqlite3.html — transactions, parameter binding and authorizers.
- scikit-learn: https://scikit-learn.org/stable/common_pitfalls.html — leakage prevention and fitted preprocessing.

Only applicable libraries are used; their upstream licenses remain in installed distributions. Project code does not claim authorship of dependencies.

Upstream python-slugify: [pinned metadata](upstream.json), [MIT license](UPSTREAM_LICENSE), and [contribution scope](CONTRIBUTION.md). text-unidecode offers an Artistic/GPL licensing choice; do not equate the project MIT license with every dependency license. No upstream submission has been made.
