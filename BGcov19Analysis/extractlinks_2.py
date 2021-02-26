#TODO - enum months

def find_relevant():
    i = 0
    headlines = open("all_headlines(1).txt",encoding="utf-8", mode="r") 
    news = open("all_news(2).txt",encoding="utf-8", mode="w") 
    covnews = open("all_covreportnews(3).txt",encoding="utf-8", mode="w") 
    for line in headlines:
        a = line.split()
    
        if i%3 == 0:
            lis = a[0].split("/")
            news.write(lis[3])
            news.write(" ")
        elif i%3 == 1:
            news.write(a[0])
            news.write(" ")
            #enum
        #TODO:this step can be optimized to not use the next for and file(2)    
        elif i%3 == 2:
            if a[0].isdigit()  and not a[1].isdigit():
                news.write(a[0])
            news.write("\n")
        i += 1
        
    news.close()        
    news = open("all_news(2).txt",encoding="utf-8", mode="r") 

    for line in news:
        lines = line.split()
        if len(lines) == 3:
            covnews.write(line) 
            
    headlines.close()        
    news.close()        
    covnews.close()        
if __name__ == '__main__':
    find_relevant()
