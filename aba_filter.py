import re

def aba_MLP(highlight):
    bmi_compile = re.compile(r'(\bBMI:?\s*[0-9]\w+|\bBMI Calculated:?\s*[0-9]\w+)', flags=re.IGNORECASE),
    body_mass_index_compile = re.compile(r'(\bbody mass index:?\s*[^a-zA-Z]\s*[0-9]\w+|\bBody Mass Index Calculated:?\s*[^a-zA-Z]\s*[0-9]\w+)',flags=re.IGNORECASE),
    kg_m2_compile = re.compile(r'([0-9]+([,.][0-9]+)?\skg\/m2\s)', flags=re.IGNORECASE),
	#ht_compile = #re.compile(r'(\bHeight\s*[^a-zA-Z]\s*[0-9]\w+|\bHt\s*[^a-zA-Z]\s*[0-9]\w+)',
            #flags=re.IGNORECASE),
    wt_compile = re.compile(r'(\bW(e|E)(i|I)(g|G)(h|H)(t|T)\s*[^a-zA-Z]\s*[0-9]\w+|\bW(g|G)?(t|T)\s*[^a-zA-Z]\s*[0-9]\w+)', flags=re.IGNORECASE)
    result = None

    

    for i in bmi_compile:
            res = i.search(highlight)
            if res:
                return True
                
    for i in body_mass_index_compile:
            res = i.search(highlight)
            if res:
                return True
                
    for i in kg_m2_compile:
        res = i.search(highlight)
        if res:
            return True
    return False
	# if not ht:
		# for i in ht_compile:
			# res = i.search(line)
			# if res:
				# ht = True
				# break

	# if not wt:
		# for i in wt_compile:
			# res = i.search(line)
			# if res:
				# wt = True
				# break
    	#if ht and wt and bmi:
    