import json
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from pprint import pprint
from nltk.tokenize import word_tokenize
from nltk.corpus import brown 

class StanfordNLP:
    def __init__(self):
        self.server = ServerProxy(JsonRpc20(),
                                  TransportTcpIp(addr=("10.129.2.170", 8082),timeout=100000.0))
    
    def parse(self, text):
        return json.loads(self.server.parse(text))

pronouns= {'he','she','him','his','her','hers','himself','herself',
             'mine', 'your','yourself',
            'our','ours','ourself','ourselves',
            'it','its','itself',
            'what','whatever','which','whichever','who','whoever','whom','whomever','whose','what','whatever',
            'that','there','their','theirs','them','themselves','these','they','this','those','theirself','theirselves','themselves'}

#'my','me', 'i','you','we','us',

nlp = StanfordNLP()
brown_files = brown.fileids()
brown_files.remove('ca11')
brown_files.remove('ca39')
brown_files.remove('ce01')
brown_files.remove('ce14')
brown_files.remove('ce24')
brown_files.remove('ce27')
brown_files.remove('cf06')
brown_files.remove('cf10')
brown_files.remove('cf16')
brown_files.remove('cf34')
brown_files.remove('cg48')
brown_files.remove('cg64')
brown_files.remove('cj08')
brown_files.remove('cj56')
brown_files.remove('cj77')
brown_files.remove('ck14')
brown_files.remove('cl20')
brown_files.remove('cl22')
brown_files.remove('cm04')
brown_files.remove('cn15')

brown_files.remove('cd02')
brown_files.remove('cf35')
brown_files.remove('cj19')
brown_files.remove('cn16')

brown_files.remove('ch09')
brown_files.remove('ch12')
#'ca11','ca39','ce01','ce14','ce24','ce27','cf06','cf10','cf16','cf34','cg48','cg64','cj08','cj56','cj77','ck14','cl20','cl22','cm04','cn15','cd02','cf35','cj19','cn16','ch09','ch12'

f_out= open("coref_brown_temp2.txt",'w')

for f in brown_files[brown_files.index('ch10'):]:
    inp = ''
    c=0
    docs_parse=[]
    print "parsing:"+str(f)
    for para in brown.paras(f):
        for sent in para: 
	    #print len(sent)
            #print sent
            #if len(sent)>=40:
                #continue
            for word in sent:
                c+=len(word)
                c+=1
            if c >= 4094:
                # print c
                c=0
                for word in sent:
                    c+=len(word)
                    c+=1
                # print inp
                # print len(inp)
                # print inp
                doc = nlp.parse(inp)
                docs_parse.append(doc)
                inp=''
            
            inp += ' '.join(sent)
            inp += ' '
            # inp = inp.replace('; ;','.')
    # print inp        
    doc = nlp.parse(inp)
    docs_parse.append(doc)


    for doc in docs_parse:
		sents=[]    
		for x in doc['sentences']:
			# print x['text']
			sents.append(word_tokenize(x['text']))
		# print "*********************************************"
		print brown_files.index(f)
		print f, len(sents)


		#print sents
		# print result['coref']
		# print result['text']
		if 'coref' in doc.keys():
			if len(doc['coref'])>0:
				for chain in doc['coref']:
					#print chain
					for pair in chain:
						#print pair
						#replacing pronounds with antecedents
						if pair[0][0].lower() in pronouns:
							sents[pair[0][1]][pair[0][3]] = pair[1][0] 
				
		for sent in sents:
			# print ' '.join(sent)
			f_out.write(' '.join(sent))
			f_out.write('\n')
		f_out.write('\n')# "********************************************************"
        
f_out.close()
