# **Movie Finder**  

A Python script that scrapes IMDb to find the top 10 best movies based on your preferences (genre, rating, release year, and review count).  

## **Description**  
Movie Finder is a command-line tool that helps you discover great movies by pulling data directly from IMDb. You can filter movies based on:  
- Genre (e.g., Action, Horror, Sci-Fi)  
- Minimum IMDb rating  
- Release year range  
- Minimum and maximum number of reviews  

It then displays a list of the top matching movies right in your terminal.  


## **Requirements & Installation**  

### **Requirements**  
- Python 3 or higher  
- Libraries: `requests`, `beautifulsoup4`  

### **Installation**  
1. Clone this repository:  
   ```bash
   git clone https://github.com/RajvirsinhJadeja/movie-finder.git
   cd moviefinder
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## **How to use the program**
Run the script with:

```bash
python main.py
```

You will be prompted for:

- Genre
- Minimum IMDb rating
- Release year range
- Review count range

![reveal gif](https://github.com/RajvirsinhJadeja/movie-finder/blob/dev/assets/movie_finder_demo.gif)

### **Example**

```yaml
What genre are you in the mood for? (e.g. action, sci-fi, horror): action
Enter the minimum IMDb rating you're okay with (0-10): 7
Enter the earliest release year (Leave blank for no limit): 2000
Enter the latest release year (Leave blank for no limit): 2025
Enter the minimum number of reviews (Leave blank for no limit): 50000
Enter the maximum number of reviews (Leave blank for no limit): 
```

### **Output**

```markdown
Here are some movies you might enjoy:

1. The Fantastic Four: First Steps
2. Superman
3. Sinners
4. F1: The Movie
5. How to Train Your Dragon
...
```
## **License**
Distributed under the MIT license. See LICENSE for more information.
