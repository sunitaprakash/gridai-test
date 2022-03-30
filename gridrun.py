 
  
  import re
with open('extraction.txt') as file:
  data = file.read()

# regex for extracting durations as we currently report them. Assumes followinf format 7d-03:50:37
prog = re.compile('[0-9][d][-][0-9][0-9][:][0-9][0-9][:][0-9][0-9]')
count = 0
for element in data.split():
  if prog.match(element) is not None:
    count +=1
  if count == 2:
    # the second duration is the run duration the first is the queued duration
    return prog.match(element).group(0)

  
  
  def status_run(self, 
  id:str,
  status2:str='succeeded|cancelled|failed|stopped',
  status3:str='succeeded',
  filter1:str = "Experiment.str.contains(@id)",  
  filter2:str = "Status.str.contains(@status2,case=False)", 
  filter3:str = "Status.str.contains(@status3,case=False)",  
  lb=1,ub=None,  # desired cardinality of lower and upper bound 
  status_col="Status",
  id_col="Experiment",
  type="run", 
  filter1_len:int = None,
  filter2_len:int = None,
  ):
