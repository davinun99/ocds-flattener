select 
	r.ocid,
	data['compiledRelease']['contracts']
	-- COALESCE(jsonb_array_length(data['compiledRelease']['contracts']), 0) as "contracts.count"
	-- (select string_agg(d['implementation']::text, '||') from jsonb_array_elements(data['compiledRelease']['contracts']) d) as "contracts.statusDetails.concat"
FROM RECORD r join data d on d.id = r.data_id 
-- where (select string_agg(d['id']::text, '||') from jsonb_array_elements(data['compiledRelease']['tender']['criteria']) d) != '"1'
-- where data['compiledRelease']['tender']['participationFees'] is not null
limit 150