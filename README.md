# hackerrank_solution_download_script
Script to download HackerRank submitted solutions

Under Construction



Used requests and BeautifulSoup modules from Python to get the url and navigate through the tags to get challenge names before finally being able to construct the URL for each challenge and navigating to the solution to download it.

Completed: 

* Getting a URL using *requests* module of Python,
* Logging in using requests.get(),
* Iterate over the content of the response captured, in chunks,
* Using a file descriptor, write it to a file on the disk,
* Use *BeautifulSoup()* to do *html.pars*-ing over the file,
* Using the returned bs object, find tags that satisfy the necessary condition (for example, contain a particular text),
* Get values of specific attributes from the tags.

TODO:

* Navigate to leaderboard from each challenge.
* Look for a tag with the username. 
* Download submission with the submitted code.  
