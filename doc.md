# Project Documentation

## Python packages used in this project (Imports)

1. Flask -- for creating web api
2. Pandas -- data processing
3. CountVectorized -- covert collection of text documents to matrix of token count.
4. cosine_similarity -- compute the cosine similarity between two vectors. (text analysis).

## Run command

```python
python main.py
```

## If you want to run in isolate env.
``` bash 
python3.9 -m venv venv
```

## Default API port-

http://localhost/5000

note: don't any other process on this port.

## Api Route

### Route

#### / recommend

    method - POST
    endpoint - http://localhost/5000/recommend

## Api Responses

#### 200 Ok

```json
{
  "recommendations": [
    "Batman Returns",
    "The Batman vs. Dracula",
    "Batman Beyond: Return of the Joker",
    "The Dark Knight",
    "Batman Begins"
  ]
}
```

#### 400 BAD REQUEST

```
{
    "error": "Title is required"
}
```

#### 404 NOT FOUND

```json
{
  "error": "Movie not found"
}
```

#### 405 METHOD NOT ALLOWED

```html
<!DOCTYPE html>
<html lang="en">
  <title>405 Method Not Allowed</title>
  <h1>Method Not Allowed</h1>
  <p>The method is not allowed for the requested URL.</p>
</html>
```

## Main function (Hero of the show)

### recommend()

```text
    Recommend movies based on a given movie title.This function takes a movie title from a JSON request, finds the movie in the dataset,and returns a list of recommended movies based on similarity.
```

## Folder Structure

```md
.vscode: Directory for Visual Studio Code settings.

settings.json: Configuration file for VS Code settings.

data: Directory for data files.
.DS_Store: System file used by macOS.

data.csv: CSV file containing data.
doc.md: Markdown file, likely containing documentation.

main.py: Main Python script for your project.

venv: Directory for the Python virtual environment.

bin/: Directory for executable files in the virtual environment.
activate, activate.csh, activate.fish, Activate.ps1: Scripts to activate the virtual environment.
Various executables like python, pip, etc.

include/: Directory for C headers that are part of the virtual environment.

lib/: Directory for Python libraries in the virtual environment.

python3.9/: Directory for Python 3.9 libraries.

site-packages/: Directory for installed Python packages.

Various packages and their compiled bytecode files (**pycache**).

pyvenv.cfg: Configuration file for the virtual environment.
```

## Credit

#### Swata Shaw (Data Processing & building recommendation function)

#### Gourab Sarkar (Api Integration & Documentation)
