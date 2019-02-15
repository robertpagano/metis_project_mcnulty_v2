def filter_by_outcome(df, type1='Adoption', type2='Transfer'):
	"""
	this will take a dataframe, and return the same dataframe but filtered by 2 specific outcome types. If not specified, will return "adopted" and "transferred"
	"""
	df = df.loc[(df['outcome_type'] == type1) | (df['outcome_type'] == type2)]
