def calcEfficiency(line,theDict):
    #asserts on the parameters
    assert isinstance(theDict, dict),\
            'bad parameter ,expected a dictionary,got %s'%theDict
    assert isinstance(line, str) and line != '',\
            'bad parameter ,expected string ,got %s'%line
            
    line = line.strip()
    fields = line.split(',')
    firstName = fields[1]
    lastName = fields[2]
    
    #mapping fields in a line to their particular variable.
    #league is a str ,everything else an int 
    leag,gp,mins,pts,ored,dreb,reb,asts,\
    stl,blk,to,pf,fga,fgm,fta,ftm,tpa,tpm = \
    fields[3],int(fields[4]),int(fields[5]),int(fields[6]),int(fields[7]),\
    int(fields[8]),int(fields[9]),int(fields[10]),int(fields[11]),int(fields[12]),\
    int(fields[13]),int(fields[14]),int(fields[15]),int(fields[16]),int(fields[17]),\
    int(fields[18]),int(fields[19]),int(fields[20])
    
    #gp can't be 0
    assert gp != 0 ,'%s %s has no games played'%(firstName,lastName)
    
    #need to address this problem!
    #assert lastName+firstName not in theDict
    #'duplicate on name %s'%(firstName+lastName)
    
    #calculate the player's efficiency
    efficiency = ((pts+reb+asts+stl+blk)-((fga-fgm)+(fta-ftm)+to))/float(gp)
    
    theDict[lastName+firstName] = {'first':firstName,'last':lastName,\
                                   'league':leag,'mins':mins,'gp':gp,\
                                   'pts':pts,'ored':ored,'dreb':dreb,'reb':reb,\
                                   'asts':asts,'stl':stl,'blk':blk,'to':to,'pf':pf,\
                                   'fga':fga,'fgm':fgm,'fta':fta,'ftm':ftm,'tpa':tpa,\
                                   'tpm':tpm,'efficiency':efficiency 
                                   }