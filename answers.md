## Coding test

### Time spent on coding test
About a total of 20 hours was spent working on the coding test

### If time wasn't a constraint, I would:
- Implement a better error handling on the frontend
- Implement pagination on the frontend. (Pagination is only on the backend currently)
- Display errors to the frontend user
- Use VueX and implement better state management
- Enable drag and drop to reorder favorite items
- Improve the general UX 
- populate the DB with some categories when migration is run
- Use a CI tool
- Make the UI more attractive
- Automate deploy with a script
- Integrate Flake8 lint check to testing
- Add more tests to the backend
- Add tests to the frontend
- Add test coverage report
- Implement end-to-end testing

## Most useful feature in latest Python version
Python 3.8 is the latest version, but it is still in beta state and I have not worked with it yet. 
However, the official latest realease which is Python 3.7 has many cool features added and the one I find most usefull is the introduction of the breakpoint keyword.
So instead of using `import pdb; pdb.set_trace()`,  we now use `breakpoint()` to enter debug mode.

```python
def concatFavorites(rank1, rank2, rank3=None):
    favs = f'{rank1} + {rank2}'
    if rank3:
        breakpoint()
        favs = f'{favs}, {rank3}'
    return favs

print(concatFavorites('Chinua Achebe', 'Steven King', 'Stepen Fry'))
```

## Tracking down a performance issue in production
One of the ways to track down a performance issue in production is to make use of logging and monitoring tools. Comparing perfomance on latest deploy with previous deploy and narrowing the root cause to features that has been added in the latest deploy.
most times, it is not so difficult to guess where the bottleneck is from especially after a recent feature has been added. Also, having a look at the logs while the code runs provide useful cues.
Through watching DB query logs, I have been able to optimize a Django app by using `select_related` queryset.
