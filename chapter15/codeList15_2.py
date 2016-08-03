'''add try...catch to catch IOError'''

def calcEfficiency(line,theDict):
    '''Calculate player efficiency'''
    fields = line.split(',')
    firstName = fields[1]
    lastName = fields[2]
    
    #mapping fields in a line to their particular uariable.
    #league is a str ,everthing else an int 
    leag,gp,mins,pts,ored,dreb,reb,asts,\
    stl,blk,to,pf,fga,fgm,fta,ftm,tpa,tpm = \
    fields[3],int(fields[4]),int(fields[5]),int(fields[6]),int(fields[7]),\
    int(fields[8]),int(fields[9]),int(fields[10]),int(fields[11]),int(fields[12]),\
    int(fields[13]),int(fields[14]),int(fields[15]),int(fields[16]),int(fields[17]),\
    int(fields[18]),int(fields[19]),int(fields[20])
    
    #calculate the player's efficiency
    efficiency = ((pts+reb+asts+stl+blk)-((fga-fgm)+(fta-ftm)+to))/float(gp)
    
    theDict[lastName+firstName] = {'first':firstName,'last':lastName,\
                                   'league':leag,'mins':mins,'gp':gp,\
                                   'pts':pts,'ored':ored,'dreb':dreb,'reb':reb,\
                                   'asts':asts,'stl':stl,'blk':blk,'to':to,'pf':pf,\
                                   'fga':fga,'fgm':fgm,'fta':fta,'ftm':ftm,'tpa':tpa,\
                                   'tpm':tpm,'efficiency':efficiency 
                                   }

def findMostEfficient(theDict,howMany):
    '''return list of tuple(efficiency,name) from dictionary
    howmany is number of tuples to gather'''
    #user must implement 
    return []

def printResults(lst):
    '''pretty print the results '''
    print 'The top %d players in efficency are'%len(lst)
    print '*'*20
    
#main program as a Function
def main():
    fName = raw_input('NBA player file name:')
    try:
        fd = open(fName)
    except IOError:
        print 'File named %s not found.'%fName
    else:   #file opened correctly
        nbaDict = {}
        for line in fd:
            if 'ilkid' in line:
                continue
            calcEfficiency(line, nbaDict)
        results = findMostEfficient(nbaDict, 20)
        printResults(results)
        fd.close()

if __name__ == '__main__':
    main()        