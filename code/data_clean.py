def filter_by_outcome(df):
	"""
	this will take a dataframe, and return the same dataframe but filtered by "adopted" and "transferred" outcome statuses
	"""
	df_2 = df.loc[(df['outcome_type'] == 'Adoption') | (df['outcome_type'] == 'Transfer')]
	return df_2
	
