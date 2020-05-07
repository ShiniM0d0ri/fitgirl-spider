import fitgirl_search
import gamepage

print("Enter name of the game")
query=input()
clink=fitgirl_search.spider(query)
print("\nWaiting for magnet links....")
gamepage.dlinks(clink)
