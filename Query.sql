select 
	data['compiledRelease']['ocid'] as "id",
	data['compiledRelease']['contracts'] as "contracts"
FROM RECORD r join data d on d.id = r.data_id 